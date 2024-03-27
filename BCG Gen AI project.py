# Boston Consulting Group Gen AI chatbot

# A project focused on applying AI and data analysis skills to develop AI-powered tools, 
# such as a financial chatbot, while learning to translate complex data into strategic business insights.

#The way this chatbot works is by taking in a csv file with preprocessed data ready to be read. 
#The chatbot will take in predefined statements and will return out strings consiting of data points
#relevant to the user query. This model is very straight forward and can be modified in many ways
#the addition of a machine learning algorithm to improve the chatbot and its thinking, so that it can grow into
#an entity capable of handling more complex discussion


'''
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows= None

data= pd.read_csv('Financial data.csv', delimiter=';')
df= data.copy()


df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue (billion $)'].pct_change() * 100

df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income (billion $)'].pct_change() * 100

df['Profit Margin (%)'] = (df['Net Income (billion $)'] / df['Total Revenue (billion $)']) * 100

df['Return on Assets (%)'] = (df['Net Income (billion $)'] / df['Total Assets (billion $)']) * 100

df['Debt-to-Equity Ratio'] = df['Total Liabilities (billion $)'] / df['Total Assets (billion $)']

df['Operating Profit Margin (%)'] = ((df['Total Revenue (billion $)'] - df['Cash from Oper.Activ. (billion $)']) / df['Total Revenue (billion $)']) * 100



company_comparison = df.groupby('Company').agg({
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean',
    'Operating Profit Margin (%)': 'mean',
    'Debt-to-Equity Ratio': 'mean'
})

df.head()
BCG_data_preprocessed= df.copy()
df.to_csv('BCG_data_preprocessed.csv', index=False)
'''

import numpy as np
import pandas as pd


data= pd.read_csv('BCG_data_preprocessed.csv')

pd.options.display.max_columns = None
pd.options.display.max_rows= None



def simple_chatbot(user_query, df):
   if user_query == "What is the total revenue of Tesla in 2023?":
        revenue_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Total Revenue (billion $)'].values[0]
        print(f"The total revenue of Tesla in 2023 is {revenue_2023} billion dollars.")   
   elif user_query == "What is the total revenue of Apple in 2023?":
        revenue_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Total Revenue (billion $)'].values[1]
        print(f"The total revenue of Apple in 2023 is {revenue_2023} billion dollars.")
   elif user_query == "What is the total revenue of Microsoft in 2023?":
        revenue_2023 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Total Revenue (billion $)'].values[2]
        print(f"The total revenue of Microsoft in 2023 is {revenue_2023} billion dollars.")
   elif user_query == "What is the net income of Tesla in 2023?":
        income_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Net Income (billion $)'].values[0]
        print(f"The net income of Tesla in 2023 is {income_2023} billion dollars.")
   elif user_query == "What is the net income of Apple in 2023?":
        income_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Total Revenue (billion $)'].values[1]
        print(f"The total revenue of Apple in 2023 is {income_2023} billion dollars.")
   elif user_query == "What is the net income of Microsoft in 2023?":
        income_2023 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Net Income (billion $)'].values[2]
        print(f"The net income of Microsoft in 2023 is {income_2023} billion dollars.")

   # Possibility to add more conditions for other predefined queries in a similar manner
   else:
       return "Sorry, I can only provide information on predefined queries."



user_query = "What is the total revenue of Tesla in 2023?"
simple_chatbot(user_query, data)