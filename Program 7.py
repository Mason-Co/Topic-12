import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv('pokemon_data.csv')


def scatterplot():
    plt.figure(figsize=(8, 5))

    x = pokemon.loc[pokemon['Type 1'] == 'Fire']['Sp. Atk']
    y = pokemon.loc[pokemon['Type 1'] == 'Fire']['Attack']

    plt.scatter(x, y, color='blue')
    plt.title("Attack and Sp. Atk for Fire Type 1 Pokemon")
    plt.xlabel("Sp. Atk")
    plt.ylabel("Attack")

    plt.show()


def linegraph():
    fire = pokemon['Type 1'] == 'Fire'
    water = pokemon['Type 1'] == 'Water'
    grass = pokemon['Type 1'] == 'Grass'

    plt.figure(figsize=(8, 5))

    plt.title("Amount of Primary Fire, Grass, and Water Types Added Over Generations")

    plt.plot(pokemon[fire]['Generation'].unique(),
             pokemon[fire]['Generation'].value_counts(), 'r.-', label='Fire', )
    plt.plot(pokemon[water]['Generation'].unique(),
             pokemon[water]['Generation'].value_counts(), 'b.-', label='Water')
    plt.plot(pokemon[grass]['Generation'].unique(),
             pokemon[grass]['Generation'].value_counts(), 'g.-', label='Grass')
    plt.xlabel("Generation")
    plt.ylabel("Number of Pokemon")

    plt.legend()

    plt.show()


def histogram():
    plt.figure(figsize=(8,5))
    bins = [0,25,50,75,100,125,150,175,200,225,255]
    plt.hist(pokemon.HP, bins=bins)

    plt.ylabel("Number of Pokemon")
    plt.xlabel("Hit Points (HP)")
    plt.xticks(bins)

    plt.show()


def piechart():
    plt.figure(figsize=(8,5))
    fire = pokemon[(pokemon['Type 1'] == 'Fire')].count()[0]
    water = pokemon[(pokemon['Type 1'] == 'Water')].count()[0]
    grass = pokemon[(pokemon['Type 1'] == 'Grass')].count()[0]
    bug = pokemon[(pokemon['Type 1'] == 'Bug')].count()[0]
    normal = pokemon[(pokemon['Type 1'] == 'Normal')].count()[0]
    flying = pokemon[(pokemon['Type 1'] == 'Flying')].count()[0]
    fighting = pokemon[(pokemon['Type 1'] == 'Fighting')].count()[0]
    fairy = pokemon[(pokemon['Type 1'] == 'Fairy')].count()[0]
    dragon = pokemon[(pokemon['Type 1'] == 'Dragon')].count()[0]
    poison = pokemon[(pokemon['Type 1'] == 'Poison')].count()[0]
    ice = pokemon[(pokemon['Type 1'] == 'Ice')].count()[0]
    ground = pokemon[(pokemon['Type 1'] == 'Ground')].count()[0]
    ghost = pokemon[(pokemon['Type 1'] == 'Ghost')].count()[0]
    dark = pokemon[(pokemon['Type 1'] == 'Dark')].count()[0]
    electric = pokemon[(pokemon['Type 1'] == 'Electric')].count()[0]
    other = pokemon[(pokemon['Type 1'] != 'Fire')
                    & (pokemon['Type 1'] != 'Water')
                    & (pokemon['Type 1'] != 'Grass')
                    & (pokemon['Type 1'] != 'Bug')
                    & (pokemon['Type 1'] != 'Normal')
                    & (pokemon['Type 1'] == 'Flying')
                    & (pokemon['Type 1'] == 'Fighting')
                    & (pokemon['Type 1'] == 'Fairy')
                    & (pokemon['Type 1'] == 'Dragon')
                    & (pokemon['Type 1'] == 'Poison')
                    & (pokemon['Type 1'] == 'Ice')
                    & (pokemon['Type 1'] == 'Ground')
                    & (pokemon['Type 1'] == 'Ghost')
                    & (pokemon['Type 1'] == 'Dark')
                    & (pokemon['Type 1'] == 'Electric')].count()[0]
    types = [fire, water, grass, bug, normal, flying, fighting, fairy,
             dragon, poison, ice, ground, ghost, dark, electric, other]
    labels = ['Fire', 'Water', 'Grass', 'Bug', 'Normal', 'Flying', 'Fighting', 'Fairy',
              'Dragon', 'Poison', 'Ice', 'Ground', 'Ghost', 'Dark', 'Electric', 'Other']
    colors = ['red', 'blue', 'green', 'yellowgreen', 'silver', 'lightskyblue', 'darkred',
              'violet', 'mediumslateblue', 'blueviolet', 'cyan', 'sienna', 'rebeccapurple',
              'dimgrey', 'yellow', 'lightgrey']

    plt.pie(types, labels=labels, colors=colors, autopct='%.2f %%', pctdistance=0.8)

    plt.show()


def box():
    bst = pokemon['BST'] = (pokemon['HP'] + pokemon['Attack'] + pokemon['Defense'] +
                            pokemon['Sp. Atk'] + pokemon['Sp. Def'] + pokemon['Speed'])
    plt.style.use('default')

    plt.figure(figsize=(6,8))

    gen1 = pokemon.loc[(pokemon.Generation == 1) & (pokemon.Legendary == True)]['BST']
    gen2 = pokemon.loc[(pokemon.Generation == 2) & (pokemon.Legendary == True)]['BST']
    gen3 = pokemon.loc[(pokemon.Generation == 3) & (pokemon.Legendary == True)]['BST']
    gen4 = pokemon.loc[(pokemon.Generation == 4) & (pokemon.Legendary == True)]['BST']
    gen5 = pokemon.loc[(pokemon.Generation == 5) & (pokemon.Legendary == True)]['BST']
    gen6 = pokemon.loc[(pokemon.Generation == 6) & (pokemon.Legendary == True)]['BST']

    labels = ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6']

    boxes = plt.boxplot([gen1, gen2, gen3, gen4, gen5, gen6], tick_labels=labels)

    for box in boxes['boxes']:
        box.set(color='#4286f4')

    plt.title("Base Stat Totals of Legendary Pokemon in Each Generation")
    plt.ylabel("Base Stat Total (BST)")

    plt.show()


def main():
    graph = int(input("Choose Graph: "
                      "\n1-Scatter plot"
                      "\n2-Line graph"
                      "\n3-Histogram"
                      "\n4-Pie chart"
                      "\n5-Box plot"))
    if graph == 1:
        scatterplot()
    elif graph == 2:
        linegraph()
    elif graph == 3:
        histogram()
    elif graph == 4:
        piechart()
    elif graph == 5:
        box()


if __name__ == "__main__":
    main()
