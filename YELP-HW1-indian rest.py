import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

import pip
pip.main()
pip.main(['install','yelp3'])
from yelp3.client import Client

apikey='BRfu2UBbZYf-2r2vUVHDOX7C0DWoNgUqfNXioJ_SjwbwUqRYIZ76YuRWc5IWNMKYPO7O9nXQnuzM_lh2mKiYBaE4laA4_GP610DGckhj8BR3Wz2fOo1L0_2LJx2PWnYx'

api= Client(apikey)

params={'term':'Indian','limit':50,'offset':0}
val=api.business_search(location='New Jersey',**params)
val
df=json_normalize(val,'businesses')
##to see the summary of the dataset
df2=json_normalize(val)
df2

##package to get all the zipcodes
pip.main(['install','uszipcode'])
from uszipcode import ZipcodeSearchEngine
search= ZipcodeSearchEngine()
res=search.by_state(state='New Jersey',returns=0)
resdf=json_normalize(res)
resdf

zcode=resdf[0]
za=zcode.values
za
zc=za[-10:].tolist()
zc

mdf=pd.DataFrame()
for i in zc:
    params={'term':'Indian','limit':50,'offset':0}
    val=api.business_search(location=i,**params)
    df=json_normalize(val)
    df2=json_normalize(val,'businesses')
    t=df.loc[0,'total']
    mdf=mdf.append(df2,ignore_index=True)
    cnt=50
    while t>0:
        params={'term':'Indian','limit':50,'offset':cnt}
        val=api.business_search(location=i,**params)
        df=json_normalize(val)
        df2=json_normalize(val,'businesses')
        mdf=mdf.append(df2,ignore_index=True)
        t=t-50
        cnt=cnt+50
        

mdf.shape

mdf.columns
idlist=mdf['id'].tolist()

ps=[]

for i in idlist:
    rev=api.review(i)
    dfrev=json_normalize(rev,'reviews')
    textlist=dfrev['text'].tolist()
    polarity=[]
    for t in textlist:
        tx=TextBlob(t)
        polarity.append(tx.sentiment.polarity)
    pol=np.array(polarity)
    ps.append(pol.mean())
    

ps


mdf['pol']=pd.Series(ps)
mdf.columns

gdf2=gdf

mdf2=mdf.location.apply(pd.Series)
mdf2['id']=mdf['id']
mdf2['pol']=mdf['pol']
mdf2.shape
gdf2.shape

gdf=mdf2.groupby(['id','zip_code'])['pol'].mean()
gdf2=gdf.reset_index()
gdf2


gdf4= gdf2.groupby('zip_code')['pol'].mean()
gdf4
gd5=gdf4.reset_index()
gd5.sort_values('pol',ascending=False)
##this is the result
resdf[resdf[0]=='07866']
resdf

##using dict
dictyelp=dict(zip(mdf2.id,mdf2.zip_code))
gdf2['zip_code']=gdf3['id'].map(dictyelp)
gdf2.shape


gdf3=pd.merge(gdf2,mdf2,how='left',on='id')
gdf3.shape

pip.main(['install','textblob'])
from textblob import TextBlob





for t in tweettext:
    tx=TextBlob(t)
    if(tx.sentiment.polarity)>=0.7:
        df['polarity']=tx.sentiment.polarity
        df['status']=True
    elif(tx.sentiment.polarity)<=-0.7:   
        df['polarity']=tx.sentiment.polarity
        df['status']=False
   



gdf= mdf.groupby('id')['id'].count()
gdf