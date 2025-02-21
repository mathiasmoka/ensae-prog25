from grid import Grid
from solver import *
import matplotlib.pyplot as plt

grid = Grid(4, 5)
print(grid)

data_path = "../input/"
#les deux points font un retour en arrière donc cela suppose que l'on est dans le dossier code
#pour executer le main, il faut donc se mettre dans le dossier code

file_name = data_path + "grid17.in"
grid = Grid.grid_from_file(file_name)
print(grid)

file_name = data_path + "grid17.in"
grid = Grid.grid_from_file(file_name, read_values=True)
print(grid)

solver = SolverEmpty(grid)
solver.run()
print("The final score of SolverEmpty is:", solver.score())

#Test de la fonction plot
print("\n Test de la fonction plot")
Grid.plot(grid)

#Test de la fonction cost
print("\n Test de la fonction cost")
res1 = Grid.cost(grid, ((1, 0), (1,1)))
print("res=", res1)

#Test de la fonction adjency
print("\n Test de la fonction adjency")
res2 = Grid.adjacency(grid, (2,3))
print("res=", res2)

#Test de la fonction all pairs
print("\n Test de la fonction all_pairs")
res3 = Grid.all_pairs(grid)
print("res=", res3)

#Test de la fonction solver
print("\n Test de la fonction solver")
solver = SolverGreedy(grid)
solver.run()
print("res=", solver)