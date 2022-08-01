from matplotlib import pyplot as plt

continents = ["North America", "South America", "Europe", "Asia", "Africa"]
population = [57900000, 422000000, 741000000, 4463000000, 1216000000]
explode = (0,0,0.1,0,0) #isolate
plt.pie(population, labels=continents, autopct="%1.1f%%", explode = explode) #f = fraction, 1.1 = 1 digit, %% percent 
#plt.pie(population, labels=continents, autopct="%1.1f%%", startangle=45) #change position
plt.legend(continents)
plt.axis("equal") #aligned
plt.show()

