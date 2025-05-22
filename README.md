# Classic Pong Game in Python (Pygame)

This is a simple and modern recreation of the classic Pong arcade game, built using Python and the Pygame library. It’s designed to be lightweight, fun, and easy to understand, making it a great project for beginners learning game development or Python programming.

---

## Features

- Two-player local multiplayer using keyboard controls
- Increasing ball speed with each paddle hit for escalating challenge
- Clean and retro-style graphics with simple game logic
- Ball resets and pauses briefly after each score
- Responsive paddle controls and smooth frame rate
- Fully customizable settings for screen size, speeds, and colors

---

## Technologies Used

- Python 3
- Pygame library

---

## Controls

| Action         | Player 1 | Player 2 |
|----------------|----------|----------|
| Move Up        | W        | Up Arrow |
| Move Down      | S        | Down Arrow |
| Quit Game      | Q        | Q        |

---

## How It Works

- The game starts with the ball moving from the center.
- If the ball hits the top or bottom wall, it bounces off.
- If it hits a paddle, it bounces back and speeds up slightly.
- If it passes a paddle, the opposing player scores a point and the ball resets.
- The game runs at 60 FPS and maintains consistent timing using Pygame's clock.

---

## Installation and Running

1. Install the required dependency in terminal (may have to run in administrator)

   ```bash
   pip install pygame
