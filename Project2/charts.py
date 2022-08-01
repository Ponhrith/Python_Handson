from matplotlib import pyplot as plt

months = [1,2,3]
income1 = [1000, 4000, 10000]
income2 = [3000, 2000, 7000]
plt.plot(months, income1)
plt.plot(months, income2)
plt.title("Income of Company 1 & Company 2\n")
plt.xlabel("\nMonths")
plt.ylabel("Income\n")
plt.show()