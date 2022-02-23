import random
import pandas as pd
import matplotlib.pyplot as plt


# Create function that simulates a single bet, returning 1 or -1 based on the chance of landing on a red

def roulette_spin():
    # betting on red
    # there are 38 slots -> 2 are green, 18 are red, 18 are black
    # therefore, the chance of winning if betting on red is 18/38 = .4737

    random_number = random.random()
    if random_number <= 0.4737:
        return 1
    else:
        return -1


# Run simulation
# We will initialize 'current_winnings' variable at 0 and store as position one.
# We will run the above function 1000 times, each time adding to the 'current_winnings' variable the amount won or lost.
# We will record the 'current_winnings' for each step in the process for review.

current_winnings = 0
tracker = [current_winnings]

for i in range(1000):
    round_winnings = roulette_spin()
    current_winnings = current_winnings + round_winnings
    tracker.append(current_winnings)

winnings_df = pd.DataFrame(tracker, columns=['cumulative_winnings'])

winnings_df['cumulative_winnings'] = winnings_df['cumulative_winnings'].astype(float)

plot = winnings_df[['cumulative_winnings']].plot()

fig = plot.get_figure()
fig.savefig("roulette_winnings.png")

print("user ended 1000 trials with {} dollars".format(tracker[-1]))
