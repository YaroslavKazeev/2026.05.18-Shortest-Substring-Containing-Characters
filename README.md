# Shortest Substring Containing Characters

You are given a string `s` containing lowercase letters (a-z).

Your task is to find the length of the shortest substring that contains every distinct
character that appears in `s` at least once.

In other words:

- Identify all unique letters in `s`
- Find the smallest window of `s` that includes all of those letters
- Return the length of that window

## Example 1

**Input:** `s = "dabbcabcd"`

**Output:** `4`

**Explanation:**

- All characters in the string: `[a, b, c, d]`
- Two of the substrings that contain all letters are `"dabbc"` and `"abcd"`.
- `"abcd"` is the shorter of the two.

## Example 2

**Input:** `s = "asdfkjeghfalawefhaef"`

**Output:** `13`

**Explanation:**

- All characters in the string: `[a, d, e, f, g, h, j, k, l, s, w]`
- The shortest substring that contains all letters is `"sdfkjeghfalawe"`.

## Constraints

- `1 <= size of s <= 10^5`
- `s` contains letters in the range `ascii[a-z]`

## Test Case Input Format

The only line contains a string, `s`.

Complete the `shortestSubstring` function below.

The function is expected to return an INTEGER.
The function accepts STRING `s` as parameter.
