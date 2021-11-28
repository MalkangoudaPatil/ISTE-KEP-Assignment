board = {

    'A1': ' ','A2': ' ','A3': ' ',
    'B1': ' ','B2': ' ','B3': ' ',
    'C1': ' ','C2': ' ','C3': ' '
}

player = 1               #to initialise 1st player
total_moves = 0          #to count no of moves
end_check = 0

def check():
    ##checking moves of player one
    
    # for horizontal(Start)
    if board['A1']=='X' and board['A2']=='X' and board['A3']=='X':
        print('player one won')
        return 1
    if board['B1']=='X' and board['B2']=='X' and board['B3']=='X':
        print('player one won')
        return 1
    if board['C1']=='X' and board['C2']=='X' and board['C3']=='X':
        print('player one won')
        return 1
    # for horizontal(end)
    
    #for diagonal(start)
    if board['A1']=='X' and board['B2']=='X' and board['C3']=='X':
        print('player one won')
        return 1
    if board['C1']=='X' and board['B2']=='X' and board['A3']=='X':
        print('player one won')
        return 1
    #for diagonal(end)

    #for vertical(start)
    if board['A1']=='X' and board['B1']=='X' and board['C1']=='X':
        print('player one won')
        return 1
    if board['A2']=='X' and board['B2']=='X' and board['C2']=='X':
        print('player one won')
        return 1
    if board['A3']=='X' and board['B3']=='X' and board['C3']=='X':
        print('player one won')
        return 1
    #for vertical(end)

    ##checking player two moves

    # for horizontal(Start)
    if board['A1']=='O' and board['A2']=='O' and board['A3']=='O':
        print('player two won')
        return 1
    if board['B1']=='O' and board['B2']=='O' and board['B3']=='O':
        print('player two won')
        return 1
    if board['C1']=='O' and board['C2']=='O' and board['C3']=='O':
        print('player two won')
        return 1
    # for horizontal(end)
    
    #for diagonal(start)
    if board['A1']=='O' and board['B2']=='O' and board['C3']=='O':
        print('player two won')
        return 1
    if board['C1']=='O' and board['B2']=='O' and board['A3']=='O':
        print('player two won')
        return 1
    #for diagonal(end)

    #for vertical(start)
    if board['A1']=='O' and board['B1']=='O' and board['C1']=='O':
        print('player two won')
        return 1
    if board['A2']=='O' and board['B2']=='O' and board['C2']=='O':
        print('player two won')
        return 1
    if board['A3']=='O' and board['B3']=='O' and board['C3']=='O':
        print('player two won')
        return 1
    #for vertical(end)
    return 0


    



    

print('A1|A2|A3')
print('- +- +-')
print('B1|B2|B3')
print('- +- +-')
print('C1|C2|C3')

print('*********************')

while True:
    print(board['A1']+'|'+board['A2']+'|'+board['A3'])
    print('-+-+-')
    print(board['B1']+'|'+board['B2']+'|'+board['B3'])
    print('-+-+-')
    print(board['C1']+'|'+board['C2']+'|'+board['C3'])

    end_check = check()

    if total_moves == 9 or end_check == 1:
        break
    while True:                   #input from the players
        if player == 1:           #choose player
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            #on wrong input

            else:
                print('invalid input!')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            #on wrong input

            else:
                print('invalid input!')
                continue
    total_moves += 1
    print('*************************************')


                   

