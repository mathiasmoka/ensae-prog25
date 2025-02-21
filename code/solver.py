class Solver:
    """
    A solver class. 

    Attributes: 
    -----------
    grid: Grid
        The grid
    pairs: list[tuple[tuple[int]]]
        A list of pairs, each being a tuple ((i1, j1), (i2, j2))
        List de couples de couples
    """

    def __init__(self, grid):
        """
        Initializes the solver.

        Parameters: 
        -----------
        grid: Grid
            The grid
        """
        self.grid = grid
        self.pairs = list()

    def score(self):
        """
        Computes the of the list of pairs in self.pairs
        """
        # On ne prends pas en compte les cases non appariées dans le calcul du score ci-dessous
        # --> il faudra donc faire un système qui prends la liste de toutes les cases de la grille, et enlève au fur et à mesure toutes les cases apartenant à des couples
        # ==> à la fin on somme les valeurs des cases restantes dans la liste
        #  
        s = 0
        for p in self.pairs :
            i0, j0 = p[0]
            i1, j1 = p[1]
            value: list[list[int]]
            s += abs(value[i1][j1] - value[i0][j0])
        return s

class SolverEmpty(Solver):
    def run(self):
        pass

class SolverGreedy(Solver):
    def run(self):
        pass
    
    def solver(self) :

        #POUR GARDER EN MEMOIRE LES CASES DEJA APPARIES
        D = {}    
        for i in range(Solver.grid.n) :
            for j in range(Solver.grid.m) :
                D[(i, j)] = 0
        # les clés de D sont les couples de coordonnes de TOUTES les cases de la grille
        # 0 : la case n'a pas été appariée à une autre case --> on sommera la valeur de cette case
        # 1 : la case a été appariée à une autre case --> on sommera la différence de valeurs entre elle et sa case couplée
        # les "-->" serviront au calcul du score, en utilisant la fonction score telle que codée plus haut (sans prendre 
        # en compte les cases seules, qu'il faut donc traiter à part)
        
        # APPARIEMMENT DES CASES !
        L = all_pairs()
        
        # tri par coût croisssant
        c = 1
        while c > 0 :
            c = 0
            for i in range (0, len(L) - 1) :
                c1 = Solver.grid.cost(Solver.grid, L[i])
                c2 = Solver.grid.cost(Solver.grid, L[i+1])
                if c1 > c2 :
                    c += 1
                    v = L[i]
                    L[i] = L[i+1]
                    L[i+1] = v

        # selection des matchs
        M = []
        for m in range (0, len(L)) :
            if D[m[0]] == 0 and D[m[1]] == 0 :
                M.append(m)
                D[m[0]] = 1
                D[m[1]] = 1

        #BONUS : Calcul du score
        s = SloverGreedy.score()
        for e in D :
            if D[e] != 1 :
                i, j = e[0], e[1]
                s += value[i][j]

        print(M, s)
        return (M,s)

