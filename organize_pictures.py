import os
import shutil
import subprocess
import json
from tqdm import tqdm
from datetime import datetime

def get_date_taken_exiftool(path):
    try:
        result = subprocess.run(['exiftool', '-DateTimeOriginal', '-j', '-n', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr:
            return None
        data = json.loads(result.stdout)
        
        # Check if 'DateTimeOriginal' is in the data and is not an empty string
        if 'DateTimeOriginal' in data[0] and data[0]['DateTimeOriginal'].strip():
            return data[0]['DateTimeOriginal']
        else:
            return None
    except Exception as e:
        return None


def get_unique_filename(dest_folder, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}_copy{counter}{extension}"
        counter += 1
    return new_filename

def organize_photos(src_folder, dest_folder_base):
    # Create a log directory inside the destination folder
    log_dir = os.path.join(dest_folder_base, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    unregistered_dir = os.path.join(dest_folder_base, 'unregistered')
    os.makedirs(unregistered_dir, exist_ok=True)

    # Generate log file name with current date and time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"log_{current_time}.txt"
    log_file_path = os.path.join(log_dir, log_file_name)

    duplicate_log = []  # List to store duplicate file information

    with open(log_file_path, 'w') as log_file:
        all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(src_folder) for f in filenames if not f.startswith('.') and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.arw', '.raf', '.psd', '.psb', '.dng'))]
        for src_path in tqdm(all_files, desc="Processing Images"):
            file_extension = os.path.splitext(src_path)[1].lower()
            if file_extension in ['.psd', '.psb']:
                psd_psb_folder = os.path.join(dest_folder_base, 'Photoshop_Files')
                os.makedirs(psd_psb_folder, exist_ok=True)
                new_path = os.path.join(psd_psb_folder, os.path.basename(src_path))
                shutil.move(src_path, new_path)
                log_file.write(f"{os.path.basename(src_path)}: {src_path} -> {new_path}\n")
            else:
                date_taken = get_date_taken_exiftool(src_path)
                if date_taken:
                    date_folder = date_taken.split()[0].replace(':', '-')  # Converts 'YYYY:MM:DD HH:MM:SS' to 'YYYY-MM-DD'
                    dest_folder = os.path.join(dest_folder_base, date_folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    unique_file_name = get_unique_filename(dest_folder, os.path.basename(src_path))
                    new_path = os.path.join(dest_folder, unique_file_name)
                    shutil.move(src_path, new_path)
                    log_file.write(f"{os.path.basename(src_path)}: {src_path} -> {new_path}\n")
                    if unique_file_name != os.path.basename(src_path):
                        duplicate_log.append(f"{os.path.basename(src_path)}: {src_path} -> {new_path} (Duplicate)")
                else:
                    new_path = os.path.join(unregistered_dir, os.path.basename(src_path))
                    shutil.move(src_path, new_path)
                    log_file.write(f"{os.path.basename(src_path)}: {src_path} -> {new_path} (Unregistered)\n")
                    continue
                    

        # Write duplicate file information
        if duplicate_log:
            log_file.write("\n--- Duplicate Files ---\n")
            log_file.writelines("%s\n" % line for line in duplicate_log)

# Replace 'src_directory_path', 'dest_directory_path', and 'log_file_path' with the appropriate paths
organize_photos('/Volumes/PortableSSD/photo_archive/archive_01', '/Volumes/home/Medias_backup/photo_organized')