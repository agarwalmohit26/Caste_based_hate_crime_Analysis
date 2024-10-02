import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

"""
Abbrivations:
cbs = crime by state
cbd = crime by district 
"""

cbd = pd.read_csv("crime_by_district_rt.csv")
print(cbd)

print(cbd.columns.to_list())

"""
**The Prevention of Atrocities (POA) Act**, also known as the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989, was enacted to prevent `atrocities` against members of `Scheduled Castes (SCs)` and `Scheduled Tribes (STs)`. The Act was brought into force on `January 31, 1990`. 

**Protection of Civil Rights (PCR) Act** - 
An Act to prescribe punishment for the `preaching and practice of - "Untouchability"`

The crime of **arson** is defined in the Indian Penal Code, 1860, under Sections 435 and 436 IPC. This section deals with `mischief caused by fire` or explosive substances with the `intent to damage property`

**Dacoity** is a serious criminal offence under Section 391 of the Indian Penal Code (IPC). It is `an armed robbery or group robbery` in which a group of people (five or more) steal property from individuals or groups using violence or the threat of violence.
"""


def standardize_state_names(df, state_column="STATE/UT"):

    df[state_column] = df[state_column].str.strip()  # Remove leading/trailing spaces
    df[state_column] = df[state_column].str.capitalize()  # Convert to Capitalize
    df[state_column] = df[state_column].str.replace(
        "&", "AND"
    )  # Replace '&' with 'AND'
    df[state_column] = df[state_column].str.replace(" ut", "")  # Remove 'UT'
    df[state_column] = df[state_column].replace(
        {"AANDn islands": "A AND n islands", "DANDn haveli": "D AND n haveli"}
    )
    return df


cbd = standardize_state_names(cbd)

print(cbd["STATE/UT"].unique())

# Analyzing number of each type of case in each state
crime_types = [
    "Murder",
    "Assault on women",
    "Kidnapping and Abduction",
    "Dacoity",
    "Robbery",
    "Arson",
    "Hurt",
    "Prevention of atrocities (POA) Act",
    "Protection of Civil Rights (PCR) Act",
    "Other Crimes Against SCs",
]

## Total cases over the years in each State

# Set up a grid for subplots
num_crimes = len(crime_types)
num_cols = 2
num_rows = (num_crimes // num_cols) + (num_crimes % num_cols > 0)

fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, num_rows * 6))

# Plot each type of crime in each subplot
for i, crime in enumerate(crime_types):
    row = i // num_cols
    col = i % num_cols
    ax = axes[row, col]

    data = cbd.groupby("Year")[crime].sum().reset_index()
    sns.lineplot(
        x="Year", y=crime, data=data, marker="o", color="green", ax=ax, label=crime
    )
    ax.set_title(f"Total {crime} per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel(f"Total {crime}")
    ax.legend()
# Use subplots_adjust instead of tight_layout
plt.subplots_adjust(hspace=0.8, wspace=0.4)  # Adjust spacing between subplots
plt.show()

total_cases_per_state = cbd.groupby('STATE/UT').sum()
# total_cases_per_state['Murder']

## Plotting total cases over the years in each State

plt.figure(figsize=(12, 5))
total_cases_per_state['Murder'].sort_values(ascending=False).plot(kind='bar', title='Total Murder Cases Over the Years in Each State', color='skyblue')
plt.xlabel('State/UT')
plt.ylabel('Number of Murder Cases')
plt.show()

## Plotting each type of crime in each state

# Set up a grid for subplots
num_crimes = len(crime_types)
num_cols = 2
num_rows = (num_crimes // num_cols) + (num_crimes % num_cols > 0)

fig, axes = plt.subplots(num_rows, num_cols, figsize=(22, num_rows * 6))

# Plot each type of crime in each subplot
for i, crime in enumerate(crime_types):
    row = i // num_cols
    col = i % num_cols
    ax = axes[row, col]
    total_cases_per_state[crime].sort_values(ascending=False).plot(kind='bar', ax=ax, color='cornflowerblue')
    ax.set_title(f'Total {crime} Cases')
    ax.set_xlabel('State/UT')
    ax.set_ylabel('Number of Cases')
# Use subplots_adjust instead of tight_layout
plt.subplots_adjust(hspace=1.5, wspace=0.4)  # Adjust spacing between subplots
plt.show()

## states with zero cases

for crime in crime_types:
    cases = cbd.groupby('STATE/UT')[crime].sum()
    zero = cases[cases == 0]
    print(f"\n\nStates with zero {crime} cases:\n")
    print(zero)

## Plot the correlation matrix

matrix = cbd[crime_types].corr()
# Plot the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(matrix, annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlation Matrix of Different Crime Types Including Total Crimes')
plt.show()

# Grouping data by 'STATE/UT' and summing only the numeric columns
total_cases_per_state = cbd.groupby('STATE/UT')[crime_types].sum()

# Add a column for total crimes per state
total_cases_per_state['Total_Crimes'] = total_cases_per_state.sum(axis=1)

# Top 5 states with the highest total crimes reported
top_states = total_cases_per_state['Total_Crimes'].sort_values(ascending=False).head(5)
print("Top 5 states with highest total crimes reported:\n", top_states)

# Visualizing top 5 states with the highest total crimes
plt.figure(figsize=(12, 6))
top_states.plot(kind='bar', title='Top 5 States with Highest Total Crimes Reported', color='salmon')
plt.xlabel('State/UT')
plt.ylabel('Total Number of Crimes')
plt.show()







