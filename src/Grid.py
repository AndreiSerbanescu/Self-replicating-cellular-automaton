from src import settings
from src.RuleInitialiser import *
from src.Cell import *
from src.Position import *

class Grid:

    def __init__(self):

        self.size = (settings.COLNO, settings.ROWNO)
        self.cells = [[Cell(Position(y, x)) for x in range(self.size[1])] \
                      for y in range(self.size[0])]

        self.next_state = [[0 for x in range(self.size[1])] \
                      for y in range(self.size[0])]

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.cells[i][j] == Cell(Position(i, j))


        self.rule_dict = RuleInitialiser("rules.txt").generate_dict()

        self.__init__loop()

        self.changed_cells = []


    def update(self):
        self.__generate_next_step()
        self.__set_next_step()


    def __generate_next_step(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                #print(self.__get_neighbours(i, j))

                config = str(self.cells[i][j].state.value) + self.__get_neighbours(i, j)
                next_state_value = self.rule_dict.get(config)
                if next_state_value == None:
                    self.next_state[i][j] = self.cells[i][j].state
                else:
                    self.next_state[i][j] = State(int(next_state_value))
                    self.changed_cells.append(self.cells[i][j])



    def __set_next_step(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.cells[i][j].state = self.next_state[i][j]


    def __get_neighbours(self, x, y):
        #FORMAT NESW
        result = ""
        cellNorth = self.__get_cell(x, y - 1)
        cellEast = self.__get_cell(x + 1, y)
        cellSouth = self.__get_cell(x, y + 1)
        cellWest = self.__get_cell(x - 1, y)

        result += str(cellNorth.state.value)
        result += str(cellEast.state.value)
        result += str(cellSouth.state.value)
        result += str(cellWest.state.value)

        return result

    def __get_cell(self, i, j):
        if i == -1:
            x = settings.COLNO - 1
        elif i == settings.COLNO:
            x = 0
        else:
            x = i

        if j == -1:
            y = settings.ROWNO - 1
        elif j == settings.ROWNO:
            y = 0
        else:
            y = j

        return self.cells[x][y]

    def render(self, screen):

        for cell in self.changed_cells:
            cell.render(screen)

        self.changed_cells.clear()


    def __init__loop(self):
        xoffset = settings.COLNO // 2 - 15
        yoffset = settings.ROWNO // 2 - 15

        langtonLoop = [
            " 22222222",\
             "2170140142",\
             "2022222202",\
             "272    212",\
             "212    212",\
             "202    212",\
             "272    212",\
             "21222222122222",\
             "207107107111112",\
             " 2222222222222"]


        for i in range(len(langtonLoop)):
            for j in range(len(langtonLoop[i])):
                if langtonLoop[i][j] == " ":
                    index = 0
                else:
                    index = int(langtonLoop[i][j])
                self.cells[xoffset + j][yoffset + i].state = State(index)

