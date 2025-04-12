# Pygame Meteorite Dodger  
The Meteorite Dodger is a game created using PyGame, where you control a Mars rover to dodge meteorites.

## Description  
The game begins once the player presses the start button. The player starts with three lives and uses the **left** and **right arrow keys** to control the rover. If the rover collides with a meteorite, the player loses a life. Once all lives are lost, the game ends.  

Invincibility shields  appear randomly during the game. When the player absorbs a shield, the rover becomes temporarily immune to meteorite collisions. Any shields absorbed after the first one will be ignored until the timer for the initial shield expires.  

Once the game is over, the player has the option to either quit or restart the game.

## Visuals  


## Requirements  
- Python 3.13  
- pygame 2.6.1  

To install pygame, use the following command:  
```bash  
pip install pygame  
