import random
import numpy as np

def simulate_game(num_simulations=10000, rounds=100, sides=6, count_all_boxes=False):
    boxes = ['B', 'R', 'W', 'E']  # Box types: Blue, Red, Wild, Event
    box_probabilities = {'B': 7 / 19, 'R': 4 / 19, 'W': 4 / 19, 'E': 4 / 19}  # Probabilities for each box type
    event_boss_chance = 2 / 15  # Chance of triggering a boss from an event box

    letter_counts = []
    event_counts = []
    artifact_counts = []
    boss_counts = []

    for _ in range(num_simulations):
        total_letters = 0
        total_events = 0
        total_artifacts = 0
        total_bosses = 0

        position = 0

        for _ in range(rounds):
            # Roll a die with weighted probabilities for each box type
            box = random.choices(boxes, weights=[box_probabilities[box] for box in boxes])[0]

            if count_all_boxes:
                # Calculate rewards for each box passed through
                steps = random.randint(1, sides)
                for _ in range(steps):
                    current_box = random.choices(boxes, weights=[box_probabilities[box] for box in boxes])[0]
                    if current_box in ['B', 'R']:
                        total_letters += 1
                    elif current_box == 'W':
                        choice = random.choice(['letter', 'event', 'artifact'])
                        if choice == 'letter':
                            total_letters += 1
                        elif choice == 'event':
                            total_events += 1
                            if random.random() < event_boss_chance:
                                total_bosses += 1
                            else:
                                total_letters += 0.5
                        else:
                            total_artifacts += 1
                    elif current_box == 'E':
                        total_events += 1
                        if random.random() < event_boss_chance:
                            total_bosses += 1
                        else:
                            total_letters += 0.5
                position += 1

            else:
                # Only calculate rewards for the box landed on
                if box in ['B', 'R']:
                        total_letters += 1
                elif box == 'W':
                    choice = random.choice(['letter', 'event', 'artifact'])
                    if choice == 'letter':
                        total_letters += 1
                    elif choice == 'event':
                        total_events += 1
                        if random.random() < event_boss_chance:
                            total_bosses += 1
                        else:
                            total_letters += 0.5
                    else:
                        total_artifacts += 1
                elif box == 'E':
                    total_events += 1
                    if random.random() < event_boss_chance:
                        total_bosses += 1
                    else:
                        total_letters += 0.5

        letter_counts.append(total_letters)
        event_counts.append(total_events)
        artifact_counts.append(total_artifacts)
        boss_counts.append(total_bosses)

    return letter_counts, event_counts, artifact_counts, boss_counts

# Run simulations for each scenario
num_simulations = 10000
rounds = 100

# Scenario 1: 4-sided Die, Counting Only the Box Landed On
letters_landed_4, events_landed_4, artifacts_landed_4, bosses_landed_4 = simulate_game(num_simulations, rounds, sides=4, count_all_boxes=False)

# Scenario 2: 4-sided Die, Counting All Boxes Walked Through
letters_all_4, events_all_4, artifacts_all_4, bosses_all_4 = simulate_game(num_simulations, rounds, sides=4, count_all_boxes=True)

# Scenario 3: 6-sided Die, Counting Only the Box Landed On
letters_landed_6, events_landed_6, artifacts_landed_6, bosses_landed_6 = simulate_game(num_simulations, rounds, sides=6, count_all_boxes=False)

# Scenario 4: 6-sided Die, Counting All Boxes Walked Through
letters_all_6, events_all_6, artifacts_all_6, bosses_all_6 = simulate_game(num_simulations, rounds, sides=6, count_all_boxes=True)

# Calculate quartiles for each scenario
q1_letters = [
    np.percentile(letters_landed_4, 25), np.percentile(letters_all_4, 25),
    np.percentile(letters_landed_6, 25), np.percentile(letters_all_6, 25)
]
q2_letters = [
    np.percentile(letters_landed_4, 50), np.percentile(letters_all_4, 50),
    np.percentile(letters_landed_6, 50), np.percentile(letters_all_6, 50)
]
q3_letters = [
    np.percentile(letters_landed_4, 75), np.percentile(letters_all_4, 75),
    np.percentile(letters_landed_6, 75), np.percentile(letters_all_6, 75)
]

q1_events = [
    np.percentile(events_landed_4, 25), np.percentile(events_all_4, 25),
    np.percentile(events_landed_6, 25), np.percentile(events_all_6, 25)
]
q2_events = [
    np.percentile(events_landed_4, 50), np.percentile(events_all_4, 50),
    np.percentile(events_landed_6, 50), np.percentile(events_all_6, 50)
]
q3_events = [
    np.percentile(events_landed_4, 75), np.percentile(events_all_4, 75),
    np.percentile(events_landed_6, 75), np.percentile(events_all_6, 75)
]

q1_artifacts = [
    np.percentile(artifacts_landed_4, 25), np.percentile(artifacts_all_4, 25),
    np.percentile(artifacts_landed_6, 25), np.percentile(artifacts_all_6, 25)
]
q2_artifacts = [
    np.percentile(artifacts_landed_4, 50), np.percentile(artifacts_all_4, 50),
    np.percentile(artifacts_landed_6, 50), np.percentile(artifacts_all_6, 50)
]
q3_artifacts = [
    np.percentile(artifacts_landed_4, 75), np.percentile(artifacts_all_4, 75),
    np.percentile(artifacts_landed_6, 75), np.percentile(artifacts_all_6, 75)
]

q1_bosses = [
    np.percentile(bosses_landed_4, 25), np.percentile(bosses_all_4, 25),
    np.percentile(bosses_landed_6, 25), np.percentile(bosses_all_6, 25)
]
q2_bosses = [
    np.percentile(bosses_landed_4, 50), np.percentile(bosses_all_4, 50),
    np.percentile(bosses_landed_6, 50), np.percentile(bosses_all_6, 50)
]
q3_bosses = [
    np.percentile(bosses_landed_4, 75), np.percentile(bosses_all_4, 75),
    np.percentile(bosses_landed_6, 75), np.percentile(bosses_all_6, 75)
]

# Print results
print("Quartiles (Q1, Q2, Q3) for each scenario:")
print("---------------------------------------------------------")
print("Letters:")
print(f"4-sided Die, Landed On:    Q1={q1_letters[0]:.2f}, Q2={q2_letters[0]:.2f}, Q3={q3_letters[0]:.2f}")
print(f"4-sided Die, All Boxes:    Q1={q1_letters[1]:.2f}, Q2={q2_letters[1]:.2f}, Q3={q3_letters[1]:.2f}")
print(f"6-sided Die, Landed On:    Q1={q1_letters[2]:.2f}, Q2={q2_letters[2]:.2f}, Q3={q3_letters[2]:.2f}")
print(f"6-sided Die, All Boxes:    Q1={q1_letters[3]:.2f}, Q2={q2_letters[3]:.2f}, Q3={q3_letters[3]:.2f}")

print("\nEvents:")
print(f"4-sided Die, Landed On:    Q1={q1_events[0]:.2f}, Q2={q2_events[0]:.2f}, Q3={q3_events[0]:.2f}")
print(f"4-sided Die, All Boxes:    Q1={q1_events[1]:.2f}, Q2={q2_events[1]:.2f}, Q3={q3_events[1]:.2f}")
print(f"6-sided Die, Landed On:    Q1={q1_events[2]:.2f}, Q2={q2_events[2]:.2f}, Q3={q3_events[2]:.2f}")
print(f"6-sided Die, All Boxes:    Q1={q1_events[3]:.2f}, Q2={q2_events[3]:.2f}, Q3={q3_events[3]:.2f}")

print("\nArtifacts:")
print(f"4-sided Die, Landed On:    Q1={q1_artifacts[0]:.2f}, Q2={q2_artifacts[0]:.2f}, Q3={q3_artifacts[0]:.2f}")
print(f"4-sided Die, All Boxes:    Q1={q1_artifacts[1]:.2f}, Q2={q2_artifacts[1]:.2f}, Q3={q3_artifacts[1]:.2f}")
print(f"6-sided Die, Landed On:    Q1={q1_artifacts[2]:.2f}, Q2={q2_artifacts[2]:.2f}, Q3={q3_artifacts[2]:.2f}")
print(f"6-sided Die, All Boxes:    Q1={q1_artifacts[3]:.2f}, Q2={q2_artifacts[3]:.2f}, Q3={q3_artifacts[3]:.2f}")

print("\nBosses:")
print(f"4-sided Die, Landed On:    Q1={q1_bosses[0]:.2f}, Q2={q2_bosses[0]:.2f}, Q3={q3_bosses[0]:.2f}")
print(f"4-sided Die, All Boxes:    Q1={q1_bosses[1]:.2f}, Q2={q2_bosses[1]:.2f}, Q3={q3_bosses[1]:.2f}")
print(f"6-sided Die, Landed On:    Q1={q1_bosses[2]:.2f}, Q2={q2_bosses[2]:.2f}, Q3={q3_bosses[2]:.2f}")
print(f"6-sided Die, All Boxes:    Q1={q1_bosses[3]:.2f}, Q2={q2_bosses[3]:.2f}, Q3={q3_bosses[3]:.2f}")
