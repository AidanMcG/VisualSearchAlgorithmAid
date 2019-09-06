# Visual Search Algorithm Learning Aid

  

Christopher Clarke 15456478

Aidan McGivern 15414228

CA326 Third Year Project

  
  
  
  
  
  
  
  
  
  
  
  
  

# 0\. Table of contents

  


0\. Table of contents  2

1\. Selecting a puzzle  3

1.1 Swapping between puzzles  

2\. The eight puzzle  3

2.1 What is the eight puzzle?  3

2.2 Inputting a start puzzle  4

2.3 Inputting a goal puzzle  4

2.4 Selecting an algorithm  4

2.5 Solving the puzzle  5

2.6 Understanding the data  5

3\. The word game  6

3.1 What is the word game?  6

3.2 Inputting a start word  7

3.3 Inputting a goal word  7

3.4 Selecting an algorithm  7

3.5 Solving the game  7

3.6 Understanding the data  7

  
  
  
  
  
  
  

# 1\. Selecting a puzzle

## 1.1 Puzzles

When the program starts it will initially open on the eight puzzle however the word game can be navigated to.

  

![](https://lh4.googleusercontent.com/5f2G8Mv08OM9S_cTj-0V7KNeF8iD8eVNWRvQy_r0s3z_r6mBxA4nyEfGif3dkkHq4PcKriSW9gu9UtBUdQpJlPtACd596HBm8Zgsd6ihk6GEB_5lSZH-XqYG-7wSDTSH-cQosMJ3)

## 1.2 Swapping between puzzles

To swap from the eight puzzle to the word game, simply select the arrow button located at the top right of the screen. To swap from the word game to the eight puzzle simply select the arrow button located at the top left of the screen.

# 2\. The eight puzzle

## 2.1 What is the eight puzzle?

The eight puzzle is a three by three square with the numbers one to eight filling eight of the nine squares. The last square is left blank. The idea of the eight puzzle is to manipulate the puzzle by utilising the blank square to move the numbers around until the the puzzle is solved.

## 2.2 Inputting a start puzzle

The start puzzle is the initial puzzle that the user will be given to solve. This can be inputted by typing in the numbers one to eight and the letter b to represent where the blank spot is.

To complete the entry simply press enter. To generate a random start puzzle simply press the randomise button. This will fill in the puzzle with random values.

  

![](https://lh6.googleusercontent.com/nkZmwWKUnx_mXCTwZ_Z_fBA7dnADW6mfh0E4Roocm0-8HEwqhf5bp4K0_1bIxuQWlo4CvL8HWTz77UxhZlDjDmjhUTY4KmMMNcJrTDHTiFfXqQf-64vIPmDm5loEwdOKdGElaokH)

## 2.3 Inputting a goal puzzle

The goal puzzle is the puzzle when it has been solved. This can be inputted by typing in the numbers one to eight and the letter b to represent where the blank spot is.

To complete the entry simply press enter. To generate a random start puzzle simply press the randomise button. This will fill in the puzzle with random values. Next press the start button to progress to solve the puzzle.

## 2.4 Selecting an algorithm

After pressing the start button a new screen should appear showing the start puzzle along with buttons on the left with the names of different algorithms. To select an algorithm click the corresponding button. The breadth first search algorithms is selected as default until a different button is pressed.

![](https://lh3.googleusercontent.com/VvOSlWaHRqdcvqjBiBSpvw3iGyNZuGO0vKAaW8faIEZ8RoePwvJCBUE64LV4ct8xXi8Ctc3TtIkMAMBxtjN2bkNXRL_l1SY18fNLw1cvzqOYxIgEoB3w6IRyRvAzLsR2xlQMQvEE)

## 2.5 Solving the puzzle

When solving the puzzle it is possible to solve it completely or step through the program. To solve the program simply click the solve button. To stop the program while it is solving the puzzle click the pause button. To restart the program click the solve button again. Alternatively it is possible to step through the puzzle one move at a time by clicking the next button. To reset the puzzle click the reset button

## 2.6 Understanding the data

On the right hand side of the screen the search tree is displayed, for each puzzle that it checks a dot is generated in a tree structure which shows nodes and their children.

BFS generates dots in horizontal lines first as you would expect as bfs selects nodes based on breadth.

  

Stepping through the puzzle, you can see dots generate slowly at your own pace which can help to understand how the algorithm works.

  

![](https://lh5.googleusercontent.com/NbE7qyFypCoPcBdRqckbhpz_uVQJEXbdVhkJRZCvlOIChXev004pPl9JhKVoFuz-efosjKJ73Ww43vUPXCbt0MjVVgwKMdGthW1PW2dVkp2WDvxr7WE9Jp3zcGgMFY8FPhukBgHZ)

# 3\. The word game

## 3.1 What is the word game?

The word game is a puzzle where a start word and a goal word is provided. The goal of the puzzle is to get from the start word to the goal word by changing one letter at a time. Each time a letter has been changed the word must be a valid word. For example if the start word was car and the goal word is eat the puzzle could go from car to cat to eat because cat is a valid word.

![](https://lh3.googleusercontent.com/G4nTnx76HivdkTnDx7UyHj26FQncTIUjTT3OifrpCfWtjTXIxfF-agRBJyPbTkjaSey0GV2fVKBgLnzQlJpcJnl59PpQsrDMSqu6IMidkw_TQZgFXwOUSeUwRW7JhKPQhmgeEWPI)

## 3.2 Inputting a start word

To input a start word click into the text box under the start word. Type in a lowercase word which will be the start word. Click enter

  

![](https://lh4.googleusercontent.com/Fw7mENXVQn5z5r4tG1f1nfCeIYi-x8h1ZU1O4C07UaQWlcCAoBQdYolSZtSGscpi81qxQ4hxi-75GVnN5_lXGUS_qKjImwZlB9NPFlS7go1aHaIVk42bUYonEgjUYOZevL9u1b0Z)

## 3.3 Inputting a goal word

To input a goal word click into the text box under the goal word. Type a lowercase word which is the same length as the start word. Click enter.

## 3.4 Selecting an algorithm

After pressing the start button a new screen should appear showing the start puzzle along with buttons on the left with the names of different algorithms. To select an algorithm click the corresponding button. The breadth first search algorithms is selected as default until a different button is pressed.

## 3.5 Solving the game

When solving the puzzle it is possible to solve it completely or step through the program. To solve the program simply click the solve button. To stop the program while it is solving the puzzle click the pause button. To restart the program click the solve button again. Alternatively it is possible to step through the puzzle one move at a time by clicking the next button. To reset the puzzle click the reset button

## 3.6 Understanding the data

On the right side of the screen is where the path is shown once it is generated. You can see the one letter difference in each word shown as it goes through the path.

  

![](https://lh3.googleusercontent.com/xzL2ZK_gudgXarR3Fr31Ubb-sXt4H5RqAFjRDrgDe9DJOl1NWuY7r7XNP2Ug6IRs6ihueSx_lXn8gQ8ysITy3V5AKPUmIcWYvmziaq0nqTTukxZhhf-OwWb2esJF6rnlgehfr6ld)