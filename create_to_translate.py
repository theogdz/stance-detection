import pandas as pd

df = pd.read_csv('data/train.csv')
related = df[df.label != 'unrelated']

seen = set()
to_translate = []
id = []
for index,row in related.iterrows():
    if row['tid1'] not in seen:
        seen.add(row['tid1'])
        id.append(row['tid1'])
        to_translate.append(row['title1_en'])
    if row['tid2'] not in seen:
        seen.add(row['tid2'])
        id.append(row['tid2'])
        to_translate.append(row['title2_en'])

df_translate = pd.DataFrame()
df_translate['Id'] = id
df_translate['Text'] = to_translate

df_translate.to_csv('data/to_translate.csv', index= False)