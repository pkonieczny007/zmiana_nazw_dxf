import os
import shutil
import pandas as pd

def rename_and_backup_dxf_files_default_path(excel_filename):
    # Set the default folder path to the current directory of the script
    folder_path = os.getcwd()

    # Set the path for the excel file in the current directory
    excel_path = os.path.join(folder_path, excel_filename)

    # Read the Excel file
    try:
        df = pd.read_excel(excel_path, usecols=['STARA_NAZWA', 'NOWA_NAZWA'])
    except Exception as e:
        return f"Error reading Excel file: {e}"

    # Create 'original' folder if it doesn't exist
    original_folder = os.path.join(folder_path, 'original')
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    # List for missing files
    missing_files = []

    # Iterate through the rows in the DataFrame
    for index, row in df.iterrows():
        old_name = row['STARA_NAZWA']
        new_name = row['NOWA_NAZWA']

        old_file_path = os.path.join(folder_path, f"{old_name}.dxf")
        new_file_path = os.path.join(folder_path, f"{new_name}.dxf")
        backup_file_path = os.path.join(original_folder, f"{old_name}.dxf")

        # Check if the old file exists
        if os.path.exists(old_file_path):
            # Backup the old file
            shutil.copy2(old_file_path, backup_file_path)
            # Rename the old file to new name
            os.rename(old_file_path, new_file_path)
        else:
            missing_files.append(old_name)

    return missing_files

# Example usage with default paths
excel_filename = 'zmiana.xlsx'
missing_files = rename_and_backup_dxf_files_default_path(excel_filename)

if missing_files:
    print("Nie znaleziono następujących plików:", missing_files)
else:
    print("Wszystkie pliki zostały pomyślnie przetworzone.")
