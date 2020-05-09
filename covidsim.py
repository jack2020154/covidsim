# CovidSim Version 0.1.0 (release.simulation.edit)
# Jack Wang and Tim Fuller

# Inputs, and setting up variables
initial_infected = int(input("How many people start infected? "))
r_nought = float(input("What is R nought? "))
total_pop = int(input("What is the population size? "))
mortality_rate: float = float(input("What is the mortality rate (decimal)? "))
number_of_generations = int(input("How many generations are to be run? "))
generation = 1
infected_by_generation = [initial_infected]
deaths_by_generation = [0]
recovered_by_generation = [0]


def next_infected():
    # Function for calculating the spread from the previous generation
    new_infected = infected_by_generation[generation-1] * r_nought
    infected_by_generation.append(int(new_infected))


def generation_deaths():
    # Function for calculating the deaths from the previous generation
    new_dead = infected_by_generation[generation-1] * mortality_rate
    deaths_by_generation.append(int(new_dead))


def generation_recoveries():
    # Function for calculating the recoveries from the previous generation
    new_recovered = infected_by_generation[generation-1] * (1 - mortality_rate)
    recovered_by_generation.append(int(new_recovered))


for i in range(number_of_generations):
    next_infected()
    generation_deaths()
    generation_recoveries()
    generation += 1

print(infected_by_generation)
print(deaths_by_generation)
print(recovered_by_generation)
