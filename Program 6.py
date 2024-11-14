import pandas as pd

athlete = pd.read_csv('athlete_events.csv')

print()
print(athlete.dropna())
print("Size decreased from 271116 to 30181.")