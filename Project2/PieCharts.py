from matplotlib import pyplot as plt

continents = ["North America", "South America", "Europe", "Asia", "Africa"]
population = [57900000, 422000000, 741000000, 4463000000, 1216000000]
plt.pie(population)
plt.legend(continents)
plt.show()