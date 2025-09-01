import pandas as pd

# Read the Excel file
df = pd.read_excel('resultmac.xlsx')

# Print the column names for debugging
print("Column names in the DataFrame:")
print(df.columns)

# Strip any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Create a list to hold new rows
new_rows = []

# Iterate over the unique 'Name / Father's Name' values
for name in df['Name / Father\'s Name'].unique():
    # Filter the DataFrame for the current name
    name_df = df[df['Name / Father\'s Name'] == name]
    
    # Create a new row for the new DataFrame
    new_row = {'Student Name': name}
    
    # Iterate through each subject and get the Obt. values
    for index, row in name_df.iterrows():
        subject = row['Subject Name']
        obtained = row['Pre Board Exam']
        new_row[subject] = obtained*2
    
    # Append the new row to the list
    new_rows.append(new_row)

# Create a new DataFrame from the list of new rows
new_df = pd.DataFrame(new_rows)

# Write the new DataFrame to an Excel file
new_df.to_excel('output.xlsx', index=False)

print("Data transformation complete. Output saved to 'output.xlsx'.")