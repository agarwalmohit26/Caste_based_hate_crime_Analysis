import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('C:/Users/krush/OneDrive/Desktop/project_1 masai/crime_by_state_rt.csv')
print(df)
print(df.head())
print(df.info())
print(df.describe())

# Group data by state and sum up crime counts
state_wise_data = df.groupby('STATE/UT').sum()

# Plotting state-wise comparison for selected crime categories
crime_categories = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

plt.figure(figsize=(32, 24))  # Adjusted figure size
for i, crime in enumerate(crime_categories, 1):
    plt.subplot(5, 2, i)
    state_wise_data[crime].sort_values(ascending=False).plot(kind='bar')
    plt.title(f'State-wise {crime} Comparison')
    plt.xticks(rotation=90)

# Use subplots_adjust instead of tight_layout
plt.subplots_adjust(hspace=1.4, wspace=0.4)  # Adjust spacing between subplots
plt.show()

plt.figure(figsize=(10, 8))
crime_types = df.columns[2:]  # Adjust this based on your dataset's columns
df[crime_types].sum().plot(kind='bar', color='purple')
plt.title('Crime Type Distribution in States')
plt.xlabel('Crime Type')
plt.ylabel('Total Count')
plt.xticks(rotation=90)
plt.show()

# Step 1: Check the column names to find crime-related columns
print(df.columns)

# Step 2: Create 'Total Crimes' column by summing up all crime-related columns
# For example, if the crime columns are 'Murder', 'Theft', 'Assault', replace them with actual names
crime_columns = ['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']  # Replace with actual column names for crimes

# Step 3: Create the new 'Total Crimes' column
df['Total Crimes'] = df[crime_columns].sum(axis=1)

# Step 4: Visualize total crime count by state
plt.figure(figsize=(10, 6))
df.groupby('STATE/UT')['Total Crimes'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Total Crime Count by State')
plt.xlabel('STATE/UT')
plt.ylabel('Total Crimes')
plt.xticks(rotation=90)
plt.show()