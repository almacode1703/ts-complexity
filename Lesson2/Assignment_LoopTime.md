# Assignment: LoopTime

## Goal

This project aims to get a clear understanding of how to calculate the time complexity of common loops.

---

## Story

Shubhangi has a piece of code and wants to calculate the time complexity of the same. Help her by finding the time complexity for each loop and printing the total time complexity.

---

## Code Snippet

```python
def myfunction(n):
    for i in range(0, n + 1):
        print("First Loop")

    j = 1
    while (j <= n + 1):
        print("Second Loop ", j)
        j = j * 2

    for i in range(0, 100):
        print("Third loop")
```

---

## Solution

### Loop 1 — `for i in range(0, n+1)`

- The loop runs from `0` to `n`, i.e., **n + 1** times.
- Each iteration performs a constant time operation (`print`).

> **Time Complexity: O(n)**

---

### Loop 2 — `while (j <= n+1)` with `j = j * 2`

- `j` starts at `1` and doubles every iteration: `1, 2, 4, 8, 16, ...`
- The loop runs until `j > n + 1`.
- After `k` iterations, `j = 2ᵏ`. The loop stops when `2ᵏ > n + 1`, i.e., `k = log₂(n + 1)`.

> **Time Complexity: O(log n)**

---

### Loop 3 — `for i in range(0, 100)`

- The loop runs exactly **100** times regardless of the input `n`.
- This is a constant number of iterations.

> **Time Complexity: O(1)**

---

## Total Time Complexity

```
T(n) = O(n) + O(log n) + O(1)
```

Since we take the **dominant term** (the one that grows the fastest as `n` increases):

> **Total Time Complexity: O(n)**

---

## Summary

| Loop | Iterations | Time Complexity |
|---|---|---|
| Loop 1 (`for` — linear) | n + 1 | **O(n)** |
| Loop 2 (`while` — doubling) | log₂(n + 1) | **O(log n)** |
| Loop 3 (`for` — constant) | 100 | **O(1)** |
| **Total** | — | **O(n)** |

---

## Complete Program

```python
import math

def myfunction(n):
    # Loop 1: O(n)
    for i in range(0, n + 1):
        print("First Loop")

    # Loop 2: O(log n)
    j = 1
    while (j <= n + 1):
        print("Second Loop ", j)
        j = j * 2

    # Loop 3: O(1)
    for i in range(0, 100):
        print("Third loop")

def print_time_complexity():
    print("Loop 1 Time Complexity: O(n)")
    print("Loop 2 Time Complexity: O(log n)")
    print("Loop 3 Time Complexity: O(1)")
    print("Total Time Complexity:  O(n)")

n = int(input("Enter n: "))
myfunction(n)
print()
print_time_complexity()
```
