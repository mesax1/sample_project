"""
The task is to write a function that finds pairs of integers from a list that
sum to a given value. The function will take as input the list of numbers as
well as the target sum.

Sample output is shown below.
```
> app 1,9,5,0,20,-4,12,16,7 12

+ 12,0
+ 5,7
+ 16,-4

```

In the example, there is an executable named `app`. It takes as command line
arguments a comma separated list of integers, and the target integer. Your app
doesn't need to have identical input/output mechanisms. For example, you could
read from a file instead of the command line.

You can assume that all input values are integers. You can assume that there aren't
any repeat values in the list.

The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately.
"""
from typing import List


def find_the_pairs(nums: List[int], target: int) -> List[int]:
    """
    Function that finds pairs of integers from a list that
    sum to a given value. The function will take as input the list of numbers as
    well as the target sum. The function will return the list of pairs that sum to
    the target value. If no pair is found, return an empty list. If the input list is
    empty, it also returns an empty list.

    Complexity O(n)

    Parameters
    ----------
    nums : List[int]
        List of integers
    target : int
        Target value to which the pairs of integers should sum

    Returns
    -------
    pairs: List[int]
        List of pairs of integers values that sum to the given target.

    """
    pairs = []
    tracking_set = set()

    for i, current_value in enumerate(nums):
        difference = target - current_value
        if difference in tracking_set:
            pairs.append([difference, current_value])
        tracking_set.add(current_value)
    return pairs


if __name__ == "__main__":
    input_list = [1, 9, 5, 0, 20, -4, 12, 16, 7]

    target_value = 12

    resulting_pairs = find_the_pairs(input_list, target_value)

    print(resulting_pairs)
