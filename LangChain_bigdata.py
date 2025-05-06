from langchain_core.tools import tool
import pandas as pd
import matplotlib.pyplot as plt

@tool
def bigdata(file_path, cat, var):
   """Analyze csv files."""
   data=pd.read_csv(file_path)

   # Count the number of variables (columns) in the csv file
   num_variables = len(data.columns)
   name_variables = data.columns.tolist()
   cat_sums = data.groupby(cat)[var].sum()
   total_value = data[var].sum()
   cat_percentages = (cat_sums / total_value) * 100
   
   # plot a bar chart for the percentages
   cat_percentages.plot(kind='bar', figsize=(10, 6))
   plt.ylabel('Percentage (%)')
   plt.title('Percentage of Each Category')
   plt.xlabel('Category')
   plt.tight_layout()
   plt.show()

   # Plot the pie chart
   plt.figure(figsize=(8, 8))
   plt.pie(cat_percentages, labels=cat_percentages.index, autopct='%1.1f%%', startangle=140)
   plt.title(f'Distribution of {cat}')
   plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
   plt.show()
   
   return (
        f"The number of variables in the file is {num_variables}.\n"
        f"The names of the variables are: {name_variables}.\n"
        f"The total sum of the 'Value' column is {total_value}.\n"
        f"The percentage for each category is:\n{cat_percentages}."
    )

# Use the tool
result = bigdata.invoke({
    "file_path": "xxx.csv",
    "cat": "cat_xxx",
    "var": "var_xxx"
})

print(result)