class DeathBoard:

    def __init__(self,width=50,height=50,board=[[0 for i in range(50)]for i in range(50)]):

        self.board = board
        self.width = width
        self.height = height

    def next_generation(self):

        old_board = self.board
        new_board = generateBoard(width=self.width,height=self.height)

        for x in range(self.width):
            for y in range(self.height):

                X_neighbors = 0
                O_neighbors = 0
                total_neighbors = 0

                neighbors, neighbors_type = self.get_neighbors(x,y)

                for i,neighbor in enumerate(neighbors):
                    if neighbor:
                        total_neighbors += 1
                        if neighbors_type[i] == 'X':
                            X_neighbors += 1
                        else:
                            O_neighbors += 1                       

                new_board[x][y] = self.evolve(old_board[x][y],total_neighbors,O_neighbors,X_neighbors)
                
        self.board = new_board

    def evolve(self,old_cell,total_neighbors,O_neighbors,X_neighbors):

        new_cell = [False,0,0]

        if old_cell[0]:
            if (total_neighbors < 2) or (total_neighbors > 3):
                new_cell = [False,0,old_cell[2]]
            else:
                new_cell = [True,old_cell[1],old_cell[2]]

        elif total_neighbors == 3:
            if X_neighbors > O_neighbors:
                new_cell = [True,'X',old_cell[2]]
            else:
                new_cell = [True,'O',old_cell[2]]

        return new_cell

    def get_neighbors(self,x,y):
        
        neighbors = []
        neighbors_type = []

        neighboring_tiles = ((-1,-1),
                             (-1,0),
                             (-1,1),
                             (0,-1),
                             (0,1),
                             (1,-1),
                             (1,0),
                             (1,1))

        for i,j in neighboring_tiles:
            if ((x+i)%self.width != 0) and ((y+j)%self.height != 0):
                neighbors.append(self.board[x+i][y+j][0])
                neighbors_type.append(self.board[x+i][y+j][1])

        return neighbors, neighbors_type

    def update(self):

        self.evolve()

        return self.board
    
def generateBoard(width,height):

    return [[[False,0,0] for j in range(width)]for i in range(height)]