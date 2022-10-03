## Day 23

### Project: Turtle crossing game

#### Description
This is a simple game where you have to cross the road without getting hit by the cars. 
The game is over when you get hit by a car or when you reach the other side of the road. 
The game is won when you reach the other side of the road.

#### How to play
- Use the arrow key to move the turtle up.
- The turtle can't move outside the screen.

### Game design

#### Game logic
- The turtle starts at the bottom of the screen.
- The turtle can move only up.
- The turtle can't move outside the screen.
- The cars start at the left of the screen.
- The cars move from left to right.

#### Game flow
- The turtle starts at the bottom of the screen.
- The turtle can move up.
- The turtle can't move outside the screen.
- The cars start at the left of the screen.
- The cars move from left to right.
- The cars speed up when the turtle reaches the other side of the road.
- The score increases when the turtle reaches the other side of the road.
- The game ends when the turtle gets hit by a car.
- The game ends when the turtle reaches the other side of the road.
- The game restarts when the turtle reaches the other side of the road.
- The game restarts when the turtle gets hit by a car.

#### Game objects
- The main.py file contains the game logic.
- The car_manager.py file contains the car class.
- The scoreboard.py file contains the scoreboard class.
- player.py file contains the player class.

##### Game mechanics car_manager.py
- Create a car class.
- Create a car object.
- Create a car list.
- Create a car speed.
- Create a car speed increase.
- Create a car speed increase interval.
- Create a car speed increase interval counter.
- Create a car speed increase interval counter reset.
- Create a car speed increase interval counter reset value.

##### Game mechanics scoreboard.py
- Create a scoreboard class.
- Create a scoreboard object.
- Create a scoreboard score.
- Create a scoreboard score increase.
- Create a game over sequence.

##### Game mechanics player.py
- Create a player class.
- Create a player object.
- Create a player starting position.
- Create a player starting position x.
- Create a player starting position y.
- Create a player move up.
- Create a player move speed.

#### Game mechanics main.py
- Create a screen.
- import a player.
- import a car manager.
- import a scoreboard.
- Create game loop.
- Create a player.
- Create a car manager.
- Create a scoreboard.
- Create a game is on.
- Create a game is on reset.

