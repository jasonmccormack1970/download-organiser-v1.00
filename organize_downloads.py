import shutil
from pathlib import Path

# --- Configuration ---
# By default, this script will organize the user's Downloads folder.
# You can change this to any other folder by modifying the path below.
TARGET_DIRECTORY = Path.home() / "Downloads"
print (f"Target directory set to: {TARGET_DIRECTORY}")

# This dictionary maps folder names to the file extensions they should contain.
# You can add new categories or add/remove extensions from existing ones.
FILE_TYPE_MAPPINGS = {
    "Images": (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"),
    "Documents": (".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"),
    "Audio": (".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"),
    "Video": (".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"),
    "Archives": (".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"),
    "Executables": (".exe", ".msi", ".dmg", ".app", ".deb", ".rpm"),
    "Code": (".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".sh", ".json", ".xml"),
    # Any file with an extension not listed above will go into the "Other" folder.
}
# --- End of Configuration ---

def organize_folder(target_dir: Path):
    """
    Organizes files in the target directory into subdirectories based on file type.

    :param target_dir: The path to the directory to organize.
    """
    if not target_dir.is_dir():
        print(f"Error: Directory not found at '{target_dir}'")
        return

    print(f"Starting organization of '{target_dir}'...")

    # Create a reverse mapping from extension to folder name for efficient lookups
    extension_to_folder = {
        ext: folder
        for folder, extensions in FILE_TYPE_MAPPINGS.items()
        for ext in extensions
    }

    # Iterate over each item in the target directory
    for item in target_dir.iterdir():
        # Skip directories and the script itself
        if item.is_dir() or item.resolve() == Path(__file__).resolve():
            continue

        # Determine the destination folder
        file_extension = item.suffix.lower()
        dest_folder_name = extension_to_folder.get(file_extension, "Other")
        dest_folder_path = target_dir / dest_folder_name

        # Create the destination folder if it doesn't exist
        dest_folder_path.mkdir(exist_ok=True)

        # Handle potential file name collisions to avoid overwriting
        dest_file_path = dest_folder_path / item.name
        counter = 1
        while dest_file_path.exists():
            # Create a new name like 'file (1).ext', 'file (2).ext'
            new_name = f"{item.stem} ({counter}){item.suffix}"
            dest_file_path = dest_folder_path / new_name
            counter += 1

        # Move the file to the new destination
        shutil.move(str(item), str(dest_file_path))
        print(f"Moved: '{item.name}'  ->  '{dest_folder_path.name}/{dest_file_path.name}'")

if __name__ == "__main__":
    organize_folder(TARGET_DIRECTORY)
    print("\nOrganization complete!")