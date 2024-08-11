# -Road-Lane-Line-Detection-System
This project aims to develop a robust Road Lane Detection System to enhance road safety by accurately detecting lane markings in real-time. The system utilizes state-of-the-art computer vision and machine learning techniques to identify lane boundaries, providing real-time feedback to drivers.

# Lane Detection using OpenCV

This project implements a lane detection system using Python and OpenCV. It processes video or image inputs to detect and highlight lanes on a road, useful for autonomous driving systems or driver assistance.

## Features

- Detects lane lines on the road from video or image inputs.
- Highlights the detected lanes with green color for easy visualization.
- Dynamic resizing of frames for consistent processing.
- Uses edge detection and Hough Line Transform for lane detection.
- Adjustable region of interest (ROI) for fine-tuning the lane detection.

## Requirements

- Python 3.7+
- OpenCV 4.x
- NumPy



### Adjusting Parameters

- **Region of Interest (ROI):** Adjust the ROI vertices in the `process_frame` function in `lane_detection.py` to fine-tune which part of the frame is analyzed for lanes.
- **Line Detection:** Modify the parameters in the `detect_lines` function to adjust sensitivity and accuracy of line detection.

## Code Structure

- `main.py`: The main script to run lane detection on videos or images.
- `lane_detection.py`: Contains functions for processing frames, detecting edges, finding lines, and drawing the lanes.
  - `process_frame(frame)`: Converts frames to grayscale, applies Gaussian blur, detects edges, and applies the ROI mask.
  - `region_of_interest(img, vertices)`: Masks the frame to focus on the region of interest.
  - `detect_lines(edges)`: Uses the Hough Line Transform to detect lines in the masked frame.
  - `draw_lane_curves(frame, lines)`: Draws the detected lanes and fills the lane area with green color.
  - `make_coordinates(frame, line_fit, y1, y2)`: Converts line slope and intercept to coordinates for drawing.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

