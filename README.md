# YOLOv5 Helmet Detection Mini Project

This is a simple mini project for object detection using YOLOv5, focused on detecting helmets.

## Setup

1. Clone YOLOv5 and install dependencies:
   ```
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

2. Prepare dataset:
   - Run `python download_dataset.py` to create dataset structure.
   - Add real images to `data/images/train` and `data/images/val`.
   - Add corresponding labels (YOLO format) to `data/labels/train` and `data/labels/val`.

## Training

Run `python train.py` to train the model. This uses pre-trained YOLOv5s weights and fine-tunes on your dataset.

## Inference

Run `python infer.py` to perform inference on an image. Update the `img_path` in the script.

## Notes

- This is a basic setup. For real use, obtain a proper dataset from sources like Roboflow or Kaggle.
- Training time depends on dataset size and hardware.
- Customize parameters in the scripts as needed.
=======
# YOLOv5 Helmet Detection Mini Project

This is a simple mini project for object detection using YOLOv5, focused on detecting helmets.

## Setup

1. Clone YOLOv5 and install dependencies:
   ```
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

2. Prepare dataset:
   - Run `python download_dataset.py` to create dataset structure.
   - Add real images to `data/images/train` and `data/images/val`.
   - Add corresponding labels (YOLO format) to `data/labels/train` and `data/labels/val`.

## Training

Run `python train.py` to train the model. This uses pre-trained YOLOv5s weights and fine-tunes on your dataset.

## Inference

Run `python infer.py` to perform inference on an image. Update the `img_path` in the script.

## Notes

- This is a basic setup. For real use, obtain a proper dataset from sources like Roboflow or Kaggle.
- Training time depends on dataset size and hardware.
- Customize parameters in the scripts as needed.
=======
# yolov5_helmet_detection
>>>>>>> 4a6ad5854d041bd55d3e6b98519de4e886fb9d41
