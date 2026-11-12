# Task 3: Automated File Organizer & Cleanup Utility
# Datheon Python Programming Internship

import logging
import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    "Documents": [".pdf", ".txt", ".doc", ".docx", ".odt", ".rtf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx"],
}

DEFAULT_CATEGORY = "Others"
SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "organizer.log"

logger = logging.getLogger("organizer")


def setup_logging():
    """Log to the screen and, if possible, to organizer.log."""
    if logger.handlers:
        return
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(console)
    try:
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s  %(levelname)s  %(message)s")
        )
        logger.addHandler(file_handler)
    except OSError:
        pass


def get_category(filename):
    """Return the category folder name for a file, based on its extension."""
    extension = Path(filename).suffix.lower()
    for category, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return category
    return DEFAULT_CATEGORY


def unique_path(destination):
    """Avoid overwriting: report.pdf -> report_1.pdf -> report_2.pdf ..."""
    destination = Path(destination)
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize_files(folder_path):
    """Sort the files in folder_path into category subfolders."""
    folder = Path(folder_path).expanduser().resolve()

    if not folder.is_dir():
        logger.error("Error: '%s' is not a valid folder.", folder)
        return None

    moved = skipped = errors = 0
    logger.info("Organizing: %s", folder)

    try:
        with os.scandir(folder) as iterator:
            entries = sorted(iterator, key=lambda entry: entry.name.lower())
    except PermissionError:
        logger.error("Permission denied: cannot read '%s'.", folder)
        return None

    for entry in entries:
        source = Path(entry.path)

        # Skip subfolders, hidden files and this script itself.
        if (
            not entry.is_file(follow_symlinks=False)
            or entry.name.startswith(".")
            or source.resolve() == Path(__file__).resolve()
        ):
            skipped += 1
            continue

        category = get_category(entry.name)
        target_dir = folder / category

        try:
            target_dir.mkdir(exist_ok=True)
            target = unique_path(target_dir / entry.name)
            shutil.move(str(source), str(target))
            logger.info("Moved: %s -> %s/", entry.name, category)
            moved += 1
        except PermissionError:
            logger.error("Permission denied: %s", entry.name)
            errors += 1
        except FileExistsError:
            logger.error("Name conflict, could not move: %s", entry.name)
            errors += 1
        except OSError as error:
            logger.error("Could not move %s: %s", entry.name, error)
            errors += 1

    print("\n===== EXECUTION SUMMARY =====")
    print(f"Total files relocated : {moved}")
    print(f"Items skipped         : {skipped}")
    print(f"Errors                : {errors}")
    return moved, skipped, errors


def main():
    setup_logging()
    print("===== FILE ORGANIZER =====")
    print("Sorts the files in a folder into category subfolders.")
    print("Example:", Path.home() / "Downloads")

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
