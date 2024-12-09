import cv2
from pyzbar.pyzbar import decode
import numpy as np

def preprocess_frame(frame):
    """
    Preprocess the input frame to enhance QR code visibility.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)
    
    return blurred

def detect_qr_codes(frame):
    """
    Detect and decode QR codes in the input frame.
    """
    qr_codes = decode(frame)
    detected_data = []

    for qr_code in qr_codes:
        points = qr_code.polygon
        qr_data = qr_code.data.decode('utf-8')
        rect = qr_code.rect

        if len(points) == 4:
            detected_data.append({
                "data": qr_data,
                "points": [(int(point.x), int(point.y)) for point in points],
                "rect": (rect.left, rect.top)
            })
    
    return detected_data

def draw_detected_qr(frame, qr_data_list):
    """
    Draw bounding boxes and data on the frame for detected QR codes.
    """
    for qr_data in qr_data_list:
        points = qr_data["points"]
        for i in range(4):
            cv2.line(frame, points[i], points[(i + 1) % 4], (0, 255, 0), 2)
        
        # Display decoded data near the QR code
        cv2.putText(frame, qr_data["data"], 
                    (qr_data["rect"][0], qr_data["rect"][1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, 
                    (0, 255, 0), 
                    2)

def main():
    # Initialize video capture (camera index 2 ajusted as per the requirement)
    cap = cv2.VideoCapture(2)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame")
            break
        
        processed_frame = preprocess_frame(frame)
        
        # Detect QR codes
        detected_qr_codes = detect_qr_codes(processed_frame)

        # Print the decoded data from QR codes
        for qr_data in detected_qr_codes:
            print(f"Decrypted QR Code Data: {qr_data['data']}")
        
        # Draw detected QR codes on the original frame
        draw_detected_qr(frame, detected_qr_codes)
        cv2.imshow('QR Code Detection', frame)

        # Break loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
