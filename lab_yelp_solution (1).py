import pip
import numpy as np 
import pandas as pd
from pandas.io.json import json_normalize

pip.main(["install","yelp3"])
from yelp3.client import Client

apikey='HsoG8rJLtpsvMaQ5_fjUvTSKuFg20fMAzKWWD-4NPSthNeTP3p2yNGSviZ9bmZ0z17vOW1k0Kzpx_FW8qAgSLrHLOYv1kT6Zx9qJUN3jshfcBWy2hcfpQmhk2l-oWnYx'

api = Client(apikey)

params={'term':'Indian','limit':50,'offset':0}
val = api.business_search(location='New Jersey',**params)
df = json_normalize(val,'businesses')
df2 = json_normalize(val)

pip.main(['install','uszipcode'])
from uszipcode import ZipcodeSearchEngine

search = ZipcodeSearchEngine()
res = search.by_state(state='New Jersey',returns=0)
resdf = json_normalize(res)

zcode = resdf[0]
za = zcode.values
zc=za[-10:].tolist()
zc

mdf = pd.DataFrame()
for i in zc:
    params={'term':'Indian','limit':50,'offset':0}
    val = api.business_search(location=i,**params)
    df = json_normalize(val)
    df2 = json_normalize(val,'businesses')
    t = df.loc[0,'total']
    mdf = mdf.append(df2,ignore_index=True)
    cnt=50
    while t>0:
        params={'term':'Indian','limit':50,'offset':cnt}
        val = api.business_search(location=i,**params)
        df2 = json_normalize(val,'businesses')
        mdf = mdf.append(df2,ignore_index=True)
        t = t-50
        cnt=cnt+50

mdf.shape

mdf.columns

pip.main(['install','textblob'])
from textblob import TextBlob

idlist = mdf.id
idlist

idlist = mdf['id'].tolist()

ps = []
for i in idlist:
    rev = api.review(i)
    dfrev = json_normalize(rev,'reviews')
    textlist = dfrev['text'].tolist()
    polarity = []
    for t in textlist:
        tx = TextBlob(t)
        polarity.append(tx.sentiment.polarity)
    pol = np.array(polarity)
    ps.append(pol.mean())  
    
ps
        
mdf['pol']=pd.Series(ps)
mdf['location']





gdf2 = gdf.reset_index(True)

mdf2 = mdf.location.apply(pd.Series)
mdf2['id']=mdf['id']
mdf2['pol']=mdf['pol']
gdf = mdf2.groupby(['id','zip_code'])['pol'].mean()
gdf2 = gdf.reset_index()
mdf2.shape
gdf2.shape

gdf2.columns
mdf2.columns


dictyelp = dict(zip(mdf2.id,mdf2.zip_code))

gdf2['zip_code']=gdf3['id'].map(dictyelp)    
gdf2.shape

gdf4 = gdf2.groupby('zip_code')['pol'].mean()
gd5 = gdf4.reset_index()
gd5.sort_values('pol',ascending=False)


resdf[resdf[0]=='07866']
resdf