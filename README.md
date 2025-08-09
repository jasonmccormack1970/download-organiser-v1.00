# Downloads Folder Organizer

A simple yet powerful Python script to automatically organize your cluttered Downloads folder (or any other directory) by moving files into categorized subfolders based on their file type.

---

## ✨ Features

- **📂 Automatic Categorization**: Sorts files into pre-defined folders like `Images`, `Documents`, `Video`, `Archives`, etc.
- **🔧 Easily Configurable**: You can change the target directory and customize the file-to-folder mappings directly within the script.
- **🚫 Collision-Proof**: Automatically renames files if a file with the same name already exists in the destination (e.g., `report.pdf` becomes `report (1).pdf`), preventing accidental overwrites.
- **💡 Smart & Safe**: Intelligently skips over sub-directories and won't attempt to move the script file itself.
- **🚀 Cross-Platform**: Works on Windows, macOS, and Linux, thanks to Python's `pathlib`.

## 📋 Requirements

- **Python 3.6+**

No external libraries are needed; this script only uses modules from the Python standard library.

## ⚙️ Setup & Usage

1.  **Download the Script**: Save the `organize_downloads.py` file to your computer. You can place it anywhere.

2.  **Run from Terminal**: Open a terminal (Command Prompt, PowerShell, or Terminal) and run the script with Python.

    ```bash
    python organize_downloads.py
    ```

The script will immediately start organizing the files in the configured `TARGET_DIRECTORY`. You will see a log of each file being moved.

## 🛠️ Configuration

You can easily customize the script's behavior by editing the configuration variables at the top of the `organize_downloads.py` file.

### Changing the Target Directory

By default, the script targets your user's `Downloads` folder. To change this, simply modify the `TARGET_DIRECTORY` variable to your desired path.

```python
# Before
TARGET_DIRECTORY = Path.home() / "Downloads"

# After (Example: Targeting the Desktop)
TARGET_DIRECTORY = Path.home() / "Desktop"
```

### Customizing File Categories

The `FILE_TYPE_MAPPINGS` dictionary controls which file extensions go into which folders. You can add new categories, add new file extensions to existing categories, or change the folder names.

For example, to add a new category for `E-books` and add the `.epub` and `.mobi` file types, you would add a new line to the dictionary:

```python
FILE_TYPE_MAPPINGS = {
    "Images": (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"),
    "Documents": (".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"),
    # ... other categories
    "E-books": (".epub", ".mobi"), # <-- Add your new category here
}
```

Files with extensions not found in this mapping will be automatically placed in a folder named `Other`.

## 📄 License

This project is open-source and available under the MIT License.
