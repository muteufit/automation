import os
import shutil

def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            extension = filename.split('.')[-1]
            extension_folder = os.path.join(destination_folder, extension)

            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(extension_folder, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {extension} folder.")

if __name__ == "__main__":
    source_folder = "/path/to/source/folder"
    destination_folder = "/path/to/destination/folder"

    organize_files(source_folder, destination_folder)
