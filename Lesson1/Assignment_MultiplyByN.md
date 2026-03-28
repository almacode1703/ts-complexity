# Assignment: MultiplyByN

## Goal

This project aims to get a clear understanding of how to program an algorithm in **1** and **N** iterations.

---

## Story

Shubhangi has to write a program by taking 2 numbers as input and multiplying them. Write 2 functions, one that will use **1 iteration** and the second using **N iterations** to multiply those numbers. Help her write this program.

---

## Example

```
Enter 'a' for a*b : 5
Enter 'b' for a*b : 6

1 iteration:  30
N iteration:  30
```

---

## Solution

### Function 1 — 1 Iteration (O(1))

Uses the direct multiplication operator to get the result in a single step.

```python
def multiply_one_iteration(a, b):
    return a * b
```

### Function 2 — N Iterations (O(n))

Uses a loop to add `a` to itself `b` times.

```python
def multiply_n_iterations(a, b):
    result = 0
    for i in range(b):
        result += a
    return result
```

### Complete Program

```python
def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

print("1 iteration: ", multiply_one_iteration(a, b))
print("N iteration: ", multiply_n_iterations(a, b))
```

---

## Output

```
Enter 'a' for a*b : 5
Enter 'b' for a*b : 6

1 iteration:  30
N iteration:  30
```

---

## Analysis

| Function | Approach | Time Complexity |
|---|---|---|
| `multiply_one_iteration` | Direct multiplication (`a * b`) | **O(1)** |
| `multiply_n_iterations` | Repeated addition (`a + a + ... b times`) | **O(n)** |
