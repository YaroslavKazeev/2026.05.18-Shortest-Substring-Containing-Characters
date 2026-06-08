def shortestSubstring(s):
    # Find all unique characters in the string
    unique_chars = set(s)
    required = len(unique_chars)

    # If string has only one unique character, return 1
    if required == 1:
        return 1

    # Sliding window approach
    from collections import defaultdict

    window_counts = defaultdict(int)
    formed = 0
    left = 0
    min_length = float("inf")

    for right, char in enumerate(s):
        # Add current character to window
        window_counts[char] += 1

        # If this character's count reaches 1, we've found a new unique character
        if window_counts[char] == 1:
            formed += 1

        # Try to shrink the window while we still have all required characters
        while formed == required and left <= right:
            # Update minimum length
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length

            # Remove leftmost character
            left_char = s[left]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                formed -= 1
            left += 1

    return min_length


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
