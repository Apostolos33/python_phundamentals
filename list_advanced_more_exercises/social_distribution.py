population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
not_equal_distribution_possible = False




for index in range(len(population)):
    bigest_number = max(population)
    index_biggest_number = population.index(bigest_number)
    if population[index] < minimum_wealth:
        wage_needed = minimum_wealth - population[index]
        if (bigest_number - wage_needed) >= minimum_wealth:
            population[index_biggest_number] -= wage_needed
            population[index] += wage_needed
        

for wage in population:
    if wage < minimum_wealth:
        not_equal_distribution_possible = True

if not_equal_distribution_possible:
    print("No equal distribution possible")
else:
    print(population)


