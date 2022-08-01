from matplotlib import pyplot as plt

months = [1,2,3]
income1 = [1000, 4000, 10000]
income2 = [2000, 3000, 4000]
plt.plot(months, income1, marker = 'o')
plt.plot(months, income2, marker="o")
plt.title("Income of Company 1 & Company 2\n")
plt.xlabel("\nMonths")
plt.ylabel("Income\n")
plt.legend(["Company 1", "Company 2"])
plt.grid()
plt.show()