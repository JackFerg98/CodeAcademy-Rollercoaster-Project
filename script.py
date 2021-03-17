# Import internal library
import codecademylib3

# 1 
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
# load rankings data
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# print(wood)
# 2
# Create a function to plot rankings over time for 1 roller coaster
def coaster_plot(name, park):
  wood_df = wood[(wood['Name'] == name) & (wood['Park'] == park)]
  ax = plt.subplot()
  plt.plot(wood_df['Year of Rank'], wood_df['Rank'])
  plt.ylabel('Rank')
  plt.xlabel('Year of Ranking')
  plt.title(name + ''''s Ranking''')
  plt.legend([name])
  ax.invert_yaxis()
  plt.show()

def coasters_plot(name1, name2, park1, park2):
  wood_df1 = wood[(wood['Name'] == name1) & (wood['Park'] == park1)]
  wood_df2 = wood[(wood['Name'] == name2) & (wood['Park'] == park2)]
  ax = plt.subplot()
  plt.plot(wood_df1['Year of Rank'], wood_df1['Rank'])
  plt.plot(wood_df2['Year of Rank'], wood_df2['Rank'])
  plt.ylabel('Rank')
  plt.xlabel('Year of Ranking')
  plt.legend([name1, name2])
  plt.title(name1 + ''''s''' + ' and ' + name2 + ''''s''' + ' Ranks over the years.')
  ax.invert_yaxis()
  plt.show()
# 3
# Create a plot of El Toro ranking over time
coaster_plot('El Toro', 'Six Flags Great Adventure')
# Create a plot of El Toro and Boulder dash hurricanes
plt.clf()
coasters_plot('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce')
# 4
# Create a function to plot top n rankings over time
def top_ranked(df, n):
  top = df[df['Rank'] <= n]
  fig, ax = plt.subplots(figsize = (14,14))
  for coaster in set(top['Name']):
    coaster_rankings = top[top['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label = coaster, linewidth = 5, alpha = 0.5)
    ax.set_yticks([i for i in range(1,6)])
    ax.invert_yaxis()
  
  plt.title('Top ' + str(n) + ' Rankings')
  plt.ylabel('Ranking')
  plt.xlabel('Year')
  plt.legend(loc= 2, bbox_to_anchor = (1, 1))
  plt.show()
# Create a plot of top n rankings over time
plt.clf()
top_ranked(wood, 5)
# 5
# load roller coaster data
coasters = pd.read_csv('roller_coasters.csv')
# print(coasters.head())
# 6
# Create a function to plot histogram of column values
def hist_coaster(df, column):
  plt.clf()
  plt.figure(figsize = (8,8))
  plt.hist((df[column]).dropna(), normed = True, color = '#000080', bins = 20)
  plt.xlabel(column.capitalize().replace('_', ' '))
  plt.ylabel('Proportion')
  plt.title('Rollercoaster Histogram')
  plt.show()
# Create histogram of roller coaster speed
hist_coaster(coasters, 'speed')
# Create histogram of roller coaster length
hist_coaster(coasters, 'length')
# Create histogram of roller coaster number of inversions
hist_coaster(coasters, 'num_inversions')
# Create a function to plot histogram of height values
def hist_heights(df, column):
  plt.clf()
  heights = coasters[coasters['height'] <= 140]
  plt.figure(figsize = (8,8))
  # print(heights)
  plt.hist(heights[column].dropna(), normed = True, color = '#000080', bins = 20)
  plt.xlabel(column.capitalize().replace('_', ' '))
  plt.ylabel('Proportion')
  plt.title('Rollercoaster Histogram')
  plt.show()
# Create a histogram of roller coaster height
hist_heights(coasters, 'height')
# 7
# Create a function to plot inversions by coaster at park
def inversion_bar(df, park):
  plt.clf()
  inversions = df[df['park'] == park]
  coaster_names = inversions['name']
  num_inversion = inversions['num_inversions']  
  plt.figure(figsize = (10,8))
  plt.bar(range(len(coaster_names)), num_inversion, color = '#000080')
  ax = plt.subplot()
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation = 90)
  plt.ylabel('Number of Inversions')
  plt.title('Rollercoaster Inversions at ' + park.capitalize())
  plt.show()
  
# Create barplot of inversions by roller coasters
inversion_bar(coasters, 'Parc Asterix')
# 8
# Create a function to plot a pie chart of status.operating
def pie_time(df):
  plt.clf()
  plt.figure(figsize = (10,10))
  coast_open = df[df['status'] == 'status.operating']
  coast_closed = df[df['status'] == 'status.closed.definitely']
  pie_store = []
  pie_store.append(len(coast_open))
  pie_store.append(len(coast_closed))
  plt.pie(pie_store, autopct = '%0.1f%%', labels = ['Open', 'Closed'], explode = [0.25,0], colors = ['#518cf5', '#db2828'], textprops = {'fontsize':20})
  plt.title('Representation of Rollercoasters Status', fontsize = (20))
  plt.axis('equal')
  plt.show()

# Create pie chart of roller coasters
pie_time(coasters)
# 9
# Create a function to plot scatter of any two columns
def scatter_two(df, column1, column2):
  plt.clf()
  plt.figure(figsize = (8,8))
  var1 = df[column1]
  var2 = df[column2]
  plt.scatter(var1, var2, color = '#db2828')
  plt.title(column2.capitalize() + ' vs ' + column1.capitalize())
  plt.xlabel(column1.capitalize())
  plt.ylabel(column2.capitalize())
  plt.show()

scatter_two(coasters, 'speed', 'length')
# Create a function to plot scatter of speed vs height
def scatter_height(df, column1, column2):
  plt.clf()
  plt.figure(figsize = (8,8))
  df = df[df['height'] < 140]
  var1 = df[column1]
  var2 = df[column2]
  plt.scatter(var1, var2, color = '#db2828')
  plt.title(column2.capitalize() + ' vs ' + column1.capitalize())
  plt.show()
# Create a scatter plot of roller coaster height by speed
scatter_height(coasters, 'height', 'speed')