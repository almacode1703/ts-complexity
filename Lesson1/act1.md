# Activity 1: OneAlgoThreeFaces

## Short Description

Calculate the time complexity of the recursive function.

---

## Solution

Suppose you have a problem writing a function that will sum the first `n` numbers for a given input `n`, then these three approaches are valid:

---

### Function 1 — O(1)

```python
def fun1(n):
    return n * (n + 1) / 2

print(fun1(4))
```

**Algorithm:**

```
(4 * 5) / 2
```

So, the number of iterations will be **1** for any input.

> **Time Complexity: O(1)**

---

### Function 2 — O(n)

```python
def fun2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(fun2(4))
```

**Algorithm:**

```
1 + 2 + 3 + 4
```

So, the number of iterations will be `1 + 1 + 1 + 1 = 4 = n` (input) iterations.

> **Time Complexity: O(n)**

---

### Function 3 — O(n²)

```python
def fun3(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += 1
    return sum

print(fun3(4))
```

**Algorithm:**

```
1  +  (1+1)  +  (1+1+1)  +  (1+1+1+1)
```

So, the number of iterations will be `1 + 2 + 3 + 4 = 10`.

> **Time Complexity: O(n²)**
