# Maze Escape Game (PS No. 43)

A console-based 5×5 Maze Escape Game developed in **Python 3** using **2D lists** and the **Breadth-First Search (BFS)** algorithm.

**Submitted By:** Chhaya  
**ERP:** RU-26-02514  
**Course:** B.Tech Computer Science and Engineering (Core), 1st Year  
**Institution:** Rungta International Skills University (Rungta R1 Campus), Bhilai  

---

## Project Overview

In this game, the player navigates a 5×5 grid maze from the starting position `(0, 0)` to the exit `(4, 4)` using `W`, `A`, `S`, and `D` keyboard inputs. The program validates every step against maze boundaries and walls, tracks only valid moves, and includes an automated **BFS solver** to compute the shortest possible path length from start to finish.

### Maze Layout & Symbols
* `P` — Player's current position (Starts at Row 0, Col 0)
* `.` — Open path cell
* `#` — Wall obstacle (blocks movement)
* `E` — Exit destination (Located at Row 4, Col 4)

```text
P . . # #
# # . # #
# . . . #
# . # # #
# . . . E
```

---

## Features

* **2D List Grid Representation:** Stores and dynamically updates the 5×5 maze board after every valid move.
* **Directional Controls:** Supports `W` (Up), `A` (Left), `S` (Down), and `D` (Right) inputs (case-insensitive).
* **Collision & Boundary Validation:** Prevents moving outside the 5×5 grid or through `#` walls without incrementing the move counter.
* **Input Error Handling:** Catches invalid keys (e.g., `X`) and prompts the user without counting a move.
* **Shortest Path Finder (BFS):** Uses a queue-based Breadth-First Search algorithm to find the minimum number of steps (`10 steps`) from start to exit.

---

## Repository Structure

```text
Maze-Escape-Game/
│
├── maze_game.py                      # Complete Python 3 source code
├── PS43_Maze_Escape_Game_Report.pdf  # Full project documentation & report
└── README.md                         # Project overview and usage guide
```

---

## How to Run

1. Make sure **Python 3** is installed on your system.
2. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/Maze-Escape-Game.git
   cd Maze-Escape-Game
   ```
3. Run the Python script in your terminal/console:
   ```bash
   python maze_game.py
   ```

---

## Verified Test Cases

| Test Case | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input | `D` (from `(0, 0)`) | `Player moved to (row 0, col 1) \| Moves: 1` |
| **Test Case 2** | Boundary Input | `W` (at `(0, 0)`) | `Cannot move outside the maze. Player stays at (0, 0) \| Moves: 0` |
| **Test Case 3** | Invalid Input | `D`, `D`, `D`, `X` | `Wall ahead. Move blocked. Player stays at (0, 2)`<br>`Invalid key 'X'. Use W, A, S or D only.`<br>`Moves counted: 2` |
| **Test Case 4(a)** | Winning Path | `D, D, S, S, A, S, S, D, D, D` | `You escaped the maze! Total moves: 10` |
| **Test Case 4(b)** | Shortest Path (BFS) | Menu Option `2` | `Shortest path length: 10 steps` |