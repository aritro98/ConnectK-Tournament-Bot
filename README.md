# Connect-K Tournament Bot

Connect-K is a two-player game similar to Connect-4 but generalized — players alternately drop pieces into columns and attempt to be the first to connect K of their pieces in a row (horizontal, vertical, or diagonal). A game ends when a player connects K pieces or the board fills (draw).

## Table of Contents
1. [Overview](#overview)
2. [Project Workflow](#project-workflow)
3. [Key Features](#key-features)
4. [Tournament Rules and Disqualification](#tournament-rules-and-disqualification)
5. [Technologies Used](#technologies-used)
6. [Bot Interface](#bot-interface)
7. [Board Representation](#board-representation)
8. [Sample Bot](#sample-bot)
9. [Installation and Setup](#installation-and-setup)
10. [Usage](#usage)
11. [Results](#results)
12. [Future Scope](#future-scope)

## Overview
The project provides a lightweight, reproducible environment to develop, test, and compete bots that play the generalized Connect-K game (like Connect-4 but with a configurable K). It bundles a compiled tournament engine that orchestrates matches and a simple python bot interface so participants can focus on writing game logic and strategies without worrying about wiring, matchmaking, or rule enforcement.

## Project Workflow
1. **Prepare bots**: Each participant implements a single Python file with the required `init` and `next_move` functions.
2. **Place bots**: Put sample and participant bot files inside `bots/`. The engine loads every `.py` in that folder.
3. **Run engine**: Run the compiled engine (`connectk_engine.exe`) from the repo root. It automatically runs tournament matches, logs board states and per-move times, and produces match results.
4. **Collect results**: The engine prints winners, draws, and any disqualifications (timeouts/invalid moves). Uses the printed output or redirect to a file for later analysis.

## Key Features
- Simple, documented bot interface (`init`, `next_move`) — easy to implement.
- Engine enforces rules: move validity, 1s per-move time limit, and automated match orchestration.
- Sample bot provided as a template (random valid moves) to get started quickly.
- Human-readable board prints and per-move timing in engine logs for debugging and transparency.

## Tournament Rules and Disqualification
- **Time limit**: Each move must be returned within 1 second. Exceeding 1s = instant disqualification.
- **Valid moves only**: Returning an invalid column (a full column) = instant disqualification. Always ensure `board[0][col] == 0`.
- **Naming**: Save your Python bot as `<name>_bot.py` (e.g., `my_bot.py`). Files not following the format may not be considered.

## Technologies Used
- **Python 3.9 (or higher)**: For writing participant bots (engine calls Python bots).
- Compiled `connectk_engine.exe`: Provided binary (engine).

## Bot Interface
The bot must implement two functions exactly as below:
```python
def init(isFirst: bool, connectK: int):
    """
    Called once at the start of a game.
    - isFirst: True if your bot is Player 1, else False.
    - connectK: the K value required to win this match.
    Save global state (player id, heuristics, time budgets) here.
    """

def next_move(board: list[list[int]]) -> int:
    """
    Called each turn to get your move.
    - board: 2D list where board[0] is the top row and board[-1] is the bottom.
      Cell values: 0 = empty, 1 = player1, 2 = player2.
    - Return: integer column index (0-based) where you want to drop a piece.
    """
```
**Important**: Only return a column `c` where `board[0][c] == 0` (top cell empty), otherwise the engine treats it as an invalid move.

## Board Representation
- `board[row][col]` with `board[0]` = top row, `board[-1]` = bottom row.
- Engine places a piece in the lowest available row in the selected column (pieces “fall” like Connect-4).

## Sample Bot
Save this template as `sample_bot.py` or `<name>_bot.py` to test:
```python
import random
import time
my_id = None
connect_k = None

def init(isFirst,connectK):
    global my_id, connect_k
    connect_k=connectK
    if isFirst:
        my_id=1
    else:
        my_id=2

def next_move(board):
    print(board)
    # valid columns: those whose top cell is empty
    valid_columns = [c for c in range(len(board[0])) if board[0][c] == 0]
    time.sleep(0.1) 
    return random.choice(valid_columns)
```
This demonstrates the minimal valid implementation.