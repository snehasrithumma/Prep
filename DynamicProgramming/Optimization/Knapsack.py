def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    print(dp)
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            print(weights[i-1], w, i)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
values = [6, 10, 12]
weights = [1, 2, 3]
capacity = 5

print(knapsack(values, weights, capacity))