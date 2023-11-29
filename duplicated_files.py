import os

def print_duplicate_files(logs_dir):
    # Check if the logs directory exists
    if not os.path.isdir(logs_dir):
        print("The logs directory does not exist.")
        return

    # Get all log files in the directory
    log_files = [f for f in os.listdir(logs_dir) if f.startswith('log_') and f.endswith('.txt')]

    print("Duplicate Files:")
    for log_file in log_files:
        # Construct full file path
        file_path = os.path.join(logs_dir, log_file)
        # Read and process each log file
        with open(file_path, 'r') as file:
            for line in file:
                # Check if the line contains duplicate information
                if "Duplicate" in line:
                    print(line.strip())


def move_duplicates_to_trash(logs_dir, trash_dir):
    # Check if the logs directory exists
    if not os.path.isdir(logs_dir):
        print("The logs directory does not exist.")
        return
    
    # Create a trash directory if it doesn't exist
    if not os.path.isdir(trash_dir):
        os.makedirs(trash_dir)
    
    # List to store the paths of duplicate files
    duplicates = []

    # Get all log files in the directory
    log_files = [f for f in os.listdir(logs_dir) if f.startswith('combined_') and f.endswith('.txt')]
    
    for log_file in log_files:
        # Construct full file path for the log file
        file_path = os.path.join(logs_dir, log_file)
        # Read each log file and collect duplicates
        with open(file_path, 'r') as file:
            for line in file:
                if "Duplicate" in line and not line.startswith("--- Duplicate Files ---"):
                    # Extract the duplicate file path from the log entry
                    duplicate_path = line.split(" -> ")[1].strip().split(" (Duplicate)")[0]
                    duplicates.append(duplicate_path)
    
    # Move duplicates to the trash folder after user confirmation
    for duplicate in duplicates:
        # Ask user for confirmation before moving
        #confirm = input(f"Move duplicate file {duplicate} to trash? (y/n): ")
        if True:
            try:
                # Construct the new path in the trash directory
                trash_path = os.path.join(trash_dir, os.path.basename(duplicate))
                # Move the file to the trash directory
                os.rename(duplicate, trash_path)
                print(f"Moved to trash: {trash_path}")
            except FileNotFoundError:
                print(f"File not found: {duplicate}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Skipped: {duplicate}")


# Replace 'path_to_logs_directory' with the actual path to your logs directory
# Specify the path to the trash directory
logs_dir = '/Volumes/home/Medias_backup/photo_organized/logs'
trash_dir = os.path.join(logs_dir, 'trash')

move_duplicates_to_trash(logs_dir, trash_dir)

#print_duplicate_files('/Volumes/Samsung_T5/backup_organized/logs')
