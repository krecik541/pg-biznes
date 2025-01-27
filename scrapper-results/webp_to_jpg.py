import os
from PIL import Image

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMAGES_DIR = os.path.join(BASE_DIR, 'scrapper-results', 'images')
JPG_IMAGES_DIR = os.path.join(BASE_DIR, 'scrapper-results', 'images_to_jpg')

# webp to jpg
def convert_webp_to_jpg(webp_path, jpg_path):
    try:
        with Image.open(webp_path) as img:
            img = img.convert("RGB")
            img.save(jpg_path, "JPEG", quality=90)
            print(f"Przekonwertowano: {webp_path} → {jpg_path}")
    except Exception as e:
        print(f"Błąd przy konwersji {webp_path} → {jpg_path}: {e}")

def convert_all_images():
    os.makedirs(JPG_IMAGES_DIR, exist_ok=True)

    for filename in os.listdir(IMAGES_DIR):
        if filename.endswith('.webp'):
            webp_path = os.path.join(IMAGES_DIR, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(JPG_IMAGES_DIR, jpg_filename)

            convert_webp_to_jpg(webp_path, jpg_path)

if __name__ == '__main__':
    convert_all_images()
