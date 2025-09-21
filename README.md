# Connect-K Tournament Bot

Connect-K is a two-player game similar to Connect-4 but generalized — players alternately drop pieces into columns and attempt to be the first to connect K of their pieces in a row (horizontal, vertical, or diagonal). A game ends when a player connects K pieces or the board fills (draw).

## Table of Contents
1. [Overview](#overview)
2. [Project Workflow](#project-workflow)
3. [Key Features](#key-features)
4. [Tournament Rules & Disqualification](#tournament-rules-and-disqualification)
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
4. **Collect results**: The engine prints winners, draws, and any disqualifications (timeouts/invalid moves). Use the printed output or redirect to a file for later analysis.

## Key Features
- Simple, documented bot interface (`init`, `next_move`) — easy to implement.
- Engine enforces rules: move validity, 1s per-move time limit, and automated match orchestration.
- Sample bot provided as a template (random valid moves) to get started quickly.
- Human-readable board prints and per-move timing in engine logs for debugging and transparency.