# 0/1 knapsack

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0]* (capacity+1) for __ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j-weights[i-1]]+values[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][capacity]


# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
values = [6, 12, 10]
weights = [1, 3, 2]
capacity = 5

print(knapsack(values, weights, capacity))