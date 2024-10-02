import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('crime_by_district_rt.csv')
print(df)


print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df.head())
print(df.columns)

crimes_per_year = df.groupby('Year')[['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt']].sum().reset_index()
print(crimes_per_year)

# Total Crimes per Year
total_crimes_per_year = crimes_per_year[['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt']].sum(axis=1)

# Plot the total crimes per year
plt.figure(figsize=(10,6))
plt.plot(crimes_per_year['Year'], total_crimes_per_year, marker='o')
plt.title('Total Crimes per Year')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.grid(True)
plt.show()

# Plot each type of crime separately
plt.figure(figsize=(10,6))
plt.plot(crimes_per_year['Year'], crimes_per_year['Murder'], label='Murder', marker='o')
plt.plot(crimes_per_year['Year'], crimes_per_year['Assault on women'], label='Assault on women', marker='o')
plt.plot(crimes_per_year['Year'], crimes_per_year['Kidnapping and Abduction'], label='Kidnapping and Abduction', marker='o')

# Plot each type of crime separately
plt.figure(figsize=(10,6))
sns.lineplot(x='Year', y='Murder', data=crimes_per_year, label='Murder')
sns.lineplot(x='Year', y='Assault on women', data=crimes_per_year, label='Assault on women')
sns.lineplot(x='Year', y='Kidnapping and Abduction', data=crimes_per_year, label='Kidnapping and Abduction')
sns.lineplot(x='Year', y='Dacoity', data=crimes_per_year, label='Dacoity')
sns.lineplot(x='Year', y='Robbery', data=crimes_per_year, label='Robbery')
sns.lineplot(x='Year', y='Arson', data=crimes_per_year, label='Arson')
sns.lineplot(x='Year', y='Hurt', data=crimes_per_year, label='Hurt')
plt.title('Crimes per Year')
plt.xlabel('Year')
plt.ylabel('Crimes')
plt.grid(True)
plt.legend()
plt.show()

# Plot each type of crime separately
plt.figure(figsize=(10,6))
sns.barplot(x='Year', y='Murder', data=crimes_per_year, label='Murder')
sns.barplot(x='Year', y='Assault on women', data=crimes_per_year, label='Assault on women')
sns.barplot(x='Year', y='Kidnapping and Abduction', data=crimes_per_year, label='Kidnapping and Abduction')
sns.barplot(x='Year', y='Dacoity', data=crimes_per_year, label='Dacoity')
sns.barplot(x='Year', y='Robbery', data=crimes_per_year, label='Robbery')
sns.barplot(x='Year', y='Arson', data=crimes_per_year, label='Arson')
# sns.barplot(x='Year', y='Hurt', data=crimes_per_year, label='Hurt')
plt.title('Crimes per Year')
plt.xlabel('Year')
plt.ylabel('Crimes')
plt.grid(True)
plt.legend()
plt.show()

crimes_per_year = df.groupby('STATE/UT')[['Murder', 'Assault on women',
'Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt']].sum().reset_index()
print(crimes_per_year)

print(df['STATE/UT'].unique())
