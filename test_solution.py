import pytest

from solution import EXAMPLE_TEST_CASES, shortestSubstring


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_shortestSubstring(case):
    result = shortestSubstring(case["input"])
    assert (
        result == case["expected"]
    ), f'{case["name"]} failed: expected {case["expected"]}, got {result}'


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
