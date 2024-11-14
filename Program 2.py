import pandas as pd

athlete = pd.read_csv("athlete_events.csv")

print("The fifth row of data: ")
print(athlete.loc[5])

print("Head and tail of all player names: ")
print(athlete["Name"])

print("\n\nPlayers from Nigeria: \n")
print(athlete[athlete['NOC'].isin(['NIG'])])