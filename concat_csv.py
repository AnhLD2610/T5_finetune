import pandas as pd

# # Define file paths for the three CSV files
# body_file = "D:/LAB/SoTitle/data/C#/test_body.csv"
# code_file = "D:/LAB/SoTitle/data/C#/test_code.csv"
# title_file = "D:/LAB/SoTitle/data/C#/test_title.csv"

# # Read the CSV files into DataFrames
# df_body = pd.read_csv(body_file)
# df_code = pd.read_csv(code_file)
# df_title = pd.read_csv(title_file)

# # Merge the DataFrames into a single DataFrame
# merged_df = pd.concat([df_body, df_code, df_title], axis=1)

# # Save the merged DataFrame to a new CSV file
# output_file = "test1.csv"
# merged_df.to_csv(output_file, index=False)





import pandas as pd

# Define file paths for the three CSV files
body_file = "D:/LAB/SoTitle/data/C#/test_body.csv"
code_file = "D:/LAB/SoTitle/data/C#/test_code.csv"
title_file = "D:/LAB/SoTitle/data/C#/test_title.csv"

df_body = pd.read_csv(body_file)
df_code = pd.read_csv(code_file)
df_title = pd.read_csv(title_file)

merged_df = pd.concat([df_body, df_code, df_title], axis=1, keys=['body', 'code', 'title'])

output_file = "test1.csv"
merged_df.to_csv(output_file, index=False)