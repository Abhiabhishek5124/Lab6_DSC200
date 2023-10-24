import pandas as pd

def merge_csv_files(file1, file2, file3, output_file):
    # Read the three CSV files into DataFrames, specifying data types for problematic columns
    dtype_dict = {
        'Column1': str,  # Replace 'Column1' with the actual column name causing the warning in file1
        'Column3': str,  # Replace 'Column3' with the actual column name causing the warning in file2
    }
    df1 = pd.read_csv(file1, dtype=dtype_dict)
    df2 = pd.read_csv(file2, dtype=dtype_dict)
    df3 = pd.read_csv(file3)

    # Merge the DataFrames using the `concat` function
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)

    # Save the merged DataFrame to the output CSV file
    merged_df.to_csv(output_file, index=False)

# Specify the file names and the output file name
file1 = "Crash_Reporting_-_Drivers_Data.csv"
file2 = "Motor_Vehicle_Collisions_-_Crashes.csv"
file3 = "Traffic_Crashes_-_Crashes.csv"
output_file = "merged_data.csv"

# Call the function to merge the datasets
merge_csv_files(file1, file2, file3, output_file)
