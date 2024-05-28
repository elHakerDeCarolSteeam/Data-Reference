# ReadMe

## Overview

This Python script reads data from two Excel files, performs a VLOOKUP-like operation to merge the data based on a common identifier, and saves the merged data to a new Excel file. It uses the `pandas` library for data manipulation and merging.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. Make sure Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/).

2. Install the `pandas` library if you haven't already. You can install it using pip:

   ```bash
   pip install pandas
   ```

## Script Details

### Purpose

The script performs the following operations:

1. Reads data from a main Excel file (`ALL_MASTER.xlsx`).
2. Reads data from a reference Excel file (`REFERENCE_FILE.xlsx`).
3. Merges the data from the reference file into the main file based on a common identifier (`Unique External ID`).
4. Saves the merged data to a new Excel file (`OUTPUT_v01.xlsx`).

### File Paths

- **Main Excel file**: The path to the main Excel file is specified in the `main_excel_file` variable.
- **Reference Excel file**: The path to the reference Excel file is specified in the `reference_file1` variable.
- **Output file**: The path where the merged data will be saved is specified in the `output_file` variable.

### Code Explanation

```python
import pandas as pd

# Read the main Excel file
main_excel_file = r"example\path\ALL_MASTER.xlsx"
df_main = pd.read_excel(main_excel_file)

# Read the reference Excel file
reference_file1 = r"example\path\REFERENCE_FILE.xlsx"
df_reference1 = pd.read_excel(reference_file1)

# Perform VLOOKUP to merge the first reference DataFrame based on 'Article'
# Identifier -> Unique External ID (Account) FROM REFERENCE
# Transferring Over Column -> Account ID
# Array matching the MASTER -> Unique External ID
merged_df = pd.merge(df_main, df_reference1[['Unique External ID (Account)', 'Account ID']], 
                      how='left', left_on='Unique External ID', right_on='Unique External ID (Account)')

# Save the merged DataFrame to a new Excel file
output_file = r"example\path\OUTPUT_v01.xlsx"
merged_df.to_excel(output_file, index=False)

print("VLOOKUP completed and merged DataFrame saved to", output_file)
```

### Steps

1. **Read the main Excel file**: The script reads the main data file into a DataFrame (`df_main`).

2. **Read the reference Excel file**: The script reads the reference data file into another DataFrame (`df_reference1`).

3. **Merge the DataFrames**: Using the `pd.merge` function, the script performs a left join on `df_main` and `df_reference1` based on the `Unique External ID` from the main file and `Unique External ID (Account)` from the reference file. The resulting merged DataFrame (`merged_df`) includes the `Account ID` from the reference file.

4. **Save the merged DataFrame**: The merged DataFrame is saved to a new Excel file specified by `output_file`.

5. **Output message**: A confirmation message is printed to the console indicating that the operation is complete and the merged file has been saved.

## Usage

1. Update the file paths in the script to point to your actual Excel files.
2. Run the script using Python:

   ```bash
   python script_name.py
   ```

3. Check the specified output path for the new Excel file containing the merged data.

## Notes

- Ensure that the column names in the Excel files match those used in the script (`Unique External ID`, `Unique External ID (Account)`, and `Account ID`).
- Adjust the file paths as needed to match your directory structure.

## Troubleshooting

- If you encounter any errors related to file paths, make sure the paths are correctly specified and that the files exist at those locations.
- Ensure that the column names in your Excel files match the column names used in the script.
- If you encounter issues with the `pandas` library, ensure it is properly installed and up-to-date.

## License

This script is provided as-is without any warranty. Use it at your own risk.
