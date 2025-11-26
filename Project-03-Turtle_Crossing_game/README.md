# 🐢 Turtle Crossing Game 🚗

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/badges/shields)

<p align="center">
    <img src="https://media.tenor.com/zabQ7gLy57YAAAAM/jet-turtle-jet-turtle2.gif" alt="Gameplay GIF of the classic snake moving and eating food" width="600" height="300">
</p>

A simple arcade-style game where you help a turtle cross a busy road filled with moving cars. Built using Python's `turtle` graphics library.

***

## ✨ Features

*   **Player Control:** Move the turtle forward to cross the road.
*   **Traffic System:** Cars move across the screen at random intervals and colors.
*   **Level Progression:** Successfully crossing the road increases the level and the speed of the cars.
*   **Collision Detection:** The game ends if the turtle gets hit by a car.
*   **Scoreboard:** Tracks and displays the current level.

***

## 🛠️ Prerequisites

To run this game, you need:

*   Python 3.x

The game uses the standard **`turtle`**, **`time`**, and **`random`** modules, which are typically included with Python.

***

## 🚀 How to Run

1.  Ensure all project files (`main.py`, `player.py`, `car_manager.py`, `scoreboard.py`) are saved in the same directory.
2.  Open your terminal or command prompt, navigate to the project directory, and run the main file:

    ```bash
    python main.py
    ```

***

## 🕹️ Controls

The turtle is controlled using the keyboard:

| Key | Action |
| :---: | :--- |
| **W** | ⬆️ Move Forward |

*Goal: Reach the top edge of the screen without hitting any cars!*

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **core game loop** that sets up the screen, initializes objects, and handles game logic (movement, collisions, level up). |
| `player.py` | Defines the **`Player` class**, managing the turtle's movement and position resetting. |
| `car_manager.py` | Defines the **`CarManager` class**, which handles creating cars, moving them, and increasing their speed. |
| `scoreboard.py` | Defines the **`Scoreboard` class**, which displays the current level and the "GAME OVER" message. |
