# memoization
def fib(n, memo={}):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo)+ fib(n-2, memo)
    print(memo)
    return memo[n]


print(fib(7))


# tabulation
def fib_memo(n):
    if n<=2:
        return 1
    table = [0] *(n+1)
    table[1], table[2] = 1,1
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]
    print(table)
    return table[n]

print(fib_memo(7))