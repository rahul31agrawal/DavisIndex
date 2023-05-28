# CELL
import pandas as pd

# Pull data from external source or manually define data
pass

import requests
import json
# key for inegi = 75565229-2f7d-38f4-3255-a593ca8eb2be

newURL = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6207131345,6207131346,6207131349/es/0700/false/BISE/2.0/75565229-2f7d-38f4-3255-a593ca8eb2be?type=json"
response_API = requests.get(newURL)
#print(response_API.status_code)


json = response_API.json()

json

# CELL
json.keys()

# CELL
json['Series']

# CELL
#type(json['Series'])
type(json['Series'][0])
df = pd.json_normalize(json['Series']) #Results contain the required data
print(df)

# CELL
df_Observations = pd.json_normalize(json['Series'],record_path='OBSERVATIONS',meta = 'INDICADOR')
df_Observations.head()

# CELL
df_Observations.drop(['OBS_EXCEPTION', 'OBS_STATUS','OBS_SOURCE','OBS_NOTE','COBER_GEO'], axis=1, inplace=True)
df_Observations

# CELL
def classification(value):
	if value == "6207131346":
		return "Sales"
	if value == "6207131345":
		return "Production"
	elif value == "6207131356":
		return "Wholesale"
	elif value == "6207131349":
		return "Exports"


df_Observations['classification'] = df_Observations['INDICADOR'].map(classification)
df_Observations.head()

# CELL
#result = df_Observations
df_Observations.drop(['INDICADOR'], axis=1, inplace=True)
df_Observations

# CELL
df_Observations['Year'] = pd.DatetimeIndex(df_Observations['TIME_PERIOD']).year
df_Observations

# CELL
df_Observations['Month'] = pd.DatetimeIndex(df_Observations['TIME_PERIOD']).month
df_Observations

# CELL
df_Observations['Unit']= 'unit'
df_Observations['Description']='-'
df_Observations['Country']= 'Mexico'
df_Observations['Source/Grade breakdown']= 'Light Vehicles'
df_Observations['Product']= 'Auto'
df_Observations['Group'] = 'Auto Sales/Production (Light Vehicles) - Mexico'
df_Observations['Source']='D129'
df_Observations.head()

# CELL
def descrip(value):
	if value == "Sales":
		return "Retail"

	else:
		return "-"


df_Observations['Description'] = df_Observations['classification'].map(descrip)
df_Observations

# CELL
df_Observations.drop(columns=['TIME_PERIOD'], axis=1, inplace=True)
df_Observations.rename(columns = {'OBS_VALUE':'Value','classification':'Type'}, inplace = True)
df_Observations

# CELL
result = df_Observations

