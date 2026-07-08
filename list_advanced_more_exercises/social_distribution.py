population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
not_equal_distribution_possible = False
index = 0

for wage in population:
    if wage < minimum_wealth:
        wage_needed = minimum_wealth - wage
        if (population[-1] - minimum_wealth) >= minimum_wealth:
            population[-1] -= wage_needed
            population[index] += wage_needed
    
        else:
            population[-2] -= wage_needed
            population[index] += wage_needed
    index += 1

for wage in population:
    if wage < minimum_wealth:
        not_equal_distribution_possible = True

if not_equal_distribution_possible:
    print("No equal distribution possible")
else:
    print(population)


