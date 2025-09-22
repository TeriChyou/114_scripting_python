import os

# 定義分類規則
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

# source folder
downloads_folder = os.getcwd() + "/Downloads"

# Make folder
for folder in file_types:
    folder_path = f"{downloads_folder}/{folder}"
    os.makedirs(folder_path, exist_ok=True)

# Make "Others" folders
others_folder = f"{downloads_folder}/Others"
os.makedirs(others_folder, exist_ok=True)

# Move files according to filename
for filename in os.listdir(downloads_folder):
    file_path = f"{downloads_folder}/{filename}"

    if not os.path.isfile(file_path):
        continue

    ext = os.path.splitext(filename)[1].lower()

    for folder, extensions in file_types.items():
        if ext in extensions:
            target_path = f"{downloads_folder}/{folder}/{filename}"
            os.rename(file_path, target_path)
            print(f"Moved: {filename} -> {folder}")
            break
    else:
        target_path = f"{others_folder}/{filename}"
        os.rename(file_path, target_path)
        print(f"Moved: {filename} -> Others")

print("Operation is done.")
