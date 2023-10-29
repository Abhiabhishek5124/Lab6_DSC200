import pandas as pd
from dateutil import parser

# Function to merge CSV files
def merge_csv_files(file1, file2, file3, output_file):
    # Read the first dataset and parse the "Crash Date/Time" column as datetime
    df1 = pd.read_csv(file1, dtype={"Local Case Number": str})
    df1["Crash Date/Time"] = df1["Crash Date/Time"].apply(parser.parse)
    df1 = df1[["Crash Date/Time", "Latitude", "Longitude"]]
    df1.rename(columns={"Crash Date/Time": "dateTime"}, inplace=True)

    # Read the second dataset and parse "CRASH DATE" and "CRASH TIME" columns as datetime
    df2 = pd.read_csv(file2, dtype={"ZIP CODE": str}, parse_dates={"dateTime": ["CRASH DATE", "CRASH TIME"]})
    df2 = df2[["dateTime", "LATITUDE", "LONGITUDE"]]
    df2.rename (columns={"LATITUDE": "Latitude", "LONGITUDE": "Longitude"}, inplace=True)

    # Read the third dataset and parse "CRASH_DATE" as datetime
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


# Function to clean data

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Print the number of features and observations before cleaning
    print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))

    # Remove extra columns
    print("Removing extra columns")
    df.drop(columns=["educ_num", "education_1", "occupation_1", "workclass_1"], inplace=True)

    # Print the number of features and observations after column removal
    print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))

    # Remove missing values
    print("Removing missing values")
    df.replace(" ?", None, inplace=True)
    df = df.dropna()

    # Print the number of features and observations after removing missing values
    print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))

    # Remove duplicate rows
    print("Removing duplicate rows")
    df = df.drop_duplicates()

    # Print the number of features and observations after removing duplicates
    print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))

    # Save the cleaned DataFrame to the output CSV file
    df.to_csv(output_file, index=False)
    print("Clean data outputted to csv")

# Main function for user interaction
def main():
    while True:
        print("Select an option:")
        print("1. Merge Datasets")
        print("2. Clean Data")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Specify the file names and the output file name for merging datasets
            file1 = "Crash_Reporting_-_Drivers_Data.csv"
            file2 = "Motor_Vehicle_Collisions_-_Crashes.csv"
            file3 = "Traffic_Crashes_-_Crashes.csv"
            output_file = "merged_data.csv"
            merge_csv_files(file1, file2, file3, output_file)
        elif choice == "2":
            # Specify the input file and output file for data cleaning
            input_file = "Lab6Data.csv"
            output_file = "Lab6OutputData.csv"
            clean_data(input_file, output_file)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()