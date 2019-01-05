import numpy as np
import pandas as pd
pip.main(['install','twitter'])
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream


ck='Y1mLW9IApc7rx3nCynXOsx0FH'
cs='j3K0YIMdorVQhm31TfDyULsrVFGAohowwO1SEM59MjcxSphMwN'
at='961675725085560836-H9A7MqmaxmY1q3OhgwgABvKyQVvR6n0'
ats='8tziPF38vyCtmDGKUJ2ppNzaJwmW9ci3mwv3jbwFSUxTe'

oauth = OAuth(at, ats, ck, cs)

api = Twitter(auth=oauth)

import json 
from pandas.io.json import json_normalize


## getting 1000 tweets
df = pd.DataFrame()
mid=0

for i in range(11):
    if i==0:
        search_result=api.search.tweets(q='SpaceX',count=100)
    else:
        search_result=api.search.tweets(q='SpaceX',count=100,max_id = mid)
        dftemp= json_normalize(search_result,'statuses')
        mid=dftemp['id'].min()
        mid=mid-1
        df = df.append(dftemp, ignore_index= True)


df.head()
df.shape



tweettext= df['text']
tweettext
wordlist= pd.DataFrame()

## splitting the tweets into words
for u in tweettext:
    wsplit= u.split()
    wordlist= wordlist.append(wsplit, ignore_index=True)
    
    
    
wordlist.shape

wordlist.head()

allword=wordlist.groupby(0).size()
allword.head()
    
    
pip.main(["install","textblob"])
!python -m textblob.download_corpora
from textblob import TextBlob

tx=tweettext[0]
blob=TextBlob(tx)

##splitting the words into nouns
nouns =[]
for u in tweettext:
    blob=TextBlob(u)
    for word, tag in blob.tags:
        if tag=='NN':
            nouns.append(word)



nouns


nounlist=pd.DataFrame(nouns)
allnouns=nounlist.groupby(0).size()
allnouns.head()
top20noun = allnouns.sort_values(0,ascending=False).head(20)
top20noun.plot(kind='bar')




##splitting the words into verbs
verbs =[]
for u in tweettext:
    blob=TextBlob(u)
    for word, tag in blob.tags:
        if tag=='VB':
            verbs.append(word)



verbs


verblist=pd.DataFrame(verbs)
allverb=verblist.groupby(0).size()
allverb.head()
top20verb = allverb.sort_values(0,ascending=False).head(20)
top20verb.plot(kind='bar')



##sentiment graph on the tweets

##sentiment analysis
##positive or negative

blob.sentiment

polarity=[]
subj=[]

for t in tweettext:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)
    
poltweet= pd.DataFrame({'polarity': polarity, 'subjectivity': subj})
poltweet.plot(title= 'Polarity and Subjectivity')


