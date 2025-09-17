import os
import shutil

# 定義分類規則
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}
# Please git clone the whole directory then execute app.py in "114_scripting"
# Source folder
downloads_folder = os.path.join("homework/0917/Downloads")

# Make folder
for folder in file_types.keys():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create others => while not included in file_types
others_folder = os.path.join(downloads_folder, "Others")
if not os.path.exists(others_folder):
    os.makedirs(others_folder)

# check all files in downloads
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # make sure the files are not folderz
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)  # get file extensions
        ext = ext.lower()  # make them lower case

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_path = os.path.join(downloads_folder, folder, filename)
                shutil.move(file_path, target_path) # replace os.rename
                print(f"Moved: {filename} -> {folder}")
                moved = True
                break

        # the file extension is not accorded to the lists -> Others
        if not moved:
            target_path = os.path.join(others_folder, filename)
            shutil.move(file_path, target_path) # replace os.rename
            print(f"Moved: {filename} -> Others")

print("Operation is done.")