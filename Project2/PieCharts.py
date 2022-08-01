from matplotlib import pyplot as plt

continents = ["North America", "South America", "Europe", "Asia", "Africa"]
population = [57900000, 422000000, 741000000, 4463000000, 1216000000]
plt.pie(population, labels=continents, autopct="%1.1f%%") #f = fraction, 1.1 = 1 digit, %% percent 
plt.legend(continents)
plt.axis("equal") #aligned
plt.show()

