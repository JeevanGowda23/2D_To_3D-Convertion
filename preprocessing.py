import cv2

def process_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save processed image
    processed_image_path = image_path.replace('.png', '_processed.png')
    cv2.imwrite(processed_image_path, gray)

    return processed_image_path
