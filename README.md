1)Description of the core functions and summarize the techniques
We created three separate python files for our game. They are menu.py, TicTacToe.py and TicTacToemodule.py. Each python file has its own functions and the files represent different parts in the whole game program. When running the game program, all three python files need to be run together at the same time.
For TicTacToemodule.py:
We import the pygame modules which is an open-platform designed for programmers writing video games. It helps import internet graphics and sound tracks to be used in the games. They can be used together with python. We start with the pygame constructor. It is related to the outlook or display of the game. It decides the width and height and number of rows and columns for the board. We also decide the size of circle and square put inside the board. We also add the title “Tic-Tac-Toe” to be displayed on the screen.
Core functions:
a) draw_lines and drawFigure function: draw_lines function draws the two horizontal
and verticals lines on the board. drawFigure function decide if the player is 1, the
player can only draw circle and if the player is 2, he or she can only draw cross.
b) availableSquare function: We input the row and column of the Square and it will
return true if no player has clicked on it before, otherwise, it will return false.
c) isBoardFull function: it is different from the availableSquare function as this function
uses two for loops to check all the squares inside the board whether all squares have been clicked by players and return true. The availableSquare function checks specific square only but not all squares.
d) checkWin function: There are 8 ways to win the game. There are three ways to win vertically and another 3 ways to win horizontally and 2 ways to win diagonally. We check whether all three squares are clicked by the same player one or two, if all three squares in one of the winning ways are all clicked by the same player, it will return true indicating the player input wins the game. We insert other methods in the class within the function. We insert isBoardFull function to check whether the board is full, it will return false indicating that the player inserted loses the game.
e) draw_Winner function: We use checkWin function to check which player win the game. If player 1 win the game, the function will display a string with test “ Player 1 win”. If no players win the game, it will display “tie” indicated no player win and the game is over. It will then three more texts. First, is “press r to restart” with yellow color background and “Press “esc” to exit game” with red background and the last text is “Press “0” to return to menu.”with blue color. Therefore, there are a total of 4 texts display vertically in the screen.
f) drawVerticleline, drawHorizontalline and the two drawDiagonalLine functions: if one of the players win the game, the function will draw a straight line to pass through all circles or crosses to indicate the way the player win. The line will be white if player one win and be black if player 2 win.
g) restart function: There is “r”button to restart the game and draw_lines functions will be implemented. The player first start(click) the game will default to be player one. The function will also clear all the crosses and circles drew in the previous game.
Techniques: In this file, we mainly use nested for loop to check where the player put their cross or circle in the board by clicking the square in the screen. The outer loop locates the row and the inner loop locates the column. We also use the if - elif - else statement to check whether the element in the square in a circle is done by player one or cross done by player 2. For TicTacToe.py:
It is the main program for the game. At start, we need to import TicTacToemodule.py. Core function:
a) main function:
The default player is player one which indicates the first person to start the game by clicking the square in the screen is the player one and it will not be changed till the current game is over. We use a whileTrue infinite loop to keep the game running as long as the player clicks the “start” button. When the user clicks the top left red cross button(sys.exit), the game will exit. Afterwards, once the player clicks the intended grid with the mouse (event) the marker would draw the shape onto the grid, we have a variable called clicked_Row and clicked_coloumns to declare which grid has been clicked and the respective shape will take effect and will be displayed on the screen. Then, we use the imported function availableSquare function to check whether the square is filled or not and we use the Square_maker function to decide which player is making the square and decide whether a cross or circle is displayed. Then, we use the imported checkWin function to check whether the player wins the game after he clicks the square and use draw_Winner function to show the text displaying which player wins, then the game will be over. After each game, the player who first starts the game who default to be player one will switch to player 2 and vice versa.
Besides, the function also detects the user keyboard input, if the user presses “R” in the keyboard, the imported restart function will be implemented. If the user presses “Esc” on the keyboard, the system will exit and the game will disappear from the screen. If the user presses “0” on the keyboard, the screen will be directed back to the menu to restart the game and the current pygame will exit. After all, the mane will be updated in accordance with what happened.
For menu.py:
This is a plain menu with a background color of blue and a caption of the menu, which is ‘menu’ and the name of our game “Tic-Tac-Toe”, with a red “start game” button and a green “quit” button.
a) Main loop for the menu:
This menu will be displayed to enter the game, and the keyboard key ‘0’ will lead you back to the menu. The program would know if you have clicked the start button using coordinates, and not a collide method, this does start up an error( further explained in the limitations).
We kept the menu simple and to be as robust as possible and not to overcrowd the menu with bloats and doesn’t really contribute to the betterment of the program. The

 .blit method does display all the text onto the menu screen.Techniques: In this file, we use the infinite whileTrue loop to check for the event that happened in the pygame, where the player presses the buttons either on the screen or the keyboard and to check if any player wins or the game is over to stop the game.
2) Implemented Data structure
The data structure we have used is 2D-Array, which is used to store the value in a grid format with rows and columns and it is used to represent the game board, with each cell in the array representing an empty spot and symbols placed by a player represented by the players symbol(‘O’ or ‘X’), allow me to iterated that this structure is purely user-defined and all the inputs are stored in the 2D Array:
example:
board =[ [None,None,None],
[None,None,None],
[None,None,None] ]
This creates a 3x3 array of none values to represent an empty Tic-Tac-Toe board. if player 1 starts:
board =[ [O,None,None],
[None,None,None],
[None,None,None] ]
then the next player which is player 2: board =[ [O,None,None],
[None,X,None],
[None,None,None] ]
These are just abstract illustrations. All of this grid is behind the decorated grid. 3)Self-Reflection
Even Though there are many perfected Tic-Tac-Toe games out there, our’s is flawed undoubtedly, but we have tried our very best to fix the game to cater the users, as the game can get more complex in the future with an Minimax algorithm, which will be our algorithm to supplement our Self-study report.
These are the following weaknesses of our program:
1: Our game isn't cross-device compatible, as this game is only workable on laptops or pc, as most of the inputs are from a physical keyboard.
Future solution:
We can use a different method in our program which is the collide method, this can allow mouse-clicks to restart the game, exit the game, to return to the menu etc.
2: Our game doesn’t have the suitable class to count the points of how many time a player has won, this something that we couldn’t add, Maybe in the future, we could add a class to store the players name and to accumulate the points of how many times the player has won, we could also add a amount of times they would like to play for example first to 5 points,etc.
3. The game overlaps the menu once a player returns to the menu using the key “0”, when the grid is not full and is required to press are ‘r’ to return to the game grid. This is one of the problems we still couldn’t find a solution to.(The pictures are included in the appendix)

 4: The game’s menu start button also doesn't work, it is static but the quit button works fine. This happens after the game is over and the user presses ‘0’ to go back to the menu. We also can't find a solution to this. Overall, these are the limitations in our program and with further research and experience, I can confidently say that we can fix the errors, but with limited python knowledge, unfortunately, this is all we can do.
4)References
Without these references, we couldn't have done all this:
GeeksForGeek: https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/amp/ Free Code Camp: Pygame Tutorial for Beginners - Python Game Development Course
To make the menu: Used Poe (AI chatbot) Disclaimer: This report was done by us entirely) Coder space: Coding Tic Tac Toe in Python with Pygame
   
 Appendix:
1:Test cases
2:Different winning scenarios 3:types of error
TEST CASES: Menu:
  The game:
 
 Player 1 wins:
 player 2 wins:
 
 Tie:
 Different winning scenarios:
     
 The errors
The game disappears after key 0 after pressing ‘r’ and then exits the menu
If you notice the caption is now the menu instead of tic-tac-toe, that's why when 0 is pressed it exits the game and the game disappears, (“INTERESTING!!!!)
    
The screen is frozen, and the start button is static The quit button works fine
