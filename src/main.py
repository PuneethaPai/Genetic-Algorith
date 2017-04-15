import string
import matplotlib.pyplot as plt

from dna import DNA
from generation import Generation
from nucleotides import Nucleotides
from population import Population
from population_initialise import PopulationInitialise

target = DNA("I can do anything!!")
target_length = len(target.structure)
nucleotides = Nucleotides(string.letters + ') -!;')
DNA.nucleotides = nucleotides
Population.kill_percentage = 50
Population.mutate_percent = 50
population_initialise = PopulationInitialise(nucleotides)

first_population = population_initialise.create(population_size=150, structure_size=target_length)

generations = [Generation(number=1, population=first_population)]

iteration = 0
while True:
    if generations[-1].population.people[0] == target:
        break
    generations.append(generations[-1].next_generation(target))
    print "Generation : %d Best Fit :%s" % (iteration, generations[-1].population.people[0].structure)
    iteration += 1

print iteration, generations[-1].population.people[0].structure

x = xrange(iteration)
y = [generation.population.fitness[0] for generation in generations[:-1]]

plt.plot(x, y, linewidth=2.0)
plt.xlabel('Generation Number')
plt.ylabel('Fitness Value')
plt.show()
