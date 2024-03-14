#Accenture Project
# This project involves cleaning, identifying, and combining three files that relate to the most popular content on a social media app
# In order to create simple visualisations of popular elemnts that need to be considered for trend learning
# Nothing too complicated, rather straight forward, lots of print statements have been commented out
# just so the terminal doesn't get filled with extra results
# comment in/out whatever print statements you require

import pandas as pd

content= pd.read_csv('/Users/muhammadibrahim/Downloads/Content.csv')
reaction= pd.read_csv('/Users/muhammadibrahim/Downloads/Reactions.csv')
reaction_types= pd.read_csv('/Users/muhammadibrahim/Downloads/ReactionTypes.csv')


# Content Cleaning

content= content.dropna()

content= content.drop(['Unnamed: 0'], axis= 1)
content= content.drop(['URL'], axis= 1)
content= content.drop(['User ID'], axis= 1)
content.rename(columns={'Type': 'Content Type'}, inplace=True)

content = content.astype(str)
for column in content.columns:
    # Replace instances of the word with quotation marks with the word without quotation marks
    content[column] = content[column].str.replace(r'"([^"]*)"', r'\1')

#print(content.head())

content.to_csv('Content.csv', index=False)
# Reaction cleaning


reaction= reaction.dropna()

reaction= reaction.drop(['Unnamed: 0'], axis= 1)
reaction= reaction.drop(['User ID'], axis= 1)
reaction.rename(columns={'Type': 'Reaction Type'}, inplace=True)

reaction = reaction.astype(str)
for column in reaction.columns:
    # Replace instances of the word with quotation marks with the word without quotation marks
    reaction[column] = reaction[column].str.replace(r'"([^"]*)"', r'\1')

#print(reaction.head())

reaction.to_csv('Reactions.csv', index=False)
#ReactionType cleaning


reaction_types.dropna()

reaction_types= reaction_types.drop(['Unnamed: 0'], axis= 1)
reaction_types.rename(columns={'Type': 'Reaction Type'}, inplace=True)

reaction_types = reaction_types.astype(str)
for column in reaction_types.columns:
    # Replace instances of the word with quotation marks with the word without quotation marks
    reaction_types[column] = reaction_types[column].str.replace(r'"([^"]*)"', r'\1')

#print(reaction_types.head())

reaction_types.to_csv('Reaction Types.csv', index=False)


mod_content= pd.read_csv('Content.csv')
mod_reactions= pd.read_csv('Reactions.csv')
mod_reaction_types= pd.read_csv('Reaction Types.csv')


# Join relevant columns to Reaction file

#First we merge Content and Reaction
content_merged_reaction = pd.merge(mod_content, mod_reactions, on='Content ID', how='inner') 

#Then we merge Reaction Type to the Content-Reaction merge
all_merged_reaction= pd.merge(content_merged_reaction, mod_reaction_types, on='Reaction Type', how='inner')


# Here we group the categories by score and arrange in descending order, with highest score on the top of the list
category= all_merged_reaction.groupby('Category')
category_scores = category['Score'].sum().reset_index()
category_scores_sorted = category_scores.sort_values(by='Score', ascending=False)

# This selects and holds the top 5 performing categories from our file
top_5_categories = category_scores_sorted.head(5)
#print(top_5_categories.head())

#Now we combine the Top 5 to the final dataset
cleaned_dataset_with_top_5_categories = pd.merge(all_merged_reaction, top_5_categories, on='Category')
cleaned_dataset_with_top_5_categories.rename(columns={'Score_x': 'Score'}, inplace=True)
cleaned_dataset_with_top_5_categories.rename(columns={'Score_y': 'Total Score'}, inplace=True)


# Now we save the result to a new CSV file on my MacBook
#cleaned_dataset_with_top_5_categories.to_csv('/Users/muhammadibrahim/Documents/cleaned_dataset_with_top_5_categories.csv', index=False)

'''

'''
#Accenture Data Insights

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data= pd.read_csv('/Users/muhammadibrahim/Downloads/Task 3_Final Content Data set.csv')

#Most popular category
category= data.groupby('Category')
category_scores = category['Score'].sum().reset_index()
category_scores_sorted = category_scores.sort_values(by='Score', ascending=False)

top_5_categories = category_scores_sorted.head(5)
#print(top_5_categories.head())

#most active month

data['Datetime'] = pd.to_datetime(data['Datetime'])
data['Month'] = data['Datetime'].dt.month
month_counts = data['Month'].value_counts()
#print(month_counts)

reactions= data['Reaction Type'].value_counts()
top_5= reactions.head(5)
#print(top_5)

#Top categories in which month

category_month_counts = data.groupby(['Month', 'Category']).size().reset_index(name='Count')
idx = category_month_counts.groupby('Month')['Count'].idxmax()
most_popular_categories = category_month_counts.loc[idx]

#print("Most popular category in each month:")
#print(most_popular_categories)

# Count the number of unique categories
num_unique_categories = data['Category'].nunique()
#print("Number of unique categories:", num_unique_categories)

# Find the most popular category
most_popular_category = most_popular_categories.loc[most_popular_categories['Count'].idxmax(), 'Category']

# Filter the DataFrame for the most popular category
most_popular_category_df = data[data['Category'] == most_popular_category]

# Count the number of reactions
num_reactions_most_popular_category = most_popular_category_df.shape[0]

# Print the result
#print("Number of reactions to the most popular category:", num_reactions_most_popular_category)

# Group the DataFrame by month and category, and count the occurrences
category_month_counts = data.groupby(['Month', 'Category']).size().reset_index(name='Count')

# For each month, find the category with the highest count
idx = category_month_counts.groupby('Month')['Count'].idxmax()

# Extract the corresponding rows
most_popular_categories_per_month = category_month_counts.loc[idx]

# Print the result
#print("Most popular category in each month:")
#print(most_popular_categories_per_month)


# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the bar graph
plt.bar(most_popular_categories['Month'], most_popular_categories['Count'], color='skyblue')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Number of Posts')
plt.title('Most Popular Category in Each Month')

# Customize x-axis labels
plt.xticks(range(1, 13), ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], rotation=45)

# Show plot
plt.tight_layout()
plt.show()




# Sort the categories based on count in descending order and select the top 5
top_5_categories = category_month_counts.groupby('Category')['Count'].sum().nlargest(5)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar plot
top_5_categories.plot(kind='bar', ax=ax, color='skyblue')

# Add labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Number of Interactions')
ax.set_title('Top 5 Content Categories')

# Show plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



