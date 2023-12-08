
# README for My Media Organizing and Log Processing Scripts

## Overview

This README provides instructions on how to use the set of Python scripts designed for organizing media files (pictures and videos) and processing log files.

There are four main scripts:

1. **organize_pictures.py**: Organizes picture files into folders based on their creation dates.
2. **organize_videos.py**: Organizes video files into folders based on their creation dates.
3. **combine_log.py**: Combines all log files from a log directory into a single file, categorizing entries into 'move' and 'duplicate' sections.
4. **duplicated_files.py**: Processes log files to identify and handle duplicate files.

### Prerequisites

- Python 3.x installed.
- `exiftool` installed: This is used for extracting media file metadata. [Install exiftool](https://exiftool.org/install.html).
- Libraries: `subprocess`, `json`, `tqdm`, `datetime`, `os`, `shutil`. Most of these are standard in Python. You might need to install `tqdm` using `pip install tqdm`.

## Usage

### 1. Organizing Pictures

**Script:** `organize_pictures.py`

This script organizes pictures into folders named by their creation dates.

#### How to Run:

1. Edit the script to specify the source and destination directories at the end of the file.
   
   ```python
   organize_photos('/path/to/source/pictures', '/path/to/destination/folder')
   ```

2. Run the script:

   ```bash
   python organize_pictures.py
   ```

### 2. Organizing Videos

**Script:** `organize_videos.py`

Similar to `organize_pictures.py`, but for video files.

#### How to Run:

1. Edit the script to specify the source and destination directories.
   
   ```python
   organize_videos('/path/to/source/videos', '/path/to/destination/folder')
   ```

2. Run the script:

   ```bash
   python organize_videos.py
   ```

### 3. Combining Log Files

**Script:** `combine_log.py`

Combines all log entries into one file, with 'move' entries first, followed by 'duplicate' entries.

#### How to Run:

1. Edit the script to specify the log directory and the name of the output combined log file.

   ```python
   combine_log_files('/path/to/logs/directory', '/path/to/combined_log_file.txt')
   ```

2. Run the script:

   ```bash
   python combine_log.py
   ```

### 4. Processing Duplicate Files

**Script:** `duplicated_files.py`

Processes log files to identify and handle duplicate files.

#### How to Run:

1. Run the script (no modifications needed unless specific log processing is required).

   ```bash
   python duplicated_files.py
   ```

## Notes

- Always backup your media files before running these scripts to prevent accidental loss.
- Modify the paths in the scripts to match your directory structure.
- Ensure `exiftool` is installed and accessible from the command line.

For further assistance or customizations, refer to the comments within each script or contact the script maintainer.
