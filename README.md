# Catan
A collection of tools designed to provide a deeper mathematical understanding of optimal Settlers of Catan strategies. This repository contains scripts for calculating winning combinations and analyzing game statistics.
### Overview

This project is aimed at players who want to move beyond casual play and understand the underlying probabilities and requirements for victory in Catan. It breaks down the game into programmable components to analyze efficiency and win conditions.
### Project Structure

The repository currently consists of two primary scripts:
#### 1. winCombinations.cpp (C++)

A performance-oriented script designed to calculate or iterate through the various ways a player can reach the 10-victory-point threshold.

    Purpose: Identifies valid combinations of Settlements, Cities, Longest Road, Largest Army, and Victory Point cards.

    Usage: Compile using any C++ compiler (e.g., g++ winCombinations.cpp -o winCombos).

#### 2. Stats.py (Python)

A script focused on the statistical and probabilistic side of the game.

    Purpose: Likely used for simulating dice roll distributions, resource yield expectations, or analyzing the frequency of specific board outcomes.

    Usage: Run using Python 3 (python Stats.py).
