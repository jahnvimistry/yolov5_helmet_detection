import torch
import cv2
from yolov5 import detect

def run_inference():
    # Load model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # Or load custom trained model

    # For custom model, uncomment below:
    # model = torch.load('runs/train/helmet_detection/weights/best.pt')

    # Run inference on an image
    img_path = 'data/images/val/hard_hat_workers0.png'  # Replace with actual image path
    results = model(img_path)

    # Display results
    results.show()

    # Save results
    results.save(save_dir='runs/detect')

    print("Inference completed. Check runs/detect for results.")

if __name__ == "__main__":
    run_inference()
