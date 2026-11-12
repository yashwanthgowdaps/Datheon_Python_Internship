# Task 3: Automated File Organizer & Cleanup Utility

A utility that sorts the files in a folder (for example Downloads) into category subfolders based on their extensions.

## Features

- Inspects every file's extension and creates category subfolders automatically
- Moves files safely with `shutil.move`
- **Avoids name collisions**: `report.pdf` becomes `report_1.pdf` instead of overwriting
- Handles `PermissionError`, `FileExistsError` and other OS errors without crashing
- Skips subfolders, hidden files and the script itself
- Logs every action to the screen and to `organizer.log`
- Prints an execution summary: files relocated, items skipped and errors

## Categories

| Folder | Extensions |
|--------|-----------|
| Documents | .pdf .txt .doc .docx .odt .rtf |
| Images | .jpg .jpeg .png .gif .bmp .webp .svg |
| Videos | .mp4 .mkv .avi .mov .wmv |
| Audio | .mp3 .wav .aac .ogg .flac |
| Archives | .zip .rar .7z .tar .gz |
| Code | .py .java .c .cpp .html .css .js |
| Spreadsheets | .csv .xls .xlsx |
| Presentations | .ppt .pptx |
| Others | anything else |

To change the mapping, edit `EXTENSION_MAP` in `organizer.py`.

## How to Run

```
python Task-3-File-Automation/organizer.py
```

Enter the folder path when asked, for example `~/Downloads` or `/storage/emulated/0/Download/test_files`.

> **Warning:** This program moves files. Try it on a small test folder first.

## Sample Output

```
Organizing: /home/user/test_files
Moved: notes.txt -> Documents/
Moved: photo.jpg -> Images/
Moved: song.mp3 -> Audio/

===== EXECUTION SUMMARY =====
Total files relocated : 3
Items skipped         : 0
Errors                : 0
```

## Python Concepts Used

`os.scandir`, `shutil`, `pathlib`, dictionaries, the `logging` module, exception handling, string and path operations.
