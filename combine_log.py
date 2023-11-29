import os
from datetime import datetime

def combine_log_files(logs_dir, output_log_file):
    # Check if the logs directory exists
    if not os.path.isdir(logs_dir):
        print(f"The directory {logs_dir} does not exist.")
        return

    # Lists to store different types of log entries
    move_entries = []
    duplicate_entries = []

    # Get all log files in the directory
    log_files = [f for f in os.listdir(logs_dir) if f.startswith('log_') and f.endswith('.txt') and not f.startswith(combined_log_prefix)]

    # Read each log file and categorize entries
    for log_file in log_files:
        file_path = os.path.join(logs_dir, log_file)
        with open(file_path, 'r') as infile:
            for line in infile:
                if "Duplicate" in line and not line.startswith("--- Duplicate Files ---"):
                    duplicate_path = line.split(" -> ")[1].strip().split(" (Duplicate)")[0]
                    if os.path.exists(duplicate_path):  # Check if the duplicate file still exists
                        duplicate_entries.append(line)
                elif not line.startswith("--- Duplicate Files ---"):
                    if line.strip() == "":
                        continue
                    move_entries.append(line)

    # Write categorized entries to the combined log file
    with open(output_log_file, 'w') as outfile:
        outfile.writelines(move_entries)
        outfile.write("\n--- Duplicate Files ---\n")
        outfile.writelines(duplicate_entries)

# Specify the log directory and the output file name
combined_log_prefix = 'combined_log'
logs_dir = '/Volumes/home/Medias_backup/photo_organized/logs'
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_log_file = os.path.join(logs_dir, f"combined_log_{current_time}.txt")

# Call the function to combine log files
combine_log_files(logs_dir, output_log_file)

