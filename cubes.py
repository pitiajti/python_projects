import matplotlib.pyplot as plt

input_values = list(range(1,5001))
squares = [_**2 for _ in range(1,5001)]
print(squares)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')