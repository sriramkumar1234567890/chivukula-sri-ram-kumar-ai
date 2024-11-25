import itertools


def word_to_number(word, mapping):
    number = 0
    for letter in word:
        number = number * 10 + mapping[letter]
    return number


def solve_crypto_arithmetic(words, result):
    letters = set(''.join(words) + result)  # Collect unique letters

    if len(letters) > 10:  # More than 10 unique letters means no solution
        print("Too many unique letters for a valid solution!")
        return

    # Try all possible digit mappings for the unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip mappings where a word or result starts with 0
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue

        # Convert words and result to their corresponding numerical values
        words_value = sum(word_to_number(word, mapping) for word in words)
        result_value = word_to_number(result, mapping)

        # Check if the sum of words equals the result
        if words_value == result_value:
            print("Solution found:")
            for letter, digit in mapping.items():
                print(f"{letter} = {digit}")
            print(f"{' + '.join(words)} = {result}")
            return

    # If no solution found
    print("No solution found.")


# Example usage
words = ["SEND", "MORE"]
result = "MONEY"
solve_crypto_arithmetic(words, result)
