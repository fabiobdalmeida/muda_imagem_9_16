from PIL import Image
import os

def adjust_to_vertical_9_16(input_folder, output_folder):
    """
    Adjust images to a 9:16 vertical ratio by cropping the center.

    Parameters:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where processed images will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                target_ratio = 9 / 16

                # Calculate new dimensions
                current_ratio = width / height

                if current_ratio > target_ratio:
                    # Image is too wide, crop horizontally
                    new_width = int(height * target_ratio)
                    left = (width - new_width) // 2
                    right = left + new_width
                    top = 0
                    bottom = height
                else:
                    # Image is too tall, crop vertically
                    new_height = int(width / target_ratio)
                    top = (height - new_height) // 2
                    bottom = top + new_height
                    left = 0
                    right = width

                # Crop and save the image
                cropped_img = img.crop((left, top, right, bottom))
                output_path = os.path.join(output_folder, file_name)

                cropped_img.save(output_path)
                print(f"Processed and saved: {output_path}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Example usage
input_folder = "input_images"  # Folder with original images
output_folder = "output_images"  # Folder to save the processed images

adjust_to_vertical_9_16(input_folder, output_folder)