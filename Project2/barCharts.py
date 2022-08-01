from matplotlib import pyplot as plt

days = [1,2,3,4,5,6,7]
day_temperature = [27,34,30,38,25,21,29]
night_tem = [20,27,25,32,21,16,23]
plt.bar(days, day_temperature)
plt.bar(days, night_tem)
plt.title("Temperature Record of the Last Week\n")
plt.xlabel("\nDays")
plt.ylabel("\nTemperature (C)")
plt.legend(["Day", "Night"])
plt.show()