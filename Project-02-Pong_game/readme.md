# 🏆 Classic Pong Game 🏓
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/badges/shields)

A classic two-player arcade game of Pong, built using Python's built-in `turtle` graphics library.
<p align="center">
<img src="https://i.pinimg.com/originals/9a/87/3b/9a873b64d3fc756c633a6c23d4627560.gif" alt="A demonstration of the two-player Pong game in action" width="800" height="300"/>
</p>
## ✨ Features

* **Two-Player Local Multiplayer:** Control two separate paddles on a single screen.
* **Dynamic Difficulty:** The ball's speed increases every time it successfully hits a paddle, making the game progressively more challenging.
* **Score Tracking:** A dedicated scoreboard tracks the points for both the left and right players.
* **Simple Collision Logic:** Detection for collisions with the top/bottom walls and the paddles.

## 🚀 Getting Started

### Prerequisites

This project only requires a standard installation of Python 3.x, which includes the necessary `turtle` and `time` modules.

### How to Run

1.  Ensure all the project files (`main.py`, `paddle.py`, `ball.py`, and `scoreboard.py`) are saved within the `Project-02-Pong_game` directory.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the project folder.
4.  Run the main game file:

    ```bash
    python Project-02-Pong_game/main.py
    ```

## 🎮 Controls

The game is controlled via the keyboard:

| Player | Action | Key |
| :--- | :--- | :--- |
| **Left Paddle (Player 1)** | Move Up | `w` |
| **Left Paddle (Player 1)** | Move Down | `s` |
| **Right Paddle (Player 2)** | Move Up | `Up Arrow` |
| **Right Paddle (Player 2)** | Move Down | `Down Arrow` |

## 📁 File Structure

The project is organized into a modular structure using object-oriented programming:

* `main.py`: The entry point for the game. It handles the screen setup, initializes game objects, manages the game loop, and contains the core collision and scoring logic.
* `paddle.py`: Defines the `Paddle` class, which handles the creation and movement methods for the player paddles.
* `ball.py`: Defines the `Ball` class. It manages the ball's movement, horizontal and vertical bouncing, speed increase logic, and resetting the ball's position.
* `scoreboard.py`: Defines the `Scoreboard` class, responsible for drawing the scores on the screen and updating them when a player scores a point.
