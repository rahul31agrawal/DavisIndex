# CELL
import pandas as pd

# Pull data from external source or manually define data
import requests
import json
#fred_key = 'ee0743b74c1facad1adf385cffa28ca1'

url_1 = "https://api.stlouisfed.org/fred/series/observations?series_id=DEUCPALTT01IXOBSAM&api_key=ee0743b74c1facad1adf385cffa28ca1&file_type=json"
url_2 = "https://api.stlouisfed.org/fred/series/observations?series_id=PIEATI02DEM661N&api_key=ee0743b74c1facad1adf385cffa28ca1&file_type=json"
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)

# CELL
json_1 = response_1.json()
json_2 = response_2.json()

# CELL
df1 = pd.DataFrame(json_1['observations'])
df2 = pd.DataFrame(json_2['observations'])

# CELL
df1.drop(['realtime_start','realtime_end'], axis=1, inplace=True)
df2.drop(['realtime_start','realtime_end'], axis=1, inplace=True)

# CELL
df1['Category'] = 'Consumer Price Index'
df1['Description'] = '(Index 2015=100,Seasonally Adjusted)'
df2['Category'] = 'Producer Price Index'
df2['Description'] = '(Index 2015=100,Not Seasonally Adjusted, Economic Activities: Industrial Activities: Domestic for Germany) '

# CELL
frames = [df1, df2]

df = pd.concat(frames)
df

# CELL
df['Unit']= 'index'

df['Year'] = pd.DatetimeIndex(df['date']).year
df['Month'] = pd.DatetimeIndex(df['date']).month
df['Country']= 'Germany'
df['Source/Grade breakdown']='-'
df['Product']= 'Macro'
df['Group'] = 'Macro - Germany'
df['Source']='D169'
df.rename(columns = {'value':'Value','Category':'Type'}, inplace = True)

df['Description'] = df['Type'] + " " + df['Description']
df['Type'] = 'Macro'

df.drop(columns=['date'], axis=1, inplace=True)
df.head()

# CELL
result = df
