import cv2
import numpy as np
from lane_detection import process_frame, detect_lines, draw_lane_curves

def process_video(video_path):
    # Capture video from file
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to standardize size
        width = 800  # Desired width of the resized frame
        frame_resized = resize_frame(frame, width)

        # Process the frame
        edges = process_frame(frame_resized)
        lines = detect_lines(edges)
        result_frame = draw_lane_curves(frame_resized, lines)

        # Display the result
        cv2.imshow("Lane Detection", result_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def resize_frame(frame, width):
    """Resize the frame to a specific width while maintaining the aspect ratio."""
    aspect_ratio = width / float(frame.shape[1])
    height = int(frame.shape[0] * aspect_ratio)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    return resized

def process_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Resize the image to standardize size
    width = 800  # Desired width of the resized image
    image_resized = resize_frame(image, width)

    # Process the image
    edges = process_frame(image_resized)
    lines = detect_lines(edges)
    result_image = draw_lane_curves(image_resized, lines)

    # Display the result
    cv2.imshow("Lane Detection", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Uncomment the line you need to use
    # For processing video
    choice=input("if image enter 'image'else type 'video' done:")
    if(choice=="video"):
     video_path = r'D:\task-1\dataset\lane_images\testvideo.mp4'  # Path to your video file
     process_video(video_path)
    elif(choice=="image"):
     image_path = r'D:\task-1\dataset\lane_images\image3.jpg'  # Path to your image file
     process_image(image_path)
    else:
       print("wrong inputs")