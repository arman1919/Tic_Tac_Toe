Tic Tac Toe Game with PyQt6

This project is a simple implementation of the classic Tic Tac Toe game using the PyQt6 library for the graphical user interface. The game allows two players to take turns and marks their symbols (X or O) on a 3x3 grid. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

Requirements
Python 3
PyQt6 library
Installation
Clone the repository:

bash

git clone https://github.com/arman1919/Tic_Tac_Toe.git

Change into the project directory:

bash

cd Tic_Tac_Toe

Install the required dependencies using pip:

bash

pip install -r requirements.txt

How to Play
Run the game by executing main.py:

bash

python main.py
Enter the names of Player 1 and Player 2 in the provided input fields and click "OK".
Players take turns clicking on the grid to place their symbols (X or O).
The game ends when one player achieves three in a row or when the board is filled (resulting in a draw).
Click "Restart" to play again.
Files
main.py: Entry point of the application, initializes the PyQt6 application and creates the main game dialog.

tik_tak.py: Contains the Ui_Dialog class, which defines the graphical user interface for the Tic Tac Toe game using PyQt6 widgets. Handles button clicks, player names input, and game restart.

XO.py: Defines the Board class for managing the game state (grid, check for a winner, restart), and the Player class to represent players with names and symbols.

Structure
The project follows a simple structure with separate files for the main application, GUI design, and game logic.

Contributions
Contributions to enhance the game or improve the code structure are welcome. Feel free to submit issues or pull requests.git init