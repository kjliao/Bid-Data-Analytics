'''
This script reads data on the website, performs statistical analysis, and plot figures. 
Below are input examples (via Q&A) for running the script: 
# url: https://www2.census.gov/programs-surveys/popest/datasets/2020-2023/state/asrh/sc-est2023-alldata6.csv
# var: POPESTIMATE2023
# cat: RACE
'''

from langchain_core.tools import tool
import pandas as pd
import matplotlib.pyplot as plt

from langchain.tools import Tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@tool
def bigdata(url, cat, var):
    """
    Fetch data from a website URL and analyze it.
    Args:
        url (str): The URL of the website to fetch data from
        cat (str): Category column name
        var (str): Variable column name to analyze      
    Returns:
        str: Analysis results
    """
    data = pd.read_csv(url)
    num_variables = len(data.columns)
    name_variables = data.columns.tolist()
    cat_sums = data.groupby(cat)[var].sum()
    total_value = data[var].sum()
    cat_percentages = (cat_sums / total_value) * 100
            
    # plot a bar chart for the percentages
    plt.figure(figsize=(10, 6))
    cat_percentages.plot(kind='bar')
    plt.ylabel('Percentage (%)')
    plt.title('Percentage of Each Category')
    plt.xlabel('Category')
    plt.tight_layout()
    plt.show()

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(cat_percentages, labels=cat_percentages.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of {cat}')
    plt.axis('equal')
    plt.show()
       
    return (
        f"The number of variables in the file is {num_variables}.\n"
        f"The names of the variables are: {name_variables}.\n"
        f"The total sum of the '{var}' column is {total_value}.\n"
        f"The percentage for each category is:\n{cat_percentages}."
        )

# use the tool
url = input("Website: ")
var = input("Variable: ")
cat = input("Category: ")

result = bigdata.invoke({
        "url": url,   
        "cat": cat,
        "var": var
    })
print(result)
