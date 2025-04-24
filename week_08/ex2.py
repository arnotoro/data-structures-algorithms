def knapsack_and_count_solutions(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    solutions_count = 0

    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1] <= w:
                dp[i][w] = dp[i - 1][w - items[i - 1]] + dp[i - 1][w]
                if items[i - 1] == w:
                    dp[i][w] += 1  # Include the current item
            else:
                dp[i][w] = dp[i - 1][w]

    # The total number of solutions is in the last cell of the table
    solutions_count = dp[n][capacity]

    return solutions_count

# Example usage
items = [5, 2, 3, 7, 1]
capacity = 8

number_of_solutions = knapsack_and_count_solutions(items, capacity)
print("Number of possible solutions:", number_of_solutions)
