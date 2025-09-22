import os
import shutil

# 定義分類規則
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf", ".md"],
    "Music": [".m4a", ".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".sh", ".json"],
    "Others": [],  # 其他未分類檔案
}


# Source folder
downloads_folder = os.getcwd() + "/Downloads"

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