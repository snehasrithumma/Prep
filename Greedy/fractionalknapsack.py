def fractional_knapsack(values, weights, capacity):
    # Calculate value per unit weight
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    
    # Sort items by value per unit weight
    index.sort(key=lambda i: ratio[i], reverse=True)
    print(index)
    max_value = 0
    fractions = [0] * len(values)

    # Add items to the knapsack
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            max_value += values[i] * fractions[i]
            break

    return max_value, fractions

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, fractions = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in knapsack: {max_value}")
print(f"Fractions of items: {fractions}")
