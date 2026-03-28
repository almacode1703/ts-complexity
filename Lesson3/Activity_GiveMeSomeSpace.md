# Activity: GiveMeSomeSpace

## Short Description

Calculate the space complexity of the recursive function.

---

## Solution

### 1. Constant Space — θ(1)

```python
def sum_n(n):
    return n * (n + 1) // 2  # integer result

print("Sum of first n numbers (n=5):", sum_n(5))
```

- The function uses only a fixed number of variables regardless of the input size.
- No extra data structures or recursive calls are involved.

> **Space Complexity: θ(1)**
> **Auxiliary Space: θ(1)**

---

### 2. Linear Space — θ(n)

```python
def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

# Examples
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))
```

- With the size of the array, the space required also increases.
- The input array `a` itself takes **θ(n)** space.
- The function only uses one extra variable (`total`), so auxiliary space is constant.

> **Space Complexity: θ(n)**
> **Auxiliary Space: θ(1)**

---

### 3. Recursive Space — θ(n)

```python
def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("Recursive sum (n=5):", summ(5))
```

- Each recursive call adds a new frame to the **call stack**.
- For input `n = 5`, the call stack looks like:

```
summ(5)
  └── summ(4)
        └── summ(3)
              └── summ(2)
                    └── summ(1)
                          └── summ(0) → returns 0
```

- There are **n + 1** frames on the stack at the deepest point.

> **Space Complexity: θ(n)**
> **Auxiliary Space: θ(n)**

---

## Summary

| Function | Approach | Space Complexity | Auxiliary Space |
|---|---|---|---|
| `sum_n` | Direct formula | **θ(1)** | **θ(1)** |
| `array_sum` | Iterative (array input) | **θ(n)** | **θ(1)** |
| `summ` | Recursive | **θ(n)** | **θ(n)** |
