from constraint import *


def map_coloring():
    problem = Problem()


    # Define the variables (regions)
    regions = ['A', 'B', 'C', 'D']
    problem.addVariables(regions, ['red', 'green', 'blue'])


    # Define the constraints (adjacent regions cannot have the same color)
    problem.addConstraint(AllDifferentConstraint(), ['A', 'B'])
    problem.addConstraint(AllDifferentConstraint(), ['A', 'C'])
    problem.addConstraint(AllDifferentConstraint(), ['B', 'C'])
    problem.addConstraint(AllDifferentConstraint(), ['B', 'D'])
    problem.addConstraint(AllDifferentConstraint(), ['C', 'D'])


    # Get and print solutions
    solutions = problem.getSolutions()
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")


map_coloring()
