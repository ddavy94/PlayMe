
##Creates dictionary representation of 6X7 connect4 gameboard with keys representing row number and values representing lists
connect4 = {}
for i in range(6):
    connect4[i] = [0,0,0,0,0,0,0]


#checks if board column is full
def checkFull(inp,gameboard):
    for i in range(6):
         if gameboard[i][inp] == 0:
            return False
    return True

#allows user to select a move based on user input that corresponds to the column number
def makeMove(usr,gameboard):
    inp = -1
    x = ""
    while not 0 <= inp <= 7:
        try:
            inp = int(input('Where would you like to go?: ')) - 1
        except ValueError:
            print(' ')
        except IndexError:
            print('')
        if not 0 <= inp <= 7:
            print('Please enter an integer between 1 and 7')
        elif checkFull(inp,gameboard):
            inp = -1
            print('This column is full, please try again')
    for i in range(6):
        if gameboard[i][inp] == 0:
            if usr == 1:
                gameboard[i][inp] = 1
            elif usr == 2:
                gameboard[i][inp] = 2
            break

#generates string representation of gameboard
def showTable(gameboard):
    for i in range(5,-1,-1):
        for e in range(7):
            if gameboard[i][e] == 1:
                print(' X  ',end="")
            elif gameboard[i][e] == 2:
                print(' 0  ',end="")
            else:
                print(' -  ',end="")
        print('\n',end="")
    print('___________________________')
    print('|1| |2| |3| |4| |5| |6| |7|')


##looks for winning row in gameboard
def checkRow(gameboard):
    for x in range(6):
        row = gameboard[x]
        y = 3
        for x in range(4):
            y = y + 1
            if row[x:y]  == [1,1,1,1]:
                return 1
            elif row[x:y] == [2,2,2,2]:
                return 2


##looks for winning column in gameboard
def checkClm(gameboard):
    for u in range(7):
        a = 0
        b = 4
        list = []
        for t in range(6):
            list.append(gameboard[t][u])
        while a < 4:
            if list[a:b] == [1,1,1,1]:
                return 1
            elif list[a:b] == [2,2,2,2]:
                return 2
            a = a+1
            b = b+1

#appends each 4-symbol diagnol sequence in gameboard to a least and searches for a winning pattern
def checkDiag(gameboard):
    list1 = []
    for a in range(3):
        r = a
        for b in range(4):
            a = r
            t = True
            list = []
            while t:
                try:
                    list.append(gameboard[a][b])
                    a = a + 1
                    b = b + 1
                except KeyError:
                    t = False
                except IndexError:
                    t = False
            list1.append(list)
            t = True
    for a in range(3):
        r = a
        for b in range(6, 2, -1):
            a = r
            t = True
            list = []
            while t and b >= 0:
                try:
                    list.append(gameboard[a][b])
                    a = a + 1
                    b = b - 1
                except KeyError:
                    t = False
                except IndexError:
                    t = False
            list1.append(list)
            t = True
    for diag in list1:
        for a in range(3):
            b = a + 4
            try:
                if diag[a:b] == [1,1,1,1]:
                    return 1
                    break
                elif diag[a:b] == [2,2,2,2]:
                    return 2
                    break
            except IndexError:
                z = ''




##game starts here
print('Welcome to Connect Four')
showTable(connect4)

user1 = input('[User 1] Please enter your name:')
user2 = input('[User 2] Please enter your name:')


while True:
    print('\nGo get em %s!!' % (user1))
    makeMove(1,connect4)
    showTable(connect4)
    if checkClm(connect4) == 1 or checkRow(connect4) == 1 or checkDiag(connect4) == 1:
        print('\n%s Wins!!!'%(user1))
        break
    if True:
        print('\nYou got this, show em how it''s done %s'%(user2))
        makeMove(2,connect4)
        showTable(connect4)
        if checkClm(connect4) == 2 or checkRow(connect4) == 2 or checkDiag(connect4) == 2:
            print('\n%s Wins!!!'%(user2))
            break






