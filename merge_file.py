import pandas as pd
from dateutil import parser

def merge_csv_files(file1, file2, file3, output_file):
    df1 = pd.read_csv(file1, dtype={"Local Case Number": str})
    df1["Crash Date/Time"] = df1["Crash Date/Time"].apply(parser.parse)
    df1 = df1[["Crash Date/Time", "Latitude", "Longitude"]]
    df1.rename(columns={"Crash Date/Time": "dateTime"}, inplace=True)
    df2 = pd.read_csv(file2, dtype={"ZIP CODE": str}, parse_dates={"dateTime": ["CRASH DATE", "CRASH TIME"]})
    df2 = df2[["dateTime", "LATITUDE", "LONGITUDE"]]
    df2.rename(columns={"LATITUDE": "Latitude", "LONGITUDE": "Longitude"}, inplace=True)
    df3 = pd.read_csv(file3, parse_dates=["CRASH_DATE"])
    df3 = df3[["CRASH_DATE", "LATITUDE", "LONGITUDE"]]
    df3.rename(columns={"CRASH_DATE": "dateTime", "LATITUDE": "Latitude", "LONGITUDE": "Longitude"}, inplace=True)
    # Merge the DataFrames using the `concat` function
    merged_df = pd.concat([df1, df2, df3])
    merged_df.dropna(inplace=True)
    merged_df.drop_duplicates(inplace=True)
    merged_df.reset_index(drop=True, inplace=True)
    print(merged_df.size)
    # Save the merged DataFrame to the output CSV file
    merged_df.to_csv(output_file)


# Specify the file names and the output file name
file1 = "Crash_Reporting_-_Drivers_Data.csv"
file2 = "Motor_Vehicle_Collisions_-_Crashes.csv"
file3 = "Traffic_Crashes_-_Crashes.csv"
output_file = "merged_data.csv"

# Call the function to merge the datasets
merge_csv_files(file1, file2, file3, output_file)
