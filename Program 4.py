import pandas as pd

bios = pd.read_csv("bios.csv")

print()
print(bios.drop(columns=["born_date", "born_city", "born_region", "died_date"]))

print()
power = bios['power'] = bios['height_cm'] * bios['weight_kg']
print(bios.sort_values('power', ascending=False))

newBios = bios.copy()
newBios.to_csv("New_Bios.csv")