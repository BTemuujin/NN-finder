import numpy as np

# read positions from file
positions = []
with open('positions.txt', 'r') as f:
    for line in f:
        x, y, z = map(float, line.strip().split())
        positions.append([x, y, z])

# convert positions list to numpy array
positions = np.array(positions)
num_positions = positions.shape[0]

# calculate distances
distances = np.zeros((num_positions, num_positions))
for i in range(num_positions):
    for j in range(num_positions):
        distances[i, j] = np.linalg.norm(positions[i] - positions[j])
        
n = 4

# find the three closest positions and distances for each position
results = []
for i in range(num_positions):
    closest_indices = np.argsort(distances[i])[1:n]  # exclude the first index since it is the position itself
    closest_positions = positions[closest_indices]
    closest_distances = distances[i, closest_indices]
    results.append((closest_positions, closest_distances))

# print results
for result in results:
    print(result)

for i in range(num_positions):
    nearest_neighbors = np.argsort(distances[i])[1:n]  # exclude the first element, which is the distance to itself
    for j in nearest_neighbors:
        #print(f"Position {i} has a nearest neighbor at position {j} with a distance of {distances[i, j]}")
        print(f"{distances[i, j]}")
