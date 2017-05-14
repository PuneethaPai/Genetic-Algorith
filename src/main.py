import matplotlib.pyplot as plt

from genetic_algorithm_app import StartApp

app = StartApp(population_size=300, kill_percentage=40, mutate_percentage=20)
result = app.run(target_string="I can do anything!!")
for item in result:
    print item[0], item[1]

x = xrange(len(result))
y = [item[1] for item in result]
plt.plot(x, y, linewidth=2.5)
plt.xlabel('Generation Number')
plt.ylabel('Fitness Value')
plt.show()
