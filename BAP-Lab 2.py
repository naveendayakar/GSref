import numpy as np
import pandas as pd
pip.main(['install','twitter'])
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
import matplotlib.pyplot as plt
import pandas as pd
import csv
import pandas as pd
from collections import Counter



ck='Y1mLW9IApc7rx3nCynXOsx0FH'
cs='j3K0YIMdorVQhm31TfDyULsrVFGAohowwO1SEM59MjcxSphMwN'
at='961675725085560836-H9A7MqmaxmY1q3OhgwgABvKyQVvR6n0'
ats='8tziPF38vyCtmDGKUJ2ppNzaJwmW9ci3mwv3jbwFSUxTe'

oauth = OAuth(at, ats, ck, cs)

twitter = Twitter(auth=oauth)

twit_api= Twitter(auth=oauth)
import json 
from pandas.io.json import json_normalize


res=twit_api.search.tweets(q='SpaceX',count=100)
resdf= json_normalize(res,'statuses')
list(resdf.columns)
stat=resdf['text']
stat

resdf['created_at'].min()
resdf['created_at'].max()
mid=resdf['id'].min()
mid=mid-1

res2= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf2= json_normalize(res2,'statuses')
list(resdf2.columns)
stat2=resdf2['text']

resdf2['created_at'].min()
resdf2['created_at'].max()
mid=resdf2['id'].min()
mid=mid-1


res3= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf3= json_normalize(res3,'statuses')
list(resdf3.columns)
stat3=resdf3['text']

resdf3['created_at'].min()
resdf3['created_at'].max()
mid=resdf3['id'].min()
mid=mid-1

res4= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf4= json_normalize(res4,'statuses')
list(resdf4.columns)
stat4=resdf4['text']

resdf4['created_at'].min()
resdf4['created_at'].max()
mid=resdf4['id'].min()
mid=mid-1

res5= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf5= json_normalize(res5,'statuses')
list(resdf5.columns)
stat5=resdf5['text']

resdf5['created_at'].min()
resdf5['created_at'].max()
mid=resdf5['id'].min()
mid=mid-1


res6= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf6= json_normalize(res6,'statuses')
list(resdf6.columns)
stat6=resdf6['text']

resdf6['created_at'].min()
resdf6['created_at'].max()
mid=resdf6['id'].min()
mid=mid-1



res7= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf7= json_normalize(res7,'statuses')
list(resdf7.columns)
stat7=resdf7['text']

resdf7['created_at'].min()
resdf7['created_at'].max()
mid=resdf7['id'].min()
mid=mid-1

res8= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf8= json_normalize(res8,'statuses')
list(resdf8.columns)
stat8=resdf8['text']

resdf8['created_at'].min()
resdf8['created_at'].max()
mid=resdf8['id'].min()
mid=mid-1


res9= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf9= json_normalize(res9,'statuses')
list(resdf9.columns)
stat9=resdf9['text']

resdf9['created_at'].min()
resdf9['created_at'].max()
mid=resdf9['id'].min()
mid=mid-1


res10= twit_api.search.tweets(q="SpaceX", count=100, max_id=mid)
resdf10= json_normalize(res10,'statuses')
list(resdf10.columns)
stat10=resdf10['text']

resdf10['created_at'].min()
resdf10['created_at'].max()
mid=resdf10['id'].min()
mid=mid-1





df = resdf.append([resdf2, resdf3,resdf4, resdf5,resdf6,resdf7, resdf8,resdf9, resdf10],ignore_index=False)
df.head()

words=df['text'].str.split(' ', expand=True).stack().value_counts()
words[:20].plot(kind='barh')
df.to_csv("SpaceX-BAP.csv")



