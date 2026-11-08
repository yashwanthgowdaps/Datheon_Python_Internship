Task 3: File Organizer

Datheon Python Programming Internship

About the Project

The File Organizer is a Python program that automatically organizes files in a selected folder into separate folders based on their file types. It helps keep files organized and makes them easier to find.

Features

- Organizes files based on their extensions.
- Automatically creates category folders.
- Supports PDFs, images, audio, videos, documents, spreadsheets, presentations, archives, and other file types.
- Avoids overwriting existing files with the same name by generating a unique filename.
- Handles errors during file operations.
- Displays a summary of moved files, skipped files, and errors.
- Allows the user to enter a folder path.

Technologies Used

- Python 3
- "os" module
- "shutil" module

Python Concepts Used

- Variables and data types
- Lists and dictionaries
- Functions
- Loops and conditional statements
- String operations
- File and folder handling
- Exception handling
- User input and validation

Folder Categories

Folder| File types
"PDF_Files"| PDF files
"Images"| JPG, JPEG, PNG, GIF, WEBP
"Audio_Files"| MP3, WAV, AAC, OGG
"Video_Files"| MP4, MKV, AVI, MOV
"Documents"| TXT, DOC, DOCX, RTF
"Spreadsheets"| XLS, XLSX, CSV
"Presentations"| PPT, PPTX
"Archives"| ZIP, RAR, 7Z, TAR
"Code_Files"| Python and other supported code files
"Other_Files"| File types not covered by the categories above

The exact extensions supported depend on the categories defined in "file_organizer.py".

How to Run

Requirements

- Python 3 installed
- Pydroid 3 on Android, or Python installed on a computer

Steps

1. Open "file_organizer.py" in Pydroid 3.
2. Run the program.
3. Enter the path of the folder you want to organize.
4. Wait for the program to finish.
5. Check the generated category folders and the organization summary.

Example Folder Path

For Android:

"/storage/emulated/0/Download/test_files"

Important: Test the program on a small sample folder first. The program moves files from their original locations, so use a backup when testing.

Sample Output

===== FILE ORGANIZER =====
This program sorts files into folders by type.

Enter folder path to organize: /storage/emulated/0/Download/test_files

Starting file organization...
Moved: example.pdf -> PDF_Files/
Moved: photo.jpg -> Images/
Moved: song.mp3 -> Audio_Files/

===== ORGANIZATION SUMMARY =====
Files moved: 3
Files skipped: 0
Errors: 0
Organization finished.

This is an illustrative example; actual results depend on the files in the selected folder.

AI Assistance

AI tools were used as a learning aid during development. The program was tested, and the code was reviewed to understand how file organization and Python file-handling operations work.

Conclusion

This project demonstrates how Python can automate file organization using file extensions, directory creation, file movement, and error handling.
