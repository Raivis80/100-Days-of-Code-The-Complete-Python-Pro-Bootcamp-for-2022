# Pong Game
## Game Description
Pong is a two-dimensional sports game that simulates table tennis. 
The game was originally manufactured by Atari, which released it in 1972. 
Pong was one of the earliest arcade video games. 
It is a table tennis sports game that simulates table tennis. 
The player controls an in-game paddle by moving it vertically across the left or right side of the screen. 
They can compete against another player controlling a second paddle on the opposing side. 
Players use the paddles to hit a ball back and forth. 
The goal is for each player to reach eleven points before the opponent; 
points are earned when one fails to return the ball to the other. 
The player who reaches eleven points first wins the game.

### Game Design
- Screen
  - Screen size: 800x600
  - Background color: black
  - Title: Pong Game
  - Tracer: 0
- Paddle
    - Shape: square
    - Color: white
    - Size: 5x1
    - Speed: 20
- Ball
    - Shape: circle
    - Color: white
    - Size: 20
    - Speed: 0.1
- Scoreboard
    - Font: Arial, 24, normal
    - Color: white
    - Position: (0, 260)
    - Alignment: center
- Wall
    - Shape: square
    - Color: white
    - Size: 0.5x30

### Game Logic with Pseudocode
- Screen
  - Setup the screen
    - Create a screen
    - Setup screen size
    - Setup background color
    - Setup screen title
    - Setup screen tracer
  - Listen to the screen
    - Listen to the screen for a click
  - Screen update
    - Update the screen
  - Screen exit on click
    - Exit the screen on click
- Paddle
    - Create paddle
        - Create a paddle
        - Setup paddle shape
        - Setup paddle color
        - Setup paddle size
        - Setup paddle speed
    - Move paddle
        - Move paddle up
        - Move paddle down
    - Paddle collision with wall
        - Paddle collision with top wall
        - Paddle collision with bottom wall
    - Paddle collision with ball
        - Paddle collision with ball
- Ball
    - Create ball
        - Create a ball
        - Setup ball shape
        - Setup ball color
        - Setup ball size
        - Setup ball speed
    - Move ball
        - Move ball
    - Ball collision with wall
        - Ball collision with top wall
        - Ball collision with bottom wall
    - Ball collision with wall
        - Ball collision with left wall
        - Ball collision with right wall
    - Ball collision with paddle
- Scoreboard
    - Create scoreboard
        - Create a scoreboard
        - Setup scoreboard font
        - Setup scoreboard color
        - Setup scoreboard position
        - Setup scoreboard alignment
    - Update scoreboard
        - Update scoreboard
- Wall
    - Create wall
        - Create a wall
        - Setup wall shape
        - Setup wall color
        - Setup wall size
    - Move wall
        - Move wall up
        - Move wall down
    - Wall collision with ball
        - Wall collision with ball
- Game
    - Game start
        - Start the game
    - Game play
        - Play the game
    - Game over
        - End the game
        - Exit the game

