open(resources/budget_data.csv) as budget_data
array = np.loadtxt(budget_data, delimiter = ",")

print(array)