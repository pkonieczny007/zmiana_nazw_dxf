import os
import shutil
import pandas as pd

def rename_and_copy_files_to_new_directory(excel_filename):
    # Set the default folder path to the current directory of the script
    folder_path = os.getcwd()

    # Create 'new_name' folder if it doesn't exist
    new_name_folder = os.path.join(folder_path, 'new_name')
    if not os.path.exists(new_name_folder):
        os.makedirs(new_name_folder)

    # Set the path for the excel file in the current directory
    excel_path = os.path.join(folder_path, excel_filename)

    # Read the Excel file
    try:
        df = pd.read_excel(excel_path, usecols=['STARA_NAZWA', 'NOWA_NAZWA'])
    except Exception as e:
        return f"Error reading Excel file: {e}"

    # List for missing files
    missing_files = []

    # Iterate through the rows in the DataFrame
    for index, row in df.iterrows():
        old_name = row['STARA_NAZWA']
        new_name = row['NOWA_NAZWA']

        old_file_path = os.path.join(folder_path, f"{old_name}.dxf")
        new_file_path = os.path.join(new_name_folder, f"{new_name}.dxf")

        # Check if the old file exists
        if os.path.exists(old_file_path):
            # Copy the old file to the new directory
            shutil.copy2(old_file_path, new_file_path)
        else:
            missing_files.append(old_name)

    return missing_files

# Example usage with default paths
excel_filename = 'zmiana.xlsx'
missing_files = rename_and_copy_files_to_new_directory(excel_filename)

if missing_files:
    print("Nie znaleziono następujących plików:", missing_files)
else:
    print("Wszystkie pliki zostały pomyślnie przetworzone.")
