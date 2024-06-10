def subset_sum(numbers, target):
    dp = [  False] *(target+1)
    dp[0] = True

    for num in numbers:
        print('------------------',num)
        for i in range(target, num-1, -1):
            print('------',i, dp[i],  dp[i-num])
            dp[i] = dp[i] or dp[i-num]
        print(dp,'**************')
    return dp[target]




# Example usage
numbers = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(numbers, target))  # Output: True