import cv2
import numpy as np

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    height, width = edges.shape
    # Adjusted ROI vertices to limit the upper area of the lane detection
    roi_vertices = [
        (int(width * 0.2), height),
        (int(width * 0.4), int(height * 0.7)),  # Moved lower for less green area
        (int(width * 0.6), int(height * 0.7)),  # Moved lower for less green area
        (int(width * 0.8), height)
    ]
    roi_edges = region_of_interest(edges, np.array([roi_vertices], np.int32))

    return roi_edges


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def detect_lines(edges):
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=50,
        minLineLength=40,
        maxLineGap=100
    )
    return lines

def draw_lane_curves(frame, lines):
    left_fit = []
    right_fit = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1 + 1e-6)
            intercept = y1 - slope * x1
            if slope > 0.5:  # Right lane
                right_fit.append((slope, intercept))
            elif slope < -0.5:  # Left lane
                left_fit.append((slope, intercept))

    left_fit_avg = np.mean(left_fit, axis=0) if left_fit else None
    right_fit_avg = np.mean(right_fit, axis=0) if right_fit else None

    y1 = frame.shape[0]
    y2 = int(y1 * 0.7)  # Adjusted y2 to match the ROI

    left_line = make_coordinates(frame, left_fit_avg, y1, y2) if left_fit_avg is not None else None
    right_line = make_coordinates(frame, right_fit_avg, y1, y2) if right_fit_avg is not None else None

    if left_line is not None:
        cv2.line(frame, left_line[:2], left_line[2:], (0, 255, 0), 10)
    if right_line is not None:
        cv2.line(frame, right_line[:2], right_line[2:], (0, 255, 0), 10)

    if left_line is not None and right_line is not None:
        # Adjusted the polygon points to match the lane boundaries
        poly_points = np.array([[left_line[2:], left_line[:2], right_line[:2], right_line[2:]]])
        cv2.fillPoly(frame, poly_points, (0, 255, 0))

    return frame


def make_coordinates(frame, line_fit, y1, y2):
    slope, intercept = line_fit
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])
