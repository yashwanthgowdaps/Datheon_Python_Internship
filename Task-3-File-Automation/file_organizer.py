
import os
import shutil

# Task 3: File Automation
# Datheon Python Programming Internship


def get_category(filename):
    """Return a folder name based on the file extension."""

    extension = os.path.splitext(filename)[1].lower()

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "PDF_Files": [".pdf"],
        "Documents": [".txt", ".doc", ".docx", ".odt", ".rtf"],
        "Code_Files": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
        "Spreadsheets": [".csv", ".xls", ".xlsx"],
        "Presentations": [".ppt", ".pptx"],
        "Audio_Files": [".mp3", ".wav", ".aac", ".ogg"],
        "Video_Files": [".mp4", ".mkv", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
    }

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Other_Files"


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""

    if not os.path.exists(destination):
        return destination

    folder = os.path.dirname(destination)
    filename = os.path.basename(destination)
    name, extension = os.path.splitext(filename)

    counter = 1

    while True:
        new_name = f"{name}_{counter}{extension}"
        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def organize_files(folder_path):
    """Organize files into folders based on their types."""

    folder_path = os.path.abspath(
        os.path.expanduser(folder_path)
    )

    if not os.path.isdir(folder_path):
        print("Error: The folder does not exist.")
        print("Please enter a valid folder path.")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0

    print("\nStarting file organization...")
    print("Folder:", folder_path)

    try:
        # Take a snapshot of the folder contents.
        filenames = os.listdir(folder_path)
    except OSError as error:
        print("Could not read the folder:", error)
        return

    for filename in filenames:
        source_path = os.path.join(folder_path, filename)

        # Organize files only, not subfolders.
        if not os.path.isfile(source_path):
            continue

        category = get_category(filename)
        destination_folder = os.path.join(
            folder_path, category
        )

        try:
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(
                destination_folder, filename
            )

            # Protect existing files from being overwritten.
            destination_path = get_unique_path(destination_path)

            shutil.move(source_path, destination_path)

            print(f"Moved: {filename} -> {category}/")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {filename}: {error}")
            error_count += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved_count)
    print("Files skipped:", skipped_count)
    print("Errors:", error_count)
    print("Organization finished.")


def main():
    print("===== FILE ORGANIZER =====")
    print("This program sorts files into folders by type.")

    default_path = (
        "/storage/emulated/0/Download/test_files"
    )

    print("\nExample folder path:")
    print(default_path)

    folder_path = input(
        "\nEnter folder path to organize: "
    ).strip().strip('"').strip("'")

    if not folder_path:
        print("No folder path entered. Program stopped.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
    