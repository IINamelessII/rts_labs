"""Genetic Algorithm usage"""

from datetime import datetime
from itertools import combinations
from random import sample, randint


def diophantine(*coefficients, y, population_size=5):
	if len(coefficients) != 4:
		raise Exception(
			'Please, enter proper amount of coefficients or leave blank to generate randomly'
		)

	a, b, c, d = coefficients
	print(
		f'Equation is: {a if a > 1 else ""}x1 + {b if b > 1 else ""}x2 + {c if c > 1 else ""}x3 + {d if d > 1 else ""}x4 = {y}\n'
	)

	old_population = [sample(range(0, 100), 4) for i in range(population_size)]
	still_no_root = True
	total_crossovers = 0
	total_mutations = 0
	while still_no_root:
		old_pop_scores = fitness_function(old_population, coefficients, y)

		if 0 in old_pop_scores:
			answer = old_population[old_pop_scores.index(0)]
			return answer, total_crossovers, total_mutations

		else:
			new_population = crossover(old_population, population_size, old_pop_scores)
			new_pop_scores = fitness_function(new_population, coefficients, y)

			old_pop_median_score = sum(old_pop_scores) / len(old_pop_scores)
			new_pop_median_score = sum(new_pop_scores) / len(new_pop_scores)

			if new_pop_median_score < old_pop_median_score:
				old_population = new_population
				total_crossovers += 1
			else:
				old_population = mutated(old_population, y, total_mutations)
				total_mutations += 1


def fitness_function(population, coefficients, goal):
	deltas_of_population = []
	for roots in population:
		result = 0
		for root, coefficient in zip(roots, coefficients):
			result += coefficient * root
		delta = abs(goal - result)
		deltas_of_population.append(delta)

	return deltas_of_population


def crossover(population, population_size, scores):
	population_with_scores = list(zip(population, scores))
	possible_mates = list(combinations(population_with_scores, 2))
	possible_mates.sort(key=lambda value: (value[0][1] + value[1][1]) / 2)
	possible_mates = possible_mates[:population_size]

	new_population = []
	for mating in possible_mates:
		crossover_point = randint(1, len(population[0]) - 1)
		new_pop = mating[0][0][:crossover_point] + mating[1][0][crossover_point:]
		new_population.append(new_pop)

	return new_population


def mutated(population, goal, mutation_index):
	mutated_population = []
	for roots in population:
		mutated_roots = roots
		mutation_indexes = sample(
			[i for i in range(len(roots))], 1 + round(3 * mutation_index / 150)
		)
		for index in mutation_indexes:
			mutated_roots[index] = mutated_roots[index] + randint(-goal // 4, +goal // 4)

		mutated_population.append(mutated_roots)

	return mutated_population


def output_result(roots, coefficients):
	x1, x2, x3, x4 = roots
	print(f'Answer is:\n x1 = {x1}\n x2 = {x2}\n x3 = {x3}\n x4 = {x4}\n')

	result = 0
	res_str = ''
	for root, coef in zip(roots, coefficients):
		result += coef * root
		res_str += f'{coef}*{root} + '

	res_str += '= '
	for root, coef in zip(roots, coefficients):
		res_str += f'{coef * root} + '
	print(f'{res_str}= {result}\n')


if __name__ == '__main__':
	coefficients = [randint(-10, 10) for i in range(4)]

	start = datetime.now()
	final_result, crossovers_num, mutate_num = diophantine(*coefficients, y=100)
	finish = datetime.now()

	output_result(final_result, coefficients)
	print(f'Algorithm execution time: {(finish - start).microseconds}mcs\nCrossovers executed: {crossovers_num}\nMutations executed: {mutate_num}')
