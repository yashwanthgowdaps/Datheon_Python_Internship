# Task 3: File Automation
# Datheon Python Programming Internship

import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "PDF_Files": [".pdf"],
    "Documents": [".txt", ".doc", ".docx", ".odt", ".rtf"],
    "Code_Files": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx"],
    "Audio_Files": [".mp3", ".wav", ".aac", ".ogg"],
    "Video_Files": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(filename):
    """Return a folder name based on the file extension."""
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other_Files"


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not os.path.exists(destination):
        return destination

    folder = os.path.dirname(destination)
    name, extension = os.path.splitext(os.path.basename(destination))

    counter = 1
    while True:
        new_path = os.path.join(folder, f"{name}_{counter}{extension}")
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def organize_files(folder_path):
    """Organize files into folders based on their types."""
    folder_path = os.path.abspath(os.path.expanduser(folder_path))

    if not os.path.isdir(folder_path):
        print("Error: The folder does not exist.")
        print("Please enter a valid folder path.")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0
    this_script = os.path.abspath(__file__)

    print("\nStarting file organization...")
    print("Folder:", folder_path)

    try:
        filenames = os.listdir(folder_path)
    except OSError as error:
        print("Could not read the folder:", error)
        return

    for filename in filenames:
        source_path = os.path.join(folder_path, filename)

        # Skip subfolders, hidden/system files and this script itself.
        if (
            not os.path.isfile(source_path)
            or filename.startswith(".")
            or os.path.abspath(source_path) == this_script
        ):
            skipped_count += 1
            continue

        category = get_category(filename)
        destination_folder = os.path.join(folder_path, category)

        try:
            os.makedirs(destination_folder, exist_ok=True)
            destination_path = get_unique_path(
                os.path.join(destination_folder, filename)
            )
            shutil.move(source_path, destination_path)

            print(f"Moved: {filename} -> {category}/")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {filename}: {error}")
            error_count += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved_count)
    print("Items skipped:", skipped_count)
    print("Errors:", error_count)
    print("Organization finished.")


def main():
    print("===== FILE ORGANIZER =====")
    print("This program sorts files into folders by type.")

    print("\nExample folder path:")
    print(os.path.join(os.path.expanduser("~"), "Downloads"))

    try:
        folder_path = input(
            "\nEnter folder path to organize: "
        ).strip().strip('"').strip("'")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram stopped.")
        return

    if not folder_path:
        print("No folder path entered. Program stopped.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
