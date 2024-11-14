import pandas as pd

athlete = pd.read_csv("athlete_events.csv")

print("First 5 lines:")
print(athlete.head(5))
print("\nLast 5 lines: ")
print(athlete.tail(5))