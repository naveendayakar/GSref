import numpy as np
import pandas as pd
!pip install python-craigslist

from craigslist import CraigslistHousing
from craigslist import CraigslistJobs

CraigslistHousing.show_filters()

cl_h=CraigslistHousing(site='newyork',area='mnh',category='aap',filters={'zip_code':'10011'})


res=[]
for result in cl_h.get_results(sort_by='newest',geotagged=True):
    res.append(result)

from pandas.io.json import json_normalize
df=json_normalize(res)
df.head()


##GOOGLE

gkey='AIzaSyBEeAEgxHYbnRkYwQem7vDrHpYzmzUf-oc'
pip.main(['install','googlemaps'])
import googlemaps

gapi=googlemaps.Client(key=gkey)
dr=gapi.directions("40.52552 -74.43821","40.75689 -73.99101",mode="driving",avoid="ferries")
dr[0]['legs'][0]['distance']
dr[0]['legs'][0]['duration']

df.head()
df2=df.geotag.apply(pd.Series)
df2
df['sgeo']=df2[0].astype(str)+','+df2[1].astype(str)
df['sgeo']



##put the directions in forloop fr the second parameter, get list of all distances.

