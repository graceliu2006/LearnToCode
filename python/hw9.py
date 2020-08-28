print("Question 1")


class Pagination(object):

    def __init__(self, items, pageSize):
        self.items = items
        self.pageSize = pageSize
        self.paginized_list = []
        self.current_page = 0

        self.paginize()
       

    def paginize(self):
        
        for k in range (0, 1+len(self.items) // self.pageSize):
            holder_list = []
            for i in range (k * self.pageSize, (k+1) * self.pageSize):
                if i < len(self.items):
                    holder_list.append(self.items[i]) 
            self.paginized_list.append(holder_list)
        
        print(self.paginized_list)

    def first_page(self):
        return(self.paginized_list[0])

    
    def last_page(self):
        return(self.paginized_list[len(self.paginized_list) - 1])
    
    def prev_page(self):
        if self.current_page >= 0:
            self.current_page -= 1
            return(self.paginized_list[self.current_page])
        else:
            print("You are at the first page already.")
    
    def next_page(self):
        if self.current_page <= len(self.paginized_list):
            self.current_page += 1
            return(self.paginized_list[self.current_page])
        else:
            print("You are at the last page already.")
    
    def go_to_page(self, page):
        self.current_page = page - 1
        return(self.paginized_list[page - 1])
        

alphabetList = "abcdefghijklmnopqrstuvwxyz"
test = Pagination(alphabetList, 4)


print("Question 2")


class Sudoku:

    def __init__(self, string):
        self.sudoku_string = list(string)
        self.matrix_board=[]
        for i in range(9):
            self.matrix_board.append(self.sudoku_string[9 * i : 9 * (i + 1)])
        self.board = self.get_board(self.sudoku_string)

    def get_board(self, list):
        for i in range(0,9):
            print(self.sudoku_string[9 * i : 9 * (i + 1)])
            

    def get_row(self, row):

        return self.sudoku_string[9 * (row-1) : 9 * row]

    def get_column(self, column):

        return self.sudoku_string[(column - 1) : (column - 1) + 81 : 9]

    def get_square(self, n, m = None):
        if m == None:
            x = self.determine_block(n) 
            y = (n % 3) * 3
        else:
            x = self.determine_block(n)
            y = self.determine_block(m)

        return self.get_block(x,y)

    def get_block(self, x, y):

        block = []
        
        for i in range (x, x+3):
            block.append(self.matrix_board[i][y:y+3])
        
        return block

    def determine_block(self, n):

        return n // 3 * 3
        if n in range(3):
            return 0
        elif n in range(3,6): 
            return 3
        else:
            return 6
    
game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

# print(game.get_row(2))
# print(game.get_column(2))
#game.board
print("*"*80)
print(game.get_square(2,5))

