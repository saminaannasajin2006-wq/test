import pandas as pd
data = {
    "calories":[420,300,390],
    "duration":[50,40,45]
}

#load data into a Dataframe object:
df = pd.DataFrame(data)
print(df)

data = {
    "students":["des","nir","dutt","sam","meg","adi","akshay","saf","george","basil"],
    "marks":[90,80,70,80,60,80,80,70,60,70]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[[0,1]])