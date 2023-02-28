from pathlib import Path
import shutil

category = {"Images": ['.jpg', '.jpeg', '.png', '.svg'],
            "Documents": ['.doc', '.docx', 'txt', '.pdf', '.xlsx', '.pptx'],
            "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
            "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
            "Video": [".avi", ".mov", ".mp4", ".mkv"],
            "PDF": [".pdf"],
            "Unknown": []}  

folder = Path(input("Enter the path to the folder: "))  

print(f"Sorting files in {folder}...")

for file in folder.iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()
        category_found = False
        for category_name, category_extensions in category.items():
            if file_extension in category_extensions:
                category_folder = folder / category_name
                category_folder.mkdir(exist_ok=True)
                shutil.move(str(file.absolute()), str(category_folder / file.name))
                print(f"Moved file {file.name} to {category_name} folder.")
                category_found = True
                break
        if not category_found:
            unknown_folder = folder / "Unknown"
            unknown_folder.mkdir(exist_ok=True)
            shutil.move(str(file.absolute()), str(unknown_folder / file.name))
            print(f"Moved file {file.name} to Unknown folder.")
            
print("File sorting complete.")