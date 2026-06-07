def shortestSubstring(s):
    # Write your code here
    unique_letters = set(s)
    uniqueQty = len(unique_letters)
    # The number of window positions for the smallest window that consist only of unique letters
    maxWindowPositions = len(s) - len(unique_letters) + 1

    for windowSizeStep in range(maxWindowPositions):
        # Each iteration the number of available positions (i) decreases in accordance with the growing size of the windowSizeStep
        for i in range(maxWindowPositions - windowSizeStep):
            window = s[i : i + uniqueQty + windowSizeStep]
            if set(window) == unique_letters:
                return len(window)


EXAMPLE_TEST_CASES = [
    {
        "name": "example_1",
        "input": "dabbcabcd",
        "expected": 4,
        "description": "Example 1 from README",
    },
    {
        "name": "example_2",
        "input": "asdfkjeghfalawefhaef",
        "expected": 13,
        "description": "Example 2 from README",
    },
    {
        "name": "single_character",
        "input": "a",
        "expected": 1,
        "description": "Single character string",
    },
    {
        "name": "all_same_characters",
        "input": "aaaaaa",
        "expected": 1,
        "description": "String with all identical characters",
    },
    {
        "name": "all_distinct_characters",
        "input": "abcdef",
        "expected": 6,
        "description": "String with all unique characters",
    },
    {
        "name": "shortest_at_beginning",
        "input": "abcddddddd",
        "expected": 4,
        "description": "Shortest substring is at the beginning",
    },
    {
        "name": "shortest_at_end",
        "input": "ddddddabcd",
        "expected": 4,
        "description": "Shortest substring is at the end",
    },
    {
        "name": "repeating_pattern",
        "input": "abccba",
        "expected": 3,
        "description": "Pattern repeats, two shortest substrings are equal length",
    },
]
