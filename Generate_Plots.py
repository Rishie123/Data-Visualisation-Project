
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches


# importing the data
data = pd.read_excel('Dataset.xlsx')

# Define lists of countries for each region
asia_countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
# north_america_countries = ['Canada', 'United States']  # Removing North America
south_america_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
europe_countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']
australia_countries = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# Filter data for each region
data_asia = data[data['country_name'].isin(asia_countries)]
# data_north_america = data[data['country_name'].isin(north_america_countries)]  # Removing North America
data_south_america = data[data['country_name'].isin(south_america_countries)]
data_europe = data[data['country_name'].isin(europe_countries)]
data_australia = data[data['country_name'].isin(australia_countries)]

# Calculate the number of reforms for each region
reforms_asia = data_asia.groupby('country_name').size().nlargest(2)
# reforms_north_america = data_north_america.groupby('country_name').size().nlargest(2)  # Removing North America
reforms_south_america = data_south_america.groupby('country_name').size().nlargest(2)
reforms_europe = data_europe.groupby('country_name').size().nlargest(2)
reforms_australia = data_australia.groupby('country_name').size().nlargest(2)

# Create a DataFrame for the stacked bar chart
df = pd.DataFrame({
    'Asia': reforms_asia,
    # 'North America': reforms_north_america,  # Removing North America
    'South America': reforms_south_america,
    'Europe': reforms_europe,
    'Australia': reforms_australia
}).fillna(0)

# Reorder columns for sorting legends by regions
df = df[['Asia', 'South America', 'Europe', 'Australia']]

# Define the fixed colors
colors = ['#0c5193', '#0fb1c6', '#d6ad42']

# Plotting
font = {'fontname': 'Econ Sans'}

plt.figure(figsize=(11, 6))  # 332 points by 198 points

ax = df.T.plot(kind='bar', stacked=True, figsize=(11, 6), color=colors)
ax.set_xlabel('Region', **font, fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Reforms', **font, fontsize=12, fontweight='bold')
ax.set_xticklabels(ax.get_xticklabels(), **font, fontsize=10)

# Add horizontal grid lines
ax.yaxis.grid(True)

# Add a red brick at the top left corner touching the top of the chart
ax.add_patch(patches.Rectangle((0.02, 0.97), 0.04, 0.03, color='red', transform=ax.transAxes))

# Title inside the plot with some space from the top
ax.text(0.56, 0.96, 'Top 2 - no. of Education Reforms ', ha='right',fontdict=font, fontsize=14, fontweight='bold', transform=ax.transAxes)

# Adjust legend to be more informative
ax.legend(title='Top 2 by no. of Education Reforms', bbox_to_anchor=(1, 1), fontsize=10)
# Save the plot as a figure
plt.savefig('Top-2-countries_by_region.svg', bbox_inches='tight')

plt.show()


# In[22]:


import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches

# Assuming your DataFrame is named 'data' and it contains the reform data
data = pd.read_excel('werd_v2.xlsx')

# Filter data for Asian and European countries
asian_countries = ['Afghanistan', 'China', 'India', 'Japan', 'South Korea', 'Pakistan', 'Bangladesh', 'Indonesia', 'Iran', 'Iraq', 'Turkey', 'Saudi Arabia', 'Vietnam', 'Philippines', 'Thailand']
european_countries = ['Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Netherlands', 'Switzerland', 'Poland', 'Sweden', 'Belgium', 'Austria', 'Norway', 'Denmark', 'Finland', 'Greece']

data_asian = data[data['country_name'].isin(asian_countries)]
data_europe = data[data['country_name'].isin(european_countries)]

# Filter data starting from the year 1900 and not exceeding 2024
data_asian = data_asian[(data_asian['year'] >= 1900) ]
data_europe = data_europe[(data_europe['year'] >= 1900) ]

# Group data by year and count the number of reforms for each year
reforms_by_year_asian = data_asian.groupby('year').size()
reforms_by_year_europe = data_europe.groupby('year').size()

# Define the fixed colors
colors = ['#0c5193', '#0fb1c6']

# Plotting
font = {'fontname': 'Econ Sans'}

plt.figure(figsize=(12, 6))

# Plot reforms in Asia as a line plot with specified color
plt.plot(reforms_by_year_asian.index, reforms_by_year_asian.values, label='Asia', color=colors[0])

# Plot reforms in Europe as a line plot with specified color
plt.plot(reforms_by_year_europe.index, reforms_by_year_europe.values, label='Europe', color=colors[1])

# Get the current Axes object
ax = plt.gca()

# Enable y-axis grid lines
ax.yaxis.grid(True)

# Add a red brick at the top left corner touching the top of the chart
ax.add_patch(patches.Rectangle((0.02, 0.97), 0.04, 0.03, color='red', transform=ax.transAxes))

# Title inside the plot with some space from the top
ax.text(0.56, 0.9, 'Education Reforms over time in Asia vs Europe ', ha='center', fontdict=font, fontsize=14, fontweight='bold', transform=ax.transAxes)

plt.xlabel('Year', **font, fontsize=10, fontweight='bold')
plt.ylabel('Number of Reforms', **font, fontsize=10, fontweight='bold')

# Set x-axis limits and tick labels
plt.xlim(1900, 2024)
plt.xticks(range(1900, 2025, 10), rotation=45)

plt.legend()
plt.tight_layout()
plt.savefig("reforms_over_time.svg")
plt.show()


# In[ ]:




