"""
This is the grid module. It contains the Grid class and its associated methods.
"""

class Grid():
    """
    A class representing the grid. 

    Attributes: 
    -----------
    n: int
        Number of lines in the grid
    m: int
        Number of columns in the grid
    color: list[list[int]]
        The color of each grid cell: value[i][j] is the value in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..n-1 and columns are numbered 0..m-1.
    value: list[list[int]]
        The value of each grid cell: value[i][j] is the value in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..n-1 and columns are numbered 0..m-1.
    colors_list: list[char]
        The mapping between the value of self.color[i][j] and the corresponding color
    """
    

    def __init__(self, n, m, color=[], value=[]):
        """
        Initializes the grid.

        Parameters: 
        -----------
        n: int
            Number of lines in the grid
        m: int
            Number of columns in the grid
        color: list[list[int]]
            The grid cells colors. Default is empty (then the grid is created with each cell having color 0, i.e., white).
        value: list[list[int]]
            The grid cells values. Default is empty (then the grid is created with each cell having value 1).
        
        The object created has an attribute colors_list: list[char], which is the mapping between the value of self.color[i][j] and the corresponding color
        """
        self.n = n
        self.m = m
        if not color:
            color = [[0 for j in range(m)] for i in range(n)]            
        self.color = color
        if not value:
            value = [[1 for j in range(m)] for i in range(n)]            
        self.value = value
        self.colors_list = ['w', 'r', 'b', 'g', 'k']

    def __str__(self): 
        """
        Prints the grid as text.
        """
        output = f"The grid is {self.n} x {self.m}. It has the following colors:\n"
        for i in range(self.n): 
            output += f"{[self.colors_list[self.color[i][j]] for j in range(self.m)]}\n"
        output += f"and the following values:\n"
        for i in range(self.n): 
            output += f"{self.value[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: n={self.n}, m={self.m}>"

    def plot(self): 
        """
        Plots a visual representation of the grid.
        """
        import matplotlib.pyplot as plt

        # Taille de la grille
        rows, cols = self.n, self.m
        print(rows, cols)

        fig, ax = plt.subplots()
        ax.set_xticks([i for i in range(cols + 1)], minor=False)
        ax.set_yticks([i for i in range(rows + 1)], minor=False)
        plt.grid()

        # Affichage des valeurs dans la grille
        tab = self.value
        for i in range(rows):
            for j in range(cols):
                if self.color[i][j] == 0:
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color='w'))
                elif self.color[i][j] == 1:
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color='r'))
                elif self.color[i][j] == 2:
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color='b'))
                elif self.color[i][j] == 3:
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color='g'))
                elif self.color[i][j] == 4:
                    ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color='k'))
                ax.text(j + 0.5, i + 0.5, str(tab[i][j]), 
                        va='center', ha='center', fontsize=14)

        plt.gca().invert_yaxis() 
        plt.show()


    def is_forbidden(self, i, j):
        """
        Returns True is the cell (i, j) is black and False otherwise
        """
        return (self.color[i][j] == 4)

    def cost(self, pair):
        """
        Returns the cost of a pair
 
        Parameters: 
        -----------
        pair: tuple[tuple[int]]
            A pair in the format ((i1, j1), (i2, j2))

        Output: 
        -----------
        cost: int
            the cost of the pair defined as the absolute value of the difference between their values
        """
        # TODO
        c = abs(self.value[pair[0][0]][pair[0][1]] - self.value[pair[1][0]][pair[1][1]])
    
        return c

    def adjacency (self, position) :
        """
        position is a couple of values. Ex : (2,3)
        """
        i, j = position
        L = []
        if i>0 :
            L.append(((i, j),(i-1, j)))
        if i < self.n-1 :
            L.append(((i, j),(i+1,j)))
        if j>0 :
            L.append(((i, j),(i, j-1)))
        if j < self.m-1 :
            L.append(((i, j),(i, j+1)))
        return L

    
    def colors_checker (self, positions) :
        """
        positions is a list of a couple of values
        """
        Lc = []
        for e in positions :
            c = 0 #c is a checker. If the couple is legal, c=1 after the tests
            (i1, j1), (i2, j2) = e[0], e[1]
            if not self.is_forbidden(i1, j1) and not self.is_forbidden(i2, j2) :
                #if we passed the test, any cell is black
                #then, we have different possible combinations of colors
                if self.color[i1][j1] == 0 or self.color[i2][j2] == 0 :
                    c = 1
                elif (self.color[i1][j1] == 1 or self.color[i1][j1] == 1) and self.color[i2][j2] < 3 :
                    c = 1
                elif self.color[i1][j1] == 3 and (self.color[i2][j2] == 3 or self.color[i2][j2] == 0) :
                    #this test could be shorter, as only the number 3 color remains for the cell [i1][j1]
                    #and the case were [i2][j2] is white has already been processed with the first test 
                    #of the loop
                    c = 1
            if c == 1 :
                Lc.append(e)
        return Lc

    def all_pairs(self):
        """
        Returns a list of all pairs of cells that can be taken together. 
        Outputs a list of tuples of tuples [(c1, c2), (c1', c2'), ...] where each cell c1 etc. is itself a tuple (i, j)
        """
        L = []
        for i in range (0, self.n) :
            for j in range (0, self.m) :
                Li = self.colors_checker (self.adjacency ((i,j))) 
                for e in Li :
                    L.append(e)
        return L

    @classmethod
    def grid_from_file(cls, file_name, read_values=False): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters:
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "n m" 
            - next n lines contain m integers that represent the colors of the corresponding cell
            - next n lines [optional] contain m integers that represent the values of the corresponding cell
        read_values: bool
            Indicates whether to read values after having read the colors. Requires that the file has 2n+1 lines

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            color = [[] for i_line in range(n)]
            for i_line in range(n):
                line_color = list(map(int, file.readline().split()))
                if len(line_color) != m: 
                    raise Exception("Format incorrect")
                for j in range(m):
                    if line_color[j] not in range(5):
                        raise Exception("Invalid color")
                color[i_line] = line_color

            if read_values:
                value = [[] for i_line in range(n)]
                for i_line in range(n):
                    line_value = list(map(int, file.readline().split()))
                    if len(line_value) != m: 
                        raise Exception("Format incorrect")
                    value[i_line] = line_value
            else:
                value = []

            grid = Grid(n, m, color, value)
            return grid

        def matachable(self, case) :
                # pourra être utile à créer si on veut éviter de prendre le e[0] vu que la fonction colors checkers
                # conçue initialement pour all_pairs renvoie la liste des COUPLES de cases ((i, j), (.., ...))
            return ()
        
        def gridToGraph (self) :
            # les cases blanches sont les celles dont la somme des indices est paires
            G = {}
            for i in range (self.n) :
                for j in range(self.m) : 
                    G[(i,j)] = []
                    M = self.colors_checker (self.adjacency ((i,j))) 
                    for e in Li :
                        G[(i,j)].append(e[0])
                return G

        def fulkerson(self) :
            G = gridToGraph() 
            # Piorisation des matchs
            for e in G :
                pour = eviter_les_bugs

            # ajout des matchs
            M = []
            
            return M

"""
---------------------------------------------------------------------------
Remarques en TP
---------------------------------------------------------------------------

class Grid
    def __init__ (self, p1, p2, p3)
        self.var1 = ...
        self.var2 = ...
    def is_forbidden(self, i, j)
        ...

    grid = Grid (p1, p2, p3)

------------------
-- Comment appeler self.var1 de grid ?
    grid.var1

-- Comment appeler une fonction ?
    grid.is_forbidden(i, j)
------------------
-- Pour appeler des attributs dans une classe, il faut absolument mettre self. ...

------------------------------------------------
Structures de données
------------------------------------------------
- listes : création, ajout, supprimer, accès indice
- set
[la suite sur ma feuille]




"""