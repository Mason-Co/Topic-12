import pandas as pd

bios = pd.read_csv("bios.csv")

print("Removing Specified Columns...\n")
print(bios.drop(columns=["born_date", "born_city", "born_region", "died_date"]))

print("\n\nAdding 'power' Column...\n")
power = bios['power'] = bios['height_cm'] * bios['weight_kg']
print("\n\nSorting 'power' Column...\n")
print(bios.sort_values('power', ascending=False))

print("\n\nCreating New .csv...\n")
newBios = bios.copy()
newBios.to_csv("New_Bios.csv")
