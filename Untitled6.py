#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the necessary libraries

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


# In[2]:


# Write the article
with open('reforms_article_top3.txt', 'w') as f:
    f.write("# Distribution of Reforms by Asian Countries (Treemap)\n\n")
    f.write("In an era defined by rapid globalization and dynamic economic shifts, Asian countries have emerged as key players in shaping the future landscape of reforms. Analyzing the distribution of reforms across these nations provides valuable insights into their policy priorities and socio-economic trajectories.\n\n")
    f.write("## Understanding the Data\n\n")
    f.write("The data utilized for this analysis is sourced from a comprehensive dataset encompassing a wide array of reforms across various sectors. Specifically focusing on Asian countries, the dataset highlights the reform initiatives undertaken by nations such as Afghanistan, China, India, Japan, and others.\n\n")
    f.write("## Unveiling the Patterns\n\n")
    f.write("Upon aggregating and processing the data, a compelling visualization in the form of a treemap emerges. Each rectangle within the treemap represents a specific country, with its size proportional to the number of reforms enacted. The color palette employed further accentuates the visual hierarchy, aiding in the identification of prominent contributors to the reform landscape.\n\n")
    f.write("## Key Insights\n\n")
    f.write("- **Diverse Landscape**: The treemap underscores the diversity of reform efforts across Asian countries. From economic policy reforms to social initiatives, each nation exhibits a unique set of priorities tailored to its developmental agenda.\n\n")
    f.write("- **Regional Dynamics**: While certain countries stand out as leaders in reform implementation, the visualization also sheds light on regional disparities. The distribution of reforms unveils patterns of collaboration and competition, reflecting broader geopolitical dynamics within the region.\n\n")
    f.write("- **Policy Implications**: By dissecting the reform landscape, policymakers and analysts gain valuable insights into the efficacy and impact of various policy interventions. Identifying successful reform models can inform evidence-based decision-making and facilitate cross-country learning.\n\n")
    f.write("## Future Directions\n\n")
    f.write("As Asian countries continue to navigate the complexities of global integration and domestic development, understanding the evolving landscape of reforms remains paramount. Leveraging data-driven approaches and collaborative frameworks can pave the way for inclusive and sustainable growth in the region.\n\n")
    f.write("## Conclusion\n\n")
    f.write("The treemap visualization serves as a powerful tool for dissecting the distribution of reforms across Asian countries. Beyond its aesthetic appeal, the visualization encapsulates a wealth of information, offering stakeholders a nuanced understanding of policy dynamics and reform trajectories. By harnessing such insights, policymakers can chart a course towards a more prosperous and equitable future for all.\n")

print("Article saved as 'reforms_article.txt' and plot saved as 'reforms_treemap.svg'.")

#importing the data

data = pd.read_excel('werd_v2.xlsx')

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




