# CELL
import pandas as pd

result = pd.DataFrame()

# CELL
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

# CELL
# CELL
# or: requests.get(url).content

resp = urlopen("https://www150.statcan.gc.ca/n1/tbl/csv/34100175-eng.zip")
myzip = ZipFile(BytesIO(resp.read()))
myzip.namelist()

# CELL
# CELL
with myzip.open(myzip.namelist()[0], 'r') as g:     
    df = pd.read_csv(g,low_memory=False)
df

# CELL
# CELL
result = df

# CELL
result.info()
