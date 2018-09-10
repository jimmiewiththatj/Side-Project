import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from player import Player

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.setFixedSize(500,500)
        self.setStyleSheet( 
    "QPushButton{ \n"
    "border-style: outset;\n"
    "border-width: 5px;\n"
    "border-radius: 10px;\n"
    "border-color: blue;\n"
    "font: 14px;\n"
    "padding: 6px;\n"
    "}\n"
    "QLabel{ \n"
    "font: 14px;\n"
    "}\n"
    ""
    
    )

        icon = QIcon()
        icon.addPixmap(QPixmap("images/title.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        
        title_label = QLabel()
        title_label.setPixmap(QPixmap("images/error.png"))
        title_button = QPushButton("Start")
        title_button.clicked.connect(self.handleStart)
        
        mainMenu = QVBoxLayout()
        mainMenu.addWidget(title_label)
        mainMenu.addWidget(title_button)
        mainMenu.setAlignment(Qt.AlignHCenter)

        wrapper = QWidget()
        wrapper.setLayout(mainMenu)

        self.setCentralWidget(wrapper)
        self.setGeometry(200, 200, 200, 400)
        self.setWindowTitle("Tic Tac Toe")
        self.show()

    def handleStart(self):
        
        self.setFixedSize(500,110)
        setupMenu = QFormLayout()
        self.textbox1 = QLineEdit()
        self.textbox2 = QLineEdit()
        button = QPushButton("Begin")
        button.clicked.connect(self.setUpBoard)

        setupMenu.addRow("Name of 1st Player", self.textbox1)
        setupMenu.addRow("Name of 2nd Player", self.textbox2)
        setupMenu.addRow(button)
        setupMenu.setAlignment(Qt.AlignHCenter)

        self.start_wrapper = QWidget()
        self.start_wrapper.setLayout(setupMenu)

        self.setCentralWidget(self.start_wrapper)

    def handlePlayer(self):
        
        row = int(self.row_enter.text())
        col = int(self.column_enter.text())
        
        if(self.turn%2 == 1):
            self.board_arr[row][col] = 1
        else:
            self.board_arr[row][col] = 2
        
        self.refresh()

    def refresh(self):

        board = QGridLayout()
        for i in range(3):
            for j in range(3):
                if self.board_arr[i][j] == 0:
                    label = QLabel()
                    label.setPixmap(QPixmap("images/default.png"))
                    board.addWidget(label, i, j)
                elif self.board_arr[i][j] == 1:
                    label = QLabel()
                    label.setPixmap(QPixmap("images/x.png"))
                    board.addWidget(label, i, j)
                else: 
                    label = QLabel()
                    label.setPixmap(QPixmap("images/o.png"))
                    board.addWidget(label, i, j)
        board.setAlignment(Qt.AlignHCenter)
        wrapper_board = QWidget()
        wrapper_board.setLayout(board)

        custom_label = ""
        if(self.turn%2 == 1):
            custom_label = "Turn " + str(self.turn) + " for "+ self.ply1 +", enter coordinates:"
        else:
            custom_label = "Turn " + str(self.turn) +" for "+ self.ply2 +", enter coordinates:"

        wrapper = QWidget()
        general = QVBoxLayout()
        if self.check_board(self.board_arr) == True:
            alt_plate = QHBoxLayout()
            if self.turn%2 == 1:
                alt_plate.addWidget(QLabel(self.ply1 + " has won"))
                
            else:
                alt_plate.addWidget(QLabel(self.ply2 + " has won"))
            again_button = QPushButton("Play Again!")
            again_button.clicked.connect(self.handleStart)
            alt_plate.addWidget(again_button)

            alt_wrapper = QWidget()
            alt_wrapper.setLayout(alt_plate)
            general.addWidget(wrapper_board)
            general.addWidget(alt_wrapper)
               
        else:
            wrapper_data = QWidget()
            wrapper_data.setLayout(self.data_plate)
            enter_plate = QVBoxLayout()
            enter_plate.addWidget(QLabel(custom_label))
            enter_plate.addWidget(wrapper_data)
            wrapper_enter = QWidget()
            wrapper_enter.setLayout(enter_plate)
            general.addWidget(wrapper_board)
            general.addWidget(wrapper_enter)
        
        wrapper.setLayout(general)
        self.setCentralWidget(wrapper)

        self.turn = self.turn + 1

    def setUpBoard(self):
        
        self.board_arr = [[0,0,0], [0,0,0], [0,0,0]]
        self.setFixedSize(500,500)

        self.row_enter = QLineEdit()
        self.column_enter = QLineEdit()
        nextButton = QPushButton("Next")
        nextButton.clicked.connect(self.handlePlayer)
        self.turn = 1

        self.data_plate = QHBoxLayout()
        self.data_plate.addWidget(QLabel("Rows: "))
        self.data_plate.addWidget(self.row_enter)
        self.data_plate.addWidget(QLabel("Column: "))
        self.data_plate.addWidget(self.column_enter)
        self.data_plate.addWidget(nextButton)

        self.ply1 = self.textbox1.text()
        self.ply2 = self.textbox2.text()

        self.refresh()
        
    
    def print_board(board):
        for i in range(3):
            line = "|"
            for j in range(3):
                line = line + str(board[i][j]) + "|"
            print("-------")
            print(line)   

    def check_board(self, board):
        # rows
        for i in range(3):
            if (board[i] == [1,1,1] or board[i] == [2,2,2]):
                return True

        #columns
        for i in range(3):
            if((board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1)
            or (board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2)):
                return True
    
        #diagonal
        if ((board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != 0)
        or (board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[1][1] != 0)):
            return True 

        return False
    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

