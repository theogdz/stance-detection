import pandas as pd


df_train = pd.read_csv('data/train.csv')
df_translation = pd.read_csv('data/translation.csv')
df_translation.set_index('Id', inplace=True)
max_id = df_train['id'].max()
to_append = []

# Delete rows where double translation equals orginal text
df_translation = df_translation[df_translation['Text'] != df_translation['Translated']]

for index, row in df_train.iterrows():
    newrow1 = row
    if row['tid1'] in df_translation.index and row['label'] != 'unrelated':
        newrow1['title1_en'] = df_translation.loc[row['tid1']]['Translated']
        max_id += 1
        newrow1['id'] = max_id
        to_append.append(newrow1)
    if row['tid2'] in df_translation.index and row['label'] != 'unrelated':
        newrow2 = row
        newrow2['title2_en'] = df_translation.loc[row['tid2']]['Translated']
        max_id += 1
        newrow2['id'] = max_id
        if newrow1.all() != newrow2.all():
            to_append.append(newrow2)


df_augmented = df_train.append(pd.DataFrame(to_append, columns=df_train.columns)).reset_index()


df_augmented.to_csv('data/augmented.csv', index=False)


print(f"Original:\n{df_train['label'].value_counts()}")
print(f"Augmented:\n{df_augmented['label'].value_counts()}")