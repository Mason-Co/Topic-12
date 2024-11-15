import pandas as pd

bios = pd.read_csv("New_Bios.csv")

print("\n\nNumber of Players in Each Country: \n")
print(bios.value_counts("NOC"))

print("\n\nAverage Height (cm) in Each Country: \n")
print(bios.groupby(['NOC'])['height_cm'].mean())

print("\n\nAverage Power in Each Country: \n")
print(bios.groupby(['NOC'])['power'].mean())
