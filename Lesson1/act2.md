# Activity 2: Iterations

## Short Description

Do the basic asymptotic analysis for the functions written in the previous activity.

---

## Solution

### Function 1

**Algorithm:**

```
(4 * 5) / 2
```

So, the number of iterations will be **1**.

---

### Function 2

**Algorithm:**

```
1 + 2 + 3 + 4
```

So, the number of iterations will be `1 + 1 + 1 + 1 = 4`.

---

### Function 3

**Algorithm:**

```
1 + (1+1) + (1+1+1) + (1+1+1+1)
```

So, the number of iterations will be `1 + 2 + 3 + 4 = 10`.

---

## Asymptotic Analysis

For our functions 1, 2, and 3, the number of iterations depends upon `n` (4 in our case):

1. **Fun1** : C₁
2. **Fun2** : C₂(n) + C₃
3. **Fun3** : C₄(n²) + C₅(n) + C₆

The above conversions are known as the **Asymptotic Analysis** of the algorithm.

---

## Comparison between Function 1 and Function 2

| n | Fun1 (iterations) | Fun2 (iterations) |
|---|---|---|
| 1 | 1 | 1 |
| 10 | 1 | 10 |
| 100 | 1 | 100 |
| 1000 | 1 | 1000 |

> As `n` grows, Function 1 remains constant at **O(1)** while Function 2 grows linearly at **O(n)**.
