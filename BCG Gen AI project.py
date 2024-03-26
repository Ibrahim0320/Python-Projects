# Boston Consulting Group Gen AI chatbot

# A project focused on applying AI and data analysis skills to develop AI-powered tools, 
# such as a financial chatbot, while learning to translate complex data into strategic business insights.

# import data from file


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

