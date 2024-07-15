Introduction

This simulation script is developed as part of the course project for IAT210. The board game "Vowel Venture: The Artifact Hunt" involves players navigating a circular board, encountering different types of boxes that yield various rewards. This simulation aims to analyze the outcomes and balance of the game under different scenarios.
Simulation Overview

The simulation script vowel_venture_simulation.py simulates multiple rounds of the board game, tracking the collection of letters, events, artifacts, and boss encounters. It allows for variations in the rules, such as counting rewards from all boxes passed through or only the box landed on, and uses different dice sizes (4-sided and 6-sided).
Features

    Box Types:
        Blue (B): Increases letter count.
        Red (R): Increases letter count.
        Wild (W): Randomly increases letter count, triggers an event, or grants an artifact.
        Event (E): Triggers an event, with a chance to encounter a boss.

    Customizable Parameters:
        num_simulations: Number of game simulations to run.
        rounds: Number of rounds per simulation.
        sides: Number of sides on the die (4 or 6).
        count_all_boxes: Whether to count rewards from all boxes passed through (True) or only the box landed on (False).

    Probability Distributions:
        Box probabilities: Blue (7/19), Red (4/19), Wild (4/19), Event (4/19).
        Boss chance from an event box: 2/15.

    Simulation Outputs:
        Quartiles (Q1, Q2, Q3) for letters, events, artifacts, and bosses collected under different scenarios.

Running the Simulation

To run the simulation, execute the script using a Python environment with the numpy library installed. The script runs four scenarios:

    4-sided die, counting only the box landed on.
    4-sided die, counting all boxes walked through.
    6-sided die, counting only the box landed on.
    6-sided die, counting all boxes walked through.

The results will be printed to the console, showing the quartiles for letters, events, artifacts, and bosses collected in each scenario.
Results Interpretation

The simulation provides quartile data for each scenario, which can be used to analyze the balance and fairness of the game mechanics. By comparing the quartiles, you can determine how different rules and die sizes affect the distribution of rewards.
Conclusion

This simulation is a tool for analyzing the game balance of "Vowel Venture: The Artifact Hunt." It helps in understanding the impact of different game rules and can guide further refinements to ensure an engaging and fair gameplay experience.
