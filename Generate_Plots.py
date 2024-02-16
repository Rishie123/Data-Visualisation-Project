#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the necessary libraries

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


# In[2]:




data = pd.read_excel('Dataset.xlsx')

# Define lists of countries for each region
asia_countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
north_america_countries = ['Canada', 'United States']
south_america_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
europe_countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']
australia_countries = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# Filter data for each region
data_asia = data[data['country_name'].isin(asia_countries)]
data_north_america = data[data['country_name'].isin(north_america_countries)]
data_south_america = data[data['country_name'].isin(south_america_countries)]
data_europe = data[data['country_name'].isin(europe_countries)]
data_australia = data[data['country_name'].isin(australia_countries)]

# Calculate the number of reforms for each region
reforms_asia = data_asia.groupby('country_name').size().nlargest(3)
reforms_north_america = data_north_america.groupby('country_name').size().nlargest(3)
reforms_south_america = data_south_america.groupby('country_name').size().nlargest(3)
reforms_europe = data_europe.groupby('country_name').size().nlargest(3)
reforms_australia = data_australia.groupby('country_name').size().nlargest(3)

# Create a DataFrame for the stacked bar chart
df = pd.DataFrame({
    'Asia': reforms_asia,
    'North America': reforms_north_america,
    'South America': reforms_south_america,
    'Europe': reforms_europe,
    'Australia': reforms_australia
}).fillna(0)

# Reorder columns for sorting legends by regions
df = df[['Asia', 'North America', 'South America', 'Europe', 'Australia']]

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
ax.text(0.5, 0.96, 'Top 3 Countries with the Highest Number of Reforms by Region', ha='center',fontdict=font, fontsize=14, fontweight='bold', transform=ax.transAxes)

# Adjust legend to be more informative
ax.legend(title='Top 3 Reformed Countries by Region', bbox_to_anchor=(1, 1), fontsize=10)
# Save the plot as a figure
plt.savefig('stacked_bar_chart.png', bbox_inches='tight')

plt.show()


# In[ ]:




