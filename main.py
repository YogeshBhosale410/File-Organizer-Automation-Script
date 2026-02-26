import os          # Used to interact with operating system (files & folders)
import shutil      # Used to move, copy, and delete files

# Get the current working directory (where the script is running)
folder_path = os.getcwd()

# Dictionary that maps folder names to their file extensions
file_types = {
    "PDFs": [".pdf"],                         # All PDF files
    "Word_files": [".doc", ".docx"],          # Word documents
    "excel_file": [".xls", ".xlsx"],          # Excel files
    "image_file": [".jpg", ".jpeg", ".png"],  # Image files
    "audio_file": [".mp3"],                   # Audio files
    "video_file": [".mp4", ".mkv"],           # Video files
    "python_files": [".py"],                  # Python scripts
}

# Create folders if they do not already exist
for folder in file_types:
    if not os.path.exists(folder):   # Check if folder already exists
        os.makedirs(folder)          # Create folder if not exists

# Loop through all files and folders in current directory
for file in os.listdir(folder_path):

    # Skip if the item is a folder (we only want files)
    if os.path.isdir(file):
        continue

    # Extract file extension (e.g., .pdf, .jpg) and convert to lowercase
    ext = os.path.splitext(file)[1].lower()

    # Check which category the file belongs to
    for folder, extensions in file_types.items():

        # If file extension matches the category extension list
        if ext in extensions:

            # Move file into the respective folder
            shutil.move(file, os.path.join(folder, file))

            # Stop checking other folders once moved
            break
