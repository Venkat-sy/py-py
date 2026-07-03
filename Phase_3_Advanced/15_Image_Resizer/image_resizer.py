"""
Project 15: Image Resizer
External Requirements: pip install Pillow
"""
from PIL import Image

def resize_image(size1, size2):
    # Ensure you have a 'test.jpg' in the directory to test this!
    try:
        image = Image.open('test.jpg')
        print(f"Current size: {image.size}")
        resized_image = image.resize((size1, size2))
        resized_image.save('test_resized.jpg')
        print("Image resized successfully.")
    except Exception as e:
        print("Error: Provide a test.jpg image in this folder to run this code.")

# resize_image(500, 500)
