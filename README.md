# Connect-K Tournament Bot

Connect-K is a two-player board game inspired by Connect-4, allowing variable board sizes and win conditions (K in-a-row). The objective is to align K consecutive pieces horizontally, vertically, or diagonally. The bot autonomously competes against others in tournament settings and aims to maximize its win rate using strategy and fast calculations.

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
This project contains an advanced AI bot for the generalized Connect-K game, designed for competitive programming tournaments. The bot leverages optimized search algorithms to excel in time-constrained, rule-driven environments.

## Project Workflow
- Understand the official tournament rules and guidelines.
- Implement and rigorously test the bot algorithm (`my_bot.py`).
- Simulate tournaments and evaluate bot performance using provided CSV results.
- Ensure strict adherence to all competition constraints.

## Key Features
- **Iterative Deepening Minimax with Alpha-Beta Pruning**: Fast and deep search for optimal moves within a 1-second time frame.
- **Smart Heuristic Evaluation**: Evaluates board state for both offense and defense, including threats, opportunities, and center control.
- **Rule Compliance**: Only valid moves, no timeouts, and plays on any board size (5–10) and K-value (K>3).
- **Tournament-Quality Reliability**: Tested with tournament match data and standings.

## Tournament Rules and Disqualification
- **1 Second/Move Limit**: Each move must be returned within 1 second; exceeding this results in disqualification.
- **Valid Column Requirement**: Placing a piece in a full column leads to instant disqualification.
- **Function Interface**: Must implement `init(isFirst, connectK)` and `next_move(board)`, each meeting strict time constraints.

## Technologies Used
- Python 3.11+
- Built-in standard libraries: `copy`, `random`, `time`
- No third-party packages (per competition regulations)

## Bot Interface
The bot must implement two functions exactly as below:
```python
def init(isFirst, connectK):
    # Sets the bot's player ID and win condition

def next_move(board):
    # Returns the next column index where the bot should play
```

## Board Representation
- The board is a list of lists.
- `0` = empty, `1` = Player 1, `2` = Player 2.
- `board` is the top row, `board[-1]` is the bottom row.

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

## Installation and Setup
1. Install Python 3.11 (bots run under Python 3.11).
2. Clone the repository:
   ```bash
   git clone https://github.com/aritro98/ConnectK-Tournament-Bot.git
   cd ConnectK-Tournament-Bot
   ```
3. Run your bot via the supplied tournament engine (`connectk_engine.exe`) as instructed in the guidelines.

## Usage
1. The bot can be directly imported or registered as an external participant in tournament scripts.
2. To test, run tournament simulations using the configurations provided.

## Results
- Tournament results and standings are available in:
  - ./stats/tournament_matrix_k5.csv
  - ./stats/tournament_standings_k5.csv

## Future Scope
- Integrate advanced move ordering and caching for deeper search.
- Add support for reinforcement learning or neural evaluation.
- Enhance the evaluation function for larger board/K combinations.
- Develop web-based or GUI-based Connect-K match visualizers.