import pandas as pd

# LOADING CSV
df = pd.read_csv("csv's\\aug_train.csv", index_col = 'enrollee_id')
# df = pd.read_csv("csv's\aug_train.csv", sep = "\t", names= ['sno', 'movname', ''year', 'rating', 'votes', 'genres']) # Incase if tabs are present this makes the seperator as tab, and name is used to name headers
print(df)


# FETCHING DATA 

# Import the requests library to download data from a URL
import requests
# Import StringIO to treat text data as a file
from io import StringIO
# URL of the CSV file hosted on GitHub
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
# User-Agent header to make the request appear as if it is coming from a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"
}
# Send an HTTP GET request to download the CSV file
req = requests.get(url, headers=headers)
# Convert the downloaded text into a file-like object
data = StringIO(req.text)
# Read the CSV data into a Pandas DataFrame
pd.read_csv(data)
print(pd)