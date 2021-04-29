import pandas as pd
import datetime
path = '/content/drive/MyDrive/Major Project/src/'
df = pd.read_csv(path+'deaths_data/deaths_org.csv')
df = df.iloc[2:-4]
df=df.reset_index(drop=True)
lst=[]
for date in df['Date']:
  if not isinstance(date,str):
    print(date)
  lst.append(datetime.datetime.strptime(date, '%d-%b-%y'))
  if not isinstance(lst[-1], datetime.datetime):
    print(date)
print(lst)
print(len(df), len(lst))
df['Date'] = pd.DataFrame(lst)
df.to_csv(path+'deaths_data/deaths_modified.csv')