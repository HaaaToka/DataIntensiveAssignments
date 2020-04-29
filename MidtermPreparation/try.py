import pandas as pd   
import numpy as np
# Creating the dataframe    
df = pd.DataFrame({"A":[5, 2, 6, 4, None],   
                   "B":[12, 19, None, 8, 21],   
                   "C":[15, 26, 11, None, 3],  
                   "D":[14, 17, 29, 16, 23]})     
# while finding mean, it skip null values   
# print(df)
#print(info.mean(axis = 1, skipna = True))
# print(df["D"].mean())
# print(df[["D"]])
# print(type(df[["D"]]))
# print(type(df[['A']]))
# print(type(df.loc[:, ['A']]))
# print(type(df.iloc[:, [0]]))
# print(type(df.A))
# print(type(df['A']))
# print(type(df.loc[:, 'A']))
# print(type(df.iloc[:, 1]))
# print(df.iloc[::-1,:])
# print(df.iloc[:,::-1])

# print(type(df[["A","B"]]))
# print(type(df.loc[:,["A"]]))
# print(type(df.loc[:,"A"]))

# print(df["D"].mean(axis=0))
# print(type(df.iloc[2,:]))



# filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]

# cars = pd.read_csv(filename, names = headers)