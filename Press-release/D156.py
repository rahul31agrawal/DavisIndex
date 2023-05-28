# CELL
import pandas as pd

# Pull data from external source or manually define data
# pass

#import requests

#url = 'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/20100001/en'

#r = requests.get(url)

#json = r.json()
#json.keys()
#json['object']

# Set `result` to a pandas Dataframe
# result = pd.DataFrame()


from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

## or: requests.get(url).content

resp = urlopen("https://www150.statcan.gc.ca/n1/tbl/csv/20100001-eng.zip")
myzip = ZipFile(BytesIO(resp.read()))
myzip.namelist()

# CELL
with myzip.open(myzip.namelist()[0], 'r') as g:     
    df = pd.read_csv(g,low_memory=False)
df

# CELL
df['Year'] = pd.DatetimeIndex(df['REF_DATE']).year
df['Month'] = pd.DatetimeIndex(df['REF_DATE']).month

df['Product'] = 'Auto'
df['Type'] = 'Sales'
df['Source']='D156'
df['GEO'] = df.GEO.astype(str)
df['Group']="Auto Sales - "+df['GEO']

df['Description'] = df['Origin of manufacture']+' - '+df['Seasonal adjustment']

df['Unit'] = ""

for i in range(len(df.index)):
    if df['UOM'][i]=="Units":
        df['Unit'][i]="units"
    else:
        df['Unit'][i]=df['SCALAR_FACTOR'][i]+' - '+df['UOM'][i]
        
df.rename(columns = {'GEO':'Country', 'Vehicle type':'Source/Grade breakdown',
                    'VALUE':'Value'}, inplace = True)


df.head()

# CELL
df=df.drop(['REF_DATE','DGUID', 'Origin of manufacture', 'Sales', 'Seasonal adjustment', 'UOM',
       'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE',
       'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS',], axis=1)
df.head()

# CELL
result=df

print("code ran sucessfully")
