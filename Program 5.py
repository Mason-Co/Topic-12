import pandas as pd

bios = pd.read_csv("New_Bios.csv")

print()
print(bios.value_counts("NOC"))

print()
print(bios.groupby(['NOC'])['height_cm'].mean())

print()
print(bios.groupby(['NOC'])['power'].mean())