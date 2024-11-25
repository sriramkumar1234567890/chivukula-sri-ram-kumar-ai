import math

def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta):
    """
    Implement Alpha-Beta Pruning.
    """
    if depth == 3:  # Terminal node
        return values[node_index]

    if is_maximizing:
        max_eval = -math.inf
        for i in range(2):  # Maximizer's turn
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Minimizer's turn
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def main():
    """
    Main function to demonstrate Alpha-Beta Pruning.
    """
    print("Alpha-Beta Pruning Demonstration")
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # Example game tree leaf node values
    print("Leaf node values:", values)
    optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
    print("Optimal value calculated by Alpha-Beta Pruning:", optimal_value)

if __name__ == "__main__":
    main()
