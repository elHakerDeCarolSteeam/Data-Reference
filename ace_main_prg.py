import pandas as pd

# Read the main Excel file
main_excel_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\MyPrograms\Accounts\Ace Hardware\2024\Q2 Ace Account Maintenance\Ace_ALL_MASTER.xlsx"
df_main = pd.read_excel(main_excel_file)

# Read the reference Excel files
reference_file1 = r"C:\Users\BryanChacha\OneDrive - Saleslink\MyPrograms\Accounts\Ace Hardware\2024\Q2 Ace Account Maintenance\Ace_ALL_Accts_SF.xlsx"
df_reference1 = pd.read_excel(reference_file1)

# Perform VLOOKUP to merge the first reference DataFrame based on 'Article'
merged_df = pd.merge(df_main, df_reference1[['Unique External ID (Account)', 'Account ID']], 
                      how='left', left_on='Unique External ID', right_on='Unique External ID (Account)')

# Save the merged DataFrame to a new Excel file
output_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\MyPrograms\Accounts\Ace Hardware\2024\Q2 Ace Account Maintenance\OUTPUT_v01.xlsx"
merged_df.to_excel(output_file, index=False)

print("VLOOKUP completed and merged DataFrame saved to", output_file)