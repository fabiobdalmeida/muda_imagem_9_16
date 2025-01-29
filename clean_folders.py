import os
import shutil

# Define the folders to clean
folders_to_clean = ["input_images", "output_images"]

def clean_folder(folder_path):
    """Deletes all files in the specified folder while keeping the folder itself."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the folder if it doesn't exist
        print(f"Created missing folder: {folder_path}")
        return
    
    # Delete all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove file or symbolic link
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove subdirectory
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    for folder in folders_to_clean:
        clean_folder(folder)
    print("✅ Cleanup completed successfully!")