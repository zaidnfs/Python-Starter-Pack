# 🐍 Python Snake Game 🎮

A classic implementation of the arcade game Snake using the Python `turtle` graphics library.

***

## 📸 Screenshots
<p align="center">
    <img src="https://i.pinimg.com/originals/f0/6e/79/f06e795352e21c9936e2b8a0991c7a42.gif" alt="Gameplay GIF of the classic snake moving and eating food" width="600">
</p>

***
## ✨ Features

* **Classic Gameplay:** Control a growing snake to eat food.
* **🏆 Persistent High Score:** The highest score is saved to a local file (`data.txt`) and loaded on startup.
* **💥 Collision Detection:** The game detects collisions with the walls and the snake's own tail.
* **🔄 Restart on Collision:** The snake resets and the score is zeroed upon collision with the wall or tail, allowing for continuous play.

***

## 🛠️ Prerequisites

To run this game, you need:

* Python 3.x

The game uses the standard **`turtle`** and **`time`** modules, which are typically included with Python.

***

## 🚀 How to Run

1.  Ensure all project files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`) are saved in the same directory.
2.  Create an empty file named **`data.txt`** in the same directory to store the high score.
3.  Open your terminal or command prompt, navigate to the project directory, and run the main file:

    ```bash
    python main.py
    ```

***

## 🕹️ Controls

The snake is controlled using the following keys:

| Key | Action |
| :---: | :--- |
| **W** | ⬆️ Move Up |
| **S** | ⬇️ Move Down |
| **D** | ➡️ Move Right |
| **A** | ⬅️ Move Left |

*Note: The snake cannot instantly reverse direction (e.g., if moving UP, pressing DOWN is ignored).*

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **core game loop** that sets up the screen, initializes objects, and handles collision logic (food, wall, tail). |
| `snake.py` | Defines the **`Snake` class**, managing segment creation, movement, extension, and resetting the snake. |
| `food.py` | Defines the **`Food` class** (the red circle 🍎), handling its appearance and random placement. |
| `scoreboard.py` | Defines the **`Scoreboard` class**, which manages and displays the current score and reads/writes the high score to `data.txt`. |
