# Activity: RecursionTimeComplexity

## Short Description

Calculate the time complexity of the recursive function.

---

## Solution

This recursive function will take:

```
T(n) = T(n/2) + T(n/2)
```

for 2 recursive calls, and for the rest of the code, our function will take **constant time**.

---

### Code

```python
def prints(n):
    if n <= 0:
        return

    print("Codingal")
    prints(n // 2)
    prints(n // 2)

# call the function
prints(8)
```

---

## Recurrence Relation

```
T(n) = T(n/2) + T(n/2) + θ(1)    when n > 0
T(n) = θ(1)                        when n <= 0
```

---

## Recurrence Tree

For `T(n) = T(n/2) + T(n/2) + θ(1)`:

```
                        T(n)                        ← Cost: 1
                       /    \
                  T(n/2)    T(n/2)                  ← Cost: 2
                 /    \     /    \
            T(n/4) T(n/4) T(n/4) T(n/4)            ← Cost: 4
            /  \   /  \   /  \   /  \
           ...  ...  ...  ...  ...  ...             ← Cost: 8
           |                          |
          T(1)  .....................T(1)            ← Cost: 2^(log n) = n
```

---

## Analysis

- At each level, the number of nodes **doubles**.
- The depth of the tree is **log₂(n)** (since `n` is halved at each level).
- Cost at each level:

| Level | Nodes | Cost per Node | Total Cost |
|---|---|---|---|
| 0 | 1 | θ(1) | 1 |
| 1 | 2 | θ(1) | 2 |
| 2 | 4 | θ(1) | 4 |
| ... | ... | ... | ... |
| k | 2ᵏ | θ(1) | 2ᵏ |
| log₂(n) | n | θ(1) | n |

- **Total cost** = 1 + 2 + 4 + 8 + ... + n = 2⁰ + 2¹ + 2² + ... + 2^(log₂n)

Using the geometric series formula:

```
Total = 2^(log₂(n) + 1) - 1 = 2n - 1
```

---

## Time Complexity

> **T(n) = O(n)**
