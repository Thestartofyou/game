import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_players = 10
num_rounds = 100

# Generate a random graph representing the network
network = nx.erdos_renyi_graph(num_players, 0.3)

# Initialize player strategies (0 or 1)
player_strategies = np.random.randint(2, size=num_players)

# Initialize player payoffs
player_payoffs = np.zeros(num_players)

# Define payoff matrix (e.g., prisoner's dilemma)
payoff_matrix = np.array([[3, 0], [5, 1]])

# Simulation
for _ in range(num_rounds):
    for i in range(num_players):
        neighbors = list(network.neighbors(i))
        neighbor_strategies = player_strategies[neighbors]
        my_strategy = player_strategies[i]
        neighbor_payoffs = payoff_matrix[my_strategy, neighbor_strategies]
        player_payoffs[i] += np.sum(neighbor_payoffs)

    # Update player strategies based on neighbor payoffs
    new_player_strategies = np.zeros(num_players)
    for i in range(num_players):
        neighbors = list(network.neighbors(i))
        neighbor_payoffs = player_payoffs[neighbors]
        best_neighbor = np.argmax(neighbor_payoffs)
        new_player_strategies[i] = player_strategies[best_neighbor]
    player_strategies = new_player_strategies

# Plot network
pos = nx.spring_layout(network, seed=42)
nx.draw(network, pos, with_labels=True, node_color=['blue' if s == 0 else 'red' for s in player_strategies])
plt.title('Network Game')
plt.show()

