# OpenCV QR Code Detection Project

This project demonstrates QR code detection and decoding using OpenCV and PyZbar. It processes video frames captured from a camera, enhances the frame for better QR code visibility, detects QR codes, decodes their data, and displays the results with bounding boxes on the video feed.

Additionally, the project supports using the **iRuin** mobile app to stream camera footage for QR code detection. This makes it easier to test the functionality with a mobile device.

## Features

- **Preprocessing**: Enhances the frame using grayscale conversion, CLAHE (Contrast Limited Adaptive Histogram Equalization), and Gaussian blur.
- **QR Code Detection**: Uses PyZbar to detect QR codes in the video frames.
- **Data Decoding**: Extracts and displays the decoded data from QR codes.
- **Real-time Visualization**: Draws bounding boxes and shows decoded data on the video feed.
- **Mobile App Integration**: Use the **iRuin** app to stream camera input from your mobile phone to the application.
