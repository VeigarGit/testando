for data in list(df_data.columns):
    print(data, file=open('columns.txt', 'a'))
    x = df.values
q = 0
for data in list(df_data):
    print(data, file=open('valores.txt', 'w'))
    if q == 100:
        break
    print(1)
    q = q + 1
