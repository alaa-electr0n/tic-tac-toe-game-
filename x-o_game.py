from tkinter import *
from tkinter import font
import random

# Creating the GUI
window = Tk()
window.title("TIC TAC TOE Game")
window.resizable(0,0)

# State Variables
players= ["X", "O"]
# pc_player = random.choice(players)
turn = 0 
game_over= False
score_player = 0
score_pc =0 

# Creation of the board grid 

buttons= []

# Create the 3x3 grid using nested loops
for row in range(3):
    
    current_row = []
    for col in range(3): 
        current_row.append(None)
    # Add the row to the board
    buttons.append(current_row) #[[(0,0), (0,1), (0,2)] ,
    #                             [(1,0),(1,1), (1,2)],
    #                             [(2,0), (2,1), (2,2)]]

def start_new_game():
    global current_player, pc_player
    pc_player = random.choice(players)
    current_player = "X"  # or "O", depending on your preference
    restart()

def disable_btns():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)


   
def check_winner(buttons):
    global game_over
    winning_color = "#34c9eb"

    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != " ":
            for j in range(3):
                buttons[i][j].config(bg=winning_color)
            game_over = True
            return buttons[i][0]['text']
        
        elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != " ":
            for j in range(3):
                buttons[j][i].config(bg=winning_color)
            game_over = True
            disable_btns()
            return buttons[0][i]['text']
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
        buttons[0][0].config(bg=winning_color)
        buttons[1][1].config(bg=winning_color)
        buttons[2][2].config(bg=winning_color)
        game_over = True
        disable_btns()
        return buttons[0][0]['text']
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
        buttons[0][2].config(bg=winning_color)
        buttons[1][1].config(bg=winning_color)
        buttons[2][0].config(bg=winning_color)
        game_over = True
        disable_btns()
        return buttons[0][2]['text']

    # Check for a tie
    occupied_count = sum(button['text'] != " " for row in buttons for button in row)
    total_cells = 9
                
    if occupied_count == total_cells:
        game_over = True
        return "Tie"
    return None


# Function to update scores and labels
def update_scores(winner):
    global score_player, score_pc
# Update score only if there's a winner
    if winner != "Tie":
        if winner == pc_player:
            score_pc += 1
        else:
            score_player += 1

    score_label_player.config(text=f"You: {score_player}")
    score_label_pc.config(text=f"PC: {score_pc}")




#Start New Game # RESTART
def restart():
    global game_over
    game_over = False
    default_bg = window.cget('bg')  # Get the default background color of the window
    status_label.config(text="")
    for row in buttons:
        for button in row:
            button.config(text=" ", state=NORMAL, bg=default_bg)

    # Check if computer should start
    if current_player == pc_player:
        computer_move()



def switch_players():
    global current_player

    
    if current_player == players[0]:  # If it's currently player 1's turn
        current_player = players[1]  # Switch to player 2's turn (or computer's turn)
    else:
        current_player = players[0]  # Switch to player 1's turn

      
        
    
     

def computer_move():
    global game_over
    if game_over:  # Exit if the game is over
        return

    # Make a move on the first available spot
    for row in buttons:
        for button in row:
            if button['text'] == " ":
                button.config(text=current_player, state=DISABLED)
                winner = check_winner(buttons)
                if winner:
                    handle_game_over(winner)
                else:
                    switch_players()
                return  # Exit after making a move

def handle_game_over(winner):
    global game_over
    game_over = True
    if winner == "Tie":
        tie_color= "#db535f"
        status_label.config(text="Tie, No Winners", foreground=tie_color)
        for row in buttons:
            for button in row:
                button.config(bg= tie_color)
    else:
        status_label.config(text=f"{winner} Wins!")
    update_scores(winner)
    disable_btns()



#Play game on clicking btns 
def play_game(row, col):
    global game_over, current_player
     
    if not game_over and buttons[row][col]['text'] == " ":
        buttons[row][col].config(text=current_player, state=DISABLED)
        winner = check_winner(buttons)
        if winner:
            # Handle game-over scenario
            handle_game_over(winner)
        else:
            switch_players()
            if current_player == pc_player:
                computer_move()
      


        


#______________GUI INTERFACE_____________________________________________________________
# Creating Score Frame and Labels
score_frame = Frame(window)
score_frame.grid(row= 0 , column= 0, columnspan= 3, sticky="nsew", pady= 20)

score_label_player = Label(score_frame, text = " You : 0", font= font.Font(family="Tahoma", size=20, weight= "bold") )
score_label_pc = Label(score_frame, text = " PC : 0 ", font= font.Font(family="Tahoma", size=20, weight= "bold") )

score_label_player.grid(row= 0 , column =0, padx= 50, pady= 7, sticky="ew")
score_label_pc.grid(row= 0 , column =2, padx= 5, pady= 7, sticky="ew")


# creating the status 
status_frame =Frame(window)
status_frame.grid(row= 2, column= 1 , columnspan= 3, sticky="ew", ipadx= 20)


status_label = Label(status_frame, text= " ", font= font.Font(family= "Tahoma", size= 18, weight="bold"), foreground="#34c9eb")
status_label.grid(row= 2, column= 1, padx = 20 , pady = 10 , sticky="ew")


# Creating the restart button 
restart_frame = Frame(window)
restart_frame.grid(row= 3, column = 0 ,columnspan= 3, pady= 10)
restart_btn= Button(restart_frame, text= "Restart", font= font.Font(family= "Tahoma", size= 16, weight="normal"), relief= RAISED, command=restart)
restart_btn.grid(row = 3, column = 2, pady= 7, ipadx= 10 )

# CReating the board

board_frame = Frame (window)
board_frame.grid (row= 4, column=0, sticky= "nsew", columnspan=3, padx= 5, pady= 7 )



# creating the 9 buttons 

for r in range(3):
    for c in range(3):
        buttons[r][c] = Button(board_frame, 
                               text =" ", 
                               width= 12 , 
                               height = 5, 
                               relief= RAISED,
                               font= font.Font(family= "Tahoma", size =14) 
                               ,command= lambda row= r, col = c: play_game(row, col))
        buttons[r][c].grid(row= r, column= c, sticky= "nsew", )





start_new_game()
window.mainloop()