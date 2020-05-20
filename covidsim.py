# CovidSim Version 1.0.5 (simulation.majorchange.minoredit)
# Jack Wang and Tim Fuller

# Inputs, and setting up variables

import matplotlib.pyplot as plt


def herd_immunity(r_nought_theoretical):
    if generation == 0:
        r_nought_effective = r_nought_theoretical * (total_pop - initial_infected)/total_pop
    else:
        r_nought_effective = r_nought_theoretical * ((total_pop - (sum_list(infected_by_generation))[generation - 1])
                                                     / total_pop)
    return r_nought_effective


def next_infected():
    # Function for calculating the spread from the previous generation
    if lenient_restrictions <= generation < heavy_restrictions:
        new_infected = infected_by_generation[generation - 1] * herd_immunity(r_nought_lenient)
        infected_by_generation.append(int(new_infected))
    elif generation >= heavy_restrictions:
        new_infected = infected_by_generation[generation - 1] * herd_immunity(r_nought_heavy)
        infected_by_generation.append(int(new_infected))
    else:
        new_infected = infected_by_generation[generation-1] * herd_immunity(r_nought)
        infected_by_generation.append(int(new_infected))


def generation_deaths():
    # Function for calculating the deaths from the previous generation
    new_dead = infected_by_generation[generation-1] * mortality_rate
    deaths_by_generation.append(int(new_dead))


def generation_recoveries():
    # Function for calculating the recoveries from the previous generation
    new_recovered = infected_by_generation[generation-1] * (1 - mortality_rate)
    recovered_by_generation.append(int(new_recovered))


def sum_list(ls):
    # Sum of list, where the value at index i is equal to the sum of all previous values (inclusive of current)
    listsum = []
    for i in range(len(ls)):
        count = 0
        for j in range(i):
            count += ls[j]
        # Lazy hotfix that works with no penalty
        count += ls[i]
        listsum.append(count)
    return listsum


initial_infected = int(input("How many people start infected? "))
r_nought = float(input("What is R nought? "))
total_pop = int(input("What is the population size? "))
mortality_rate: float = float(input("What is the mortality rate (decimal)? "))
number_of_generations = int(input("How many generations are to be run? "))
generation = 1
infected_by_generation = [initial_infected]
deaths_by_generation = [0]
recovered_by_generation = [0]
lenient_restrictions = int(input("How many generations until lenient restrictions are in place? "))
r_nought_lenient: float = float(input("What is R nought after lenient restrictions are enacted? "))
heavy_restrictions = int(input("How many generations until heavy restrictions are in place? "))
r_nought_heavy: float = float(input("What is R nought after heavy restrictions are enacted? "))

for i in range(number_of_generations):
    # Runs the actual sim
    next_infected()
    generation_deaths()
    generation_recoveries()
    generation += 1

# Gives results
print(infected_by_generation)
print(sum_list(infected_by_generation))
print(deaths_by_generation)
print(sum_list(deaths_by_generation))
print(recovered_by_generation)
print(sum_list(recovered_by_generation))

fig, ax = plt.subplots()
plot0 = plt.figure(1)
ax.plot(range(0, number_of_generations + 1), sum_list(infected_by_generation), "r--", label='Infected')
ax.plot(range(0, number_of_generations + 1), sum_list(deaths_by_generation), "k--", label='Deaths')
ax.plot(range(0, number_of_generations + 1), sum_list(recovered_by_generation), "b--", label='Recovered')
legend = ax.legend(loc='best', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')
plt.xlabel('Generations')
plt.ylabel('Population')

fig, ax = plt.subplots()
plot1 = plt.figure(2)
ax.plot(range(0, number_of_generations + 1), infected_by_generation, "r--", label='Infected')
ax.plot(range(0, number_of_generations + 1), deaths_by_generation, "k--", label='Deaths')
ax.plot(range(0, number_of_generations + 1), recovered_by_generation, "b--", label='Recovered')
legend = ax.legend(loc='best', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')
plt.xlabel('Generations')
plt.ylabel('Infected by Generation')
plt.show()
