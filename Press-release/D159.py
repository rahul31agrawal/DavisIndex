# CELL
import pandas as pd

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

# CELL
respIPPI = urlopen("https://www150.statcan.gc.ca/n1/tbl/csv/18100265-eng.zip")
myzip2 = ZipFile(BytesIO(respIPPI.read()))
myzip2.namelist()

# CELL
with myzip2.open(myzip2.namelist()[0], 'r') as g:     
    df_IPPI = pd.read_csv(g,low_memory=False)
df_IPPI

# CELL
list(df_IPPI.columns)

# CELL
df_IPPI = df_IPPI.drop(columns=['GEO',
 'DGUID','UOM',
 'UOM_ID',
 'SCALAR_FACTOR',
 'SCALAR_ID',
 'VECTOR',
 'COORDINATE',
 'STATUS',
 'SYMBOL',
 'TERMINATED',
 'DECIMALS'])


df_IPPI

# CELL
df_IPPI['Year'] = pd.DatetimeIndex(df_IPPI['REF_DATE']).year
df_IPPI['Month'] = pd.DatetimeIndex(df_IPPI['REF_DATE']).month
df_IPPI.drop(columns=['REF_DATE'], axis=1, inplace=True)
df_IPPI.rename(columns = {'North American Product Classification System (NAPCS)':'Source/Grade breakdown','VALUE':'Value'}, inplace = True)
df_IPPI

# CELL
df_IPPI['Unit']= 'index'
df_IPPI['Description']='Industrial Product Price Index (Index 202001=100)'

df_IPPI['Country']= 'Canada'


df_IPPI['Type']= 'Macro'


df_IPPI['Product']= 'Macro'
df_IPPI['Group'] = 'Macro - Canada'
df_IPPI['Source']='D159'
df_IPPI.head()

# CELL
result = df_IPPI
