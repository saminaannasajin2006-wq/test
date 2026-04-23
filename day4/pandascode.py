import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\sam\day4\mark.csv")

print(df)

plt.bar(df["Name"],df["Marks"])
plt.xlabel("Students")
plt.xlabel("Marks")
plt.title("Student Marks Graph")

plt.show()