import os
import pandas as pd

def list_files(path):
    data = []
    
    for parent_folder in os.listdir(path):
        parent_folder_path = os.path.join(path, parent_folder)
        
        if os.path.isdir(parent_folder_path):
            for sub_folder in os.listdir(parent_folder_path):
                sub_folder_path = os.path.join(parent_folder_path, sub_folder)
                
                if os.path.isdir(sub_folder_path):
                    for root, _, files in os.walk(sub_folder_path):
                        sub_sub_folder = os.path.relpath(root, start=sub_folder_path)
                        for file in files:
                            if sub_sub_folder:
                                data.append([parent_folder,  "/" + sub_folder,  "/" + sub_sub_folder,  "/" + file])
                            else:
                                data.append([parent_folder,  "/" + sub_folder,  "/" + file])
    
    return data

if __name__ == "__main__":
    folder_path = r"D:\y2-sum-intern\model-picture\rearrangeed-folder"
    file_data = list_files(folder_path)

    df = pd.DataFrame(file_data, columns=["Parent Folder", "Sub-folder", "Sub-sub-folder", "File Name"])
    
    excel_path = r"D:\y2-sum-intern\model-picture\Filepath.xlsx"
    df.to_excel(excel_path, index=False, header=False)  # Set header to False to not include the title row
    
    print(f"Data exported to {excel_path}")
    
    # Read the Excel file again and print only the necessary columns based on conditions
    df_read = pd.read_excel(excel_path, header=None)  # Read Excel file without header
    
    if df_read.shape[1] == 3:  # Only Parent Folder, Sub-folder, File Name
        print(df_read)
    elif df_read.shape[1] == 4:  # Parent Folder, Sub-folder, Sub-sub-folder, File Name
        print(df_read)
    else:
        print("Unknown format in Excel.")