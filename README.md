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
The project provides a lightweight, reproducible environment to develop, test, and compete bots that play the generalized Connect-K game (like Connect-4 but with a configurable K). It bundles a compiled tournament engine that orchestrates matches and a simple Python bot interface so participants can focus on writing game logic and strategies without worrying about wiring, matchmaking, or rule enforcement.