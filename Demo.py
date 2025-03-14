import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "C:\\Users\\55231\\OneDrive - ICF\\Desktop\\GenAI\\Input_Data_for_Copilot.csv"
data = pd.read_csv(file_path)

# Count the number of variables
num_variables = len(data.columns)

# List the names of the variables
variable_names = data.columns.tolist()

# Calculate the frequencies of unique values in the variable "Race"
race_frequencies = data['Race'].value_counts()

# Plot a histogram of frequencies of unique values in the variable "Race"
plt.figure(figsize=(10, 6))
race_frequencies.plot(kind='hist', bins=len(race_frequencies), color='skyblue', edgecolor='black')
plt.title('Histogram of Frequencies of Unique Values in Race')
plt.xlabel('Frequency')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot a barchart of frequencies of unique values in the variable "Education" using different colors for each bar
education_frequencies = data['Education'].value_counts()
plt.figure(figsize=(10, 6))
education_frequencies.plot(kind='bar', color=plt.cm.tab20.colors)
plt.title('Barchart of Frequencies of Unique Values in Education')
plt.xlabel('Education')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot a pie chart of frequencies of unique values in the variable "Collection Year"
collection_year_frequencies = data['Collection Year'].value_counts()
plt.figure(figsize=(8, 8))
collection_year_frequencies.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Pie Chart of Frequencies of Unique Values in Collection Year')
plt.ylabel('')
plt.show()

# Print the results
print(f"Number of variables: {num_variables}")
print(f"Names of variables: {variable_names}")
print(f"Frequencies of unique values in Race:\n{race_frequencies}")