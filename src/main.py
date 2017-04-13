import string

from dna import DNA
from generation import Generation
from nucleotides import Nucleotides
from population import Population
from population_initialise import PopulationInitialise

target = DNA("Puneeth did Implement!!")
target_length = len(target.structure)
nucleotides = Nucleotides(string.letters + ' !')
DNA.nucleotides = nucleotides
Population.kill_percentage = 50
Population.mutate_percent = 10
population_initialise = PopulationInitialise(nucleotides)

first_population = population_initialise.create(population_size=150, structure_size=target_length)

generations = [Generation(number=1, population=first_population)]

for i in xrange(1000):
    if generations[-1].population.people[0] == target:
        break
    generations.append(generations[-1].next_generation(target))
    print "Generation : %d Best Fit :%s, %s, %s" %(i, generations[-1].population.people[0].structure, generations[-1].population.people[1].structure, generations[-1].population.people[2].structure)

print i, generations[-1].population.people[0].structure
