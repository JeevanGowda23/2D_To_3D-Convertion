import cv2
import numpy as np

def estimate_depth(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")

    # Normalize the image to range 0-1
    img_normalized = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)

    # Apply edge detection
    edges = cv2.Canny((img_normalized * 255).astype(np.uint8), 100, 200)

    # Invert edges to create a pseudo-depth map
    depth_map = cv2.bitwise_not(edges)

    return depth_map
