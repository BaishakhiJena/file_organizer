import os
import shutil

print("📂 Organizing files...\n")

file_types = {
    "Images": [".jpg",".jpeg",".png"],
    "Videos": [".mp4",".mov"],
    "Documents": [".pdf",".txt",".docx"],
    "Music": [".mp3",".wav"]
}
source_folder = "test"
files=os.listdir(source_folder)

for folder in file_types:
    folder_path=os.path.join(source_folder,folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in files:
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():

            if file.lower().endswith(tuple(extensions)):

                destination = os.path.join(source_folder, folder, file)

                shutil.move(file_path, destination)

                print(f"Moved {file} → {folder}")

print("\n✅ Files organized successfully!")