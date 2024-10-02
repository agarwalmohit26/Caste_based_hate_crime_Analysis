import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("crime_by_state_rt.csv")
print(df)

#1
#correlation betwwen crime types
correlation_matrix=df[['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']].corr()
print(correlation_matrix)

plt.figure(figsize=(6,6))
sns.heatmap(correlation_matrix,annot=True,cmap="magma",fmt=".2f",square=True,linewidth=0.5,linecolor="yellow",cbar_kws={"shrink":0.8})
plt.title("Correlation Heatmap of Crime Categories",fontsize=20,weight="bold",color="#2e2e2e")
plt.xticks(rotation=45,ha="right",fontsize=10)
plt.yticks(rotation=0,fontsize=10)
plt.show()

#2
#average crimes per state
average_crimes_per_state=df[['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']].mean().reset_index()
print(average_crimes_per_state)

#4 total distribution
distribution=df[['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']].sum()
print(distribution)
distribution.plot(kind="bar",figsize=(5,5))
plt.title("Tolat Distribution")
plt.ylabel("Crimes")
plt.show()

crime_columns=['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']
#Sum all crime columns for each yera
df['Total Crimes'] = df[crime_columns].sum(axis=1)
total_crimes_per_year = df.groupby('Year')['Total Crimes'].sum().reset_index()
print(total_crimes_per_year)

sns.set(style="whitegrid")
plt.figure(figsize=(10,6))

# Creating the line plot
sns.barplot(x='Year', y='Total Crimes', data=total_crimes_per_year, color='b')

# Adding titles and labels
plt.title('Total Crimes Per Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Crimes', fontsize=12)

# Display the plot
plt.show()

crime_columns=['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']
crimes_per_year=df.groupby("Year")[crime_columns].sum().reset_index()

print(crimes_per_year)

sns.set(style="whitegrid")
plt.figure(figsize=(12,8))

# Plotting each crime category over the years
for column in crime_columns:
    sns.lineplot(x='Year', y=column, data=crimes_per_year, label=column)
plt.title('Total Crimes Per Year by Category', fontsize=18, weight='bold', color='#3e3e3e')
plt.xlabel('Year', fontsize=14, color='#3e3e3e')
plt.ylabel('Number of Crimes', fontsize=14, color='#3e3e3e')
plt.xticks(ticks=range(2001,2013),fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Crime Type', fontsize=12, title_fontsize=13, loc='upper right')
plt.show()

sns.set(style="whitegrid")
plt.figure(figsize=(20,40))
palette = sns.color_palette("husl", len(crime_columns))  # Using 'husl' color palette for bright colors
# Plotting each crime category over the years with custom design elements
for i, column in enumerate(crime_columns):
    sns.lineplot(x='Year', y=column, data=crimes_per_year, label=column,
                 color=palette[i], marker='o', markersize=7, linewidth=2.5)
# Add shaded areas under the lines to highlight trends
for i, column in enumerate(crime_columns):
    plt.fill_between(crimes_per_year['Year'], crimes_per_year[column], color=palette[i], alpha=0.1)
# Customizing the plot further
plt.title('Total Crimes Per Year by Category', fontsize=20, weight='bold', color='#2e2e2e')
plt.xlabel('Year', fontsize=15, color='#2e2e2e')
plt.ylabel('Number of Crimes', fontsize=15, color='#2e2e2e')
plt.xticks(ticks=range(2001,2013),labels=range(2001,2013),fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Crime Type', fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))
max_year = crimes_per_year.iloc[crimes_per_year[crime_columns].sum(axis=1).idxmax()]['Year']
max_value = crimes_per_year[crime_columns].sum(axis=1).max()
plt.text(max_year, max_value, f"Highest Total Crime Year\n{max_year}", color='red', fontsize=12, weight='bold')
plt.tight_layout()
plt.show()

# Step 2: Create 'Total Crimes' column by summing up all crime-related columns
# For example, if the crime columns are 'Murder', 'Theft', 'Assault', replace them with actual names
crime_columns = ['Murder', 'Assault on women',
       'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt',
       'Prevention of atrocities (POA) Act',
       'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

# Step 3: Create the new 'Total Crimes' column
df['Total Crimes'] = df[crime_columns].sum(axis=1)
sns.set(style="whitegrid")
# Step 4: Visualize total crime count by state
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
ax=df.groupby('STATE/UT')['Total Crimes'].sum().sort_values(ascending=False).plot(kind='bar', color=sns.color_palette("mako",len(df["STATE/UT"].unique())))
plt.title('Total Crime Count by State')
plt.xlabel('STATE/UT')
plt.ylabel('Total Crimes')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 10),
                textcoords='offset points', fontsize=6, weight='bold', color='red')

plt.xticks(rotation=90,fontsize=10)
plt.grid(axis="y",linestyle="--",alpha=0.7)
sns.despine(left=True, bottom=True)
plt.show()

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




