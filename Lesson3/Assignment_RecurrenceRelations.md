# Assignment: Recurrence Relations

## Goal

This project aims to get a clear understanding of how to calculate the recurrence relation of any recursive function.

---

## Story

Shubhangi has written some code and now wants to calculate the time complexity of the same. She wants to calculate the recurrence relations of the functions. Help her find the same and print the output.

---

## Function 1

```python
def myfunction1(n):
    if (n > 0):
        return
    for i in range(0, n + 1):
        print("Codingal")
    myfunction1(n / 2)
    myfunction1(n / 3)
```

### Analysis

- The `for` loop runs `n + 1` times → **θ(n)**
- There are **2 recursive calls**: one with `n/2` and one with `n/3`.

### Recurrence Relation

```
T(n) = T(n/2) + T(n/3) + θ(n)    when n > 0
T(n) = θ(1)                        when n <= 0
```

---

## Function 2

```python
def myfunction2(n):
    if (n <= 1):
        return
    print("Codingal")
    myfunction2(n - 1)
```

### Analysis

- The `print` statement takes **constant time** → **θ(1)**
- There is **1 recursive call** with `n - 1`.

### Recurrence Relation

```
T(n) = T(n-1) + θ(1)    when n > 1
T(n) = θ(1)              when n <= 1
```

### Solving the Recurrence (Substitution Method)

```
T(n) = T(n-1) + 1
     = T(n-2) + 1 + 1
     = T(n-3) + 1 + 1 + 1
     ...
     = T(1) + (n-1)
     = 1 + (n-1)
     = n
```

> **Time Complexity: O(n)**

---

## Complete Program

```python
def myfunction1(n):
    if (n > 0):
        return
    for i in range(0, n + 1):
        print("Codingal")
    myfunction1(n / 2)
    myfunction1(n / 3)

def myfunction2(n):
    if (n <= 1):
        return
    print("Codingal")
    myfunction2(n - 1)

# Print recurrence relations
print("Recurrence Relation for myfunction1:")
print("T(n) = T(n/2) + T(n/3) + θ(n)  when n > 0")
print("T(n) = θ(1)                      when n <= 0")
print()
print("Recurrence Relation for myfunction2:")
print("T(n) = T(n-1) + θ(1)            when n > 1")
print("T(n) = θ(1)                      when n <= 1")
print("Time Complexity: O(n)")
```

---

## Summary

| Function | Recursive Calls | Non-Recursive Cost | Recurrence Relation | Time Complexity |
|---|---|---|---|---|
| `myfunction1` | `T(n/2) + T(n/3)` | θ(n) | T(n) = T(n/2) + T(n/3) + θ(n) | — |
| `myfunction2` | `T(n-1)` | θ(1) | T(n) = T(n-1) + θ(1) | **O(n)** |
