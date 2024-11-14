import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv('pokemon_data.csv')

def scatterplot():
    plt.figure(figsize=(8,5))

    x = pokemon.loc[pokemon['Type 1'] == 'Fire']['Sp. Atk']
    y = pokemon.loc[pokemon['Type 1'] == 'Fire']['Attack']

    plt.scatter(x,y,color='blue')
    plt.title("Attack and Sp. Atk for Fire Type 1 Pokemon")
    plt.xlabel("Sp. Atk")
    plt.ylabel("Attack")

    plt.show()

def main():
    scatterplot()

if __name__ == "__main__":
    main()