import pandas as pd

bios = pd.read_csv("bios.csv")

print("Sorted Names Alphabetically: ")
print(bios.sort_values("name"))

print("Sorted Weight Largest to Smallest: ")
print(bios.sort_values("weight_kg", ascending=False))

print("Sorted Deaths Chronologically: ")
print(bios.sort_values("died_date"))
