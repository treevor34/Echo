from pytrends.request import TrendReq
import pandas as pd
import time
startTime = time.time()
pytrend = TrendReq(hl='en-GB', tz=360)

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames)
df1 = df["keywords"].values.tolist()
df1.remove("Keywords")

dataset = []
dataset1 = []

for x in range(0,len(df1)):
     keywords = [df1[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     #timeframe='2021-04-01 2021-06-01',
     timeframe='today 12-m', #'all' outputs monthly so it would be possible
     geo='GB')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)
     
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     #timeframe='2021-04-01 2021-06-01',
     timeframe='all', #'all' outputs monthly so it would be possible
     geo='GB')
     data1 = pytrend.interest_over_time()
     if not data1.empty:
          data1 = data1.drop(labels=['isPartial'],axis='columns')
          dataset1.append(data1)

result = pd.concat(dataset, axis=1)
extraResult = pd.concat(dataset1, axis = 1)
result.to_csv('output.csv')
extraResult.to_csv('outputAll.csv')



executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))