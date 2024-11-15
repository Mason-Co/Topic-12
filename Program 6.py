import pandas as pd

athlete = pd.read_csv('athlete_events.csv')

print("\n\nClearing Data With Missing Attributes...\n")
print(athlete.dropna())
print("\nSize decreased from 271116 to 30181.")
