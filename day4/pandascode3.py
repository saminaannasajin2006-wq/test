import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("C:\sam\day4\sumavg.csv")

print(df)

plt.bar(df["Name"],df["Sum"])
plt.xlabel("Students")
plt.xlabel("Sum")
plt.title("Student total_Marks Graph")

plt.show()