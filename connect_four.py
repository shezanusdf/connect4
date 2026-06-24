positions = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def main():
    drawBoard()
    while True:
        move("X")
        drawBoard()
        if whoWon("X"):
            break
        move("O")
        drawBoard()
        if whoWon("O"):
            break

def drawBoard():
    for i in positions:
        board = " | ".join(i)
        print("|", board, "|")
    print("-----------------------------")

def move(symbol):
    while True:
        column = int(input(f"Enter Column (1-7) to place {symbol}: "))
        if positions[0][(column-1)] != " ":
            print("Enter valid value")
            continue         
        for row in positions[::-1]:
            if row[(column-1)] == ' ':
                row[(column-1)] = symbol
            elif row[(column-1)] != ' ':
                continue

            break
        break                

def whoWon(symbol):
    # horizontal
    for row in positions:
        result2 = "".join(row)
        if f"{symbol}{symbol}{symbol}{symbol}" in result2:
                    print(f"{symbol} Wins!")
                    return True
        
    # vertical
    for column in range(7):
        for i in range(3):
            if positions[i][column] == positions[i+1][column] == positions[i+2][column] == positions[i+3][column] == symbol:
                print(f"{symbol} Wins!")
                return True
    # across
    for column in range(4):
        for i in range(3):
            if positions[i][column] == positions[i+1][column+1] == positions[i+2][column+2] == positions[i+3][column+3] == symbol:
                print(f"{symbol} Wins!")
                return True
    
        for i in range(3,6):
            if positions[i][column] == positions[i-1][column+1] == positions[i-2][column+2] == positions[i-3][column+3] == symbol:
                print(f"{symbol} Wins!")
                return True

    return False 

   
    
        
if __name__ == "__main__":
    main()

