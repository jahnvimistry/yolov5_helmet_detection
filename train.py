import torch
from yolov5 import train

def train_model():
    # Set device
    device = 'cpu'  # Force CPU to avoid YAML serialization issues
    print(f"Using device: {device}")

    # Training parameters
    data_yaml = 'data/data.yaml'  # Path to data.yaml
    weights = 'yolov5s.pt'  # Pre-trained weights
    epochs = 10  # Small number for demo
    batch_size = 16
    img_size = 640

    # Run training
    train.run(
        data=data_yaml,
        weights=weights,
        epochs=epochs,
        batch_size=batch_size,
        imgsz=img_size,
        device=device,
        project='runs/train',  # Save results here
        name='helmet_detection'
    )

if __name__ == "__main__":
    train_model()
