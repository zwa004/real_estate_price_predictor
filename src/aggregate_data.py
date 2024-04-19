import pandas as pd
import regex as re
import os

# Load into a dataframe
def load_data(root_dir):
    
    data_frames = []

    # Loop through the years in data folder
    for year in range(2019, 2023):
        year_path = os.path.join(root_dir, 'data', str(year))

        # Loop through each file in the year folder
        for file in os.listdir(year_path):
            if file.endswith((".xls", ".xlsx")):
                file_path = os.path.join(year_path, file)
                data = pd.read_excel(file_path)

        # Add a column for zone to the dataframe based on the name of the file (ex 09_z_6.xls is zone 6) and remove the .xls extension
                match = re.match(r'^(\d{2})_z_(\d+).*', file)
                if match:
                    zone = int(match.group(2))
                    data['Zone'] = zone
                else:
                    print(f"Invalid file name format: {file}")

        # Append DataFrame to list
                data_frames.append(data)

    all_data = pd.concat(data_frames, ignore_index=True)
    return all_data

# Add df as csv file and save as csv to the folder
def main():
    root_dir = 'C:/Users/ZachAllgood/Personal Projects/real_estate_price_predictor'
    combined_data = load_data(root_dir)

    # Save the combined data to a CSV file
    combined_data.to_csv(os.path.join(root_dir, 'data', 'combined_data.csv'), index=False)

if __name__ == '__main__':
    main()