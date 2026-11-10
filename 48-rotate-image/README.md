# Rotate Image – LeetCode 48

<h2><a href="https://leetcode.com/problems/rotate-image/">Rotate Image</a></h2>

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Topic](https://img.shields.io/badge/Topic-Array-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Approach](https://img.shields.io/badge/Approach-In--Place-green)

---

## 1. Problem Statement

You are given an `n x n` 2D matrix representing an image. Rotate the image by **90 degrees clockwise**.

You must rotate the image **in-place**, meaning you must modify the original input matrix directly.

**Important:** Do not create another 2D matrix to store the rotated result.

### Example 1

**Input:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output:**

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Example 2

**Input:**

```python
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
```

**Output:**

```python
[
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
```

### Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## 2. What Does In-Place Mean?

An **in-place algorithm** modifies the original data structure instead of creating another data structure to store the result.

For example:

**Not in-place:**

```python
new_matrix = []
```

Here, we are creating another matrix to store the rotated result.

**In-place:**

```python
matrix[0][0], matrix[2][2] = matrix[2][2], matrix[0][0]
```

Here, we directly swap elements inside the original matrix.

### Important Points

- We modify the original matrix.
- We do not create another matrix.
- We use a constant amount of auxiliary memory.
- We use swapping and existing list operations.

---

## 3. Approach: Transpose + Reverse Each Row

The easiest way to rotate an N x N matrix 90 degrees clockwise in-place is to perform two operations:

1. Transpose the matrix.
2. Reverse every individual row.

### Step 1: Understand Transpose

Transposing means converting rows into columns and columns into rows.

**Original Matrix:**

```text
1  2  3
4  5  6
7  8  9
```

**After Transpose:**

```text
1  4  7
2  5  8
3  6  9
```

Notice:

- First row `[1, 2, 3]` becomes the first column.
- Second row `[4, 5, 6]` becomes the second column.
- Third row `[7, 8, 9]` becomes the third column.

### How Do We Transpose In-Place?

We swap elements across the main diagonal.

The swapping syntax in Python is:

```python
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

Here:

- `i` represents the row index.
- `j` represents the column index.
- `matrix[i][j]` represents the element at row `i` and column `j`.
- `matrix[j][i]` represents the corresponding element across the diagonal.

### Step 2: Understand the Transpose Code

```python
n = len(matrix)

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

#### Line 1: Calculate Matrix Size

```python
n = len(matrix)
```

`len(matrix)` returns the number of rows.

For our 3 x 3 matrix:

```python
n = 3
```

Since this is a square matrix, the number of rows and columns is equal.

#### Line 2: Outer Loop

```python
for i in range(n):
```

The outer loop controls the row index.

It executes with:

```text
i = 0
i = 1
i = 2
```

#### Line 3: Inner Loop

```python
for j in range(i + 1, n):
```

The inner loop controls the column index.

**Important:** We start `j` from `i + 1` instead of `0`.

Why?

Because:
1. We don't need to swap diagonal elements with themselves.
2. We don't want to swap the same pair of elements twice.
3. Starting from `i + 1` ensures that we only swap elements above the main diagonal with their corresponding elements below it.

### Why Do We Use `j = i + 1`?

Consider the matrix coordinates:

```text
(0,0)  (0,1)  (0,2)
(1,0)  (1,1)  (1,2)
(2,0)  (2,1)  (2,2)
```

The required swaps are:

```text
(0,1) <-> (1,0)
(0,2) <-> (2,0)
(1,2) <-> (2,1)
```

We don't swap the diagonal elements:

```text
(0,0), (1,1), (2,2)
```

They are already in their correct positions.

If we start `j` from `0`, the same elements would be swapped twice, undoing the first swap.

---

## 4. Complete Dry Run of Transpose

Initial matrix:

```text
1  2  3
4  5  6
7  8  9
```

### Iteration 1: i = 0

```python
for j in range(1, 3):
```

Therefore:

```text
j = 1
j = 2
```

**First swap:**

```python
matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
```

We swap `2` and `4`.

Matrix becomes:

```text
1  4  3
2  5  6
7  8  9
```

**Second swap:**

```python
matrix[0][2], matrix[2][0] = matrix[2][0], matrix[0][2]
```

We swap `3` and `7`.

Matrix becomes:

```text
1  4  7
2  5  6
3  8  9
```

### Iteration 2: i = 1

```python
for j in range(2, 3):
```

Therefore:

```text
j = 2
```

Swap:

```python
matrix[1][2], matrix[2][1] = matrix[2][1], matrix[1][2]
```

We swap `6` and `8`.

Matrix becomes:

```text
1  4  7
2  5  8
3  6  9
```

### Iteration 3: i = 2

```python
for j in range(3, 3):
```

This range is empty, so no swapping happens.

**Transpose is completed!**

Result:

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

---

## 5. Step 2: Reverse Every Individual Row

After transposing, our matrix is:

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

Our target is:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

We need to reverse every individual inner list.

### Understand Python's reverse() Method

Example:

```python
arr = [1, 2, 3]

arr.reverse()

print(arr)
```

Output:

```python
[3, 2, 1]
```

**Important:** `reverse()` modifies the original list. It does not create a new list.

### Why Do We Write `for row in matrix`?

Our matrix is a list containing other lists.

```python
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

We can access the inner lists using:

```python
matrix[0] = [1, 4, 7]
matrix[1] = [2, 5, 8]
matrix[2] = [3, 6, 9]
```

When we write:

```python
for row in matrix:
    row.reverse()
```

Python automatically iterates over the elements of `matrix` and assigns each inner list to the variable `row`.

We don't need to define `row` before the loop.

### Dry Run

**Iteration 1:**

```python
row = matrix[0]
```

Value:

```python
[1, 4, 7]
```

After:

```python
row.reverse()
```

Result:

```python
[7, 4, 1]
```

**Iteration 2:**

```python
row = matrix[1]
```

Value:

```python
[2, 5, 8]
```

After reversing:

```python
[8, 5, 2]
```

**Iteration 3:**

```python
row = matrix[2]
```

Value:

```python
[3, 6, 9]
```

After reversing:

```python
[9, 6, 3]
```

Final matrix:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Why Does `row.reverse()` Modify the Original Matrix?

This is an important Python concept called **References and Mutable Objects**.

Consider:

```python
matrix = [[1, 2, 3], [4, 5, 6]]

row = matrix[0]

row.reverse()

print(matrix)
```

Output:

```python
[
    [3, 2, 1],
    [4, 5, 6]
]
```

Why did the original matrix change?

Because:

```python
row = matrix[0]
```

does not create another list.

Both `row` and `matrix[0]` refer to the same list object in memory.

Therefore, modifying `row` also modifies `matrix[0]`.

**Remember:**

- `row = matrix[0]` → Reference to the original inner list.
- `row = matrix[0].copy()` → Creates a shallow copy of that inner list.
- `row.reverse()` → Modifies the list directly.
- `row[::-1]` → Creates a new reversed list.

### Alternative Way Using Indexing

Instead of:

```python
for row in matrix:
    row.reverse()
```

We can also write:

```python
for i in range(len(matrix)):
    matrix[i].reverse()
```

Both approaches work.

---

## 6. Complete Python Solution

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse every individual row
        for row in matrix:
            row.reverse()
```

**Note:** LeetCode expects the original matrix to be modified. Returning a new matrix is not required.

---

## 7. Can We Optimize This Algorithm?

Let's analyze the complexity.

| Operation | Time Complexity |
|---|---|
| Transpose | O(N²) |
| Reverse every row | O(N²) |
| Total | O(N²) |

### Space Complexity

**Auxiliary Space: O(1)**

Why?

- We don't create another matrix.
- We don't create another list to store the rotated result.
- We use only a constant number of extra variables.
- We modify the original matrix using swapping.

### Is O(N²) the Best Possible Time Complexity?

Yes, asymptotically.

An N x N matrix contains N² elements. A rotation requires all elements to be placed in their correct positions.

Therefore, the time complexity cannot be reduced below O(N²) for a general matrix rotation.

### Other Possible Approach: Four-Way Swapping

We can also rotate the matrix directly by swapping four elements at a time.

For example, in a 3 x 3 matrix:

```text
1  2  3
4  5  6
7  8  9
```

The outer four corners move like this:

```text
1 -> 3
3 -> 9
9 -> 7
7 -> 1
```

This can be implemented layer by layer using temporary variables.

Its complexity is also:

- Time: O(N²)
- Auxiliary Space: O(1)

However, it is more complicated to implement.

**Recommended approach: Transpose + Reverse Rows.**

It is easier to understand, debug, and explain in interviews. There is no asymptotic time or auxiliary-space improvement from switching to four-way swapping.

---

## 8. Important Python List Operations

These operations are useful in array and matrix problems.

| Operation | Meaning | In-place? |
|---|---|---|
| `arr.reverse()` | Reverses the original list | Yes |
| `arr[::-1]` | Creates a reversed copy | No |
| `arr.sort()` | Sorts the original list | Yes |
| `sorted(arr)` | Creates a sorted list | No |
| `arr.append(10)` | Adds an element | Yes |
| `arr.copy()` | Creates a shallow copy | No |
| `arr[i], arr[j] = arr[j], arr[i]` | Swaps two elements | Yes |

### Important Difference: reverse() vs [::-1]

```python
arr = [1, 2, 3]

arr.reverse()
```

This modifies the original list.

But:

```python
arr = [1, 2, 3]

new_arr = arr[::-1]
```

This creates a new list and leaves the original unchanged.

---

## 9. Interview Questions and Answers

**Q1. What is an in-place algorithm?**

An in-place algorithm modifies the original data structure without creating another data structure of comparable size to store the result.

**Q2. What is matrix transposition?**

Matrix transposition means converting rows into columns and columns into rows.

**Q3. Why do we use `j = i + 1` during transposition?**

To avoid swapping diagonal elements and to prevent swapping the same pair twice.

**Q4. Why do we reverse every row after transposing?**

Transposition alone does not produce a clockwise rotation. Reversing each row after transposition completes the 90-degree clockwise rotation.

**Q5. Why does `for row in matrix` modify the original matrix?**

Because `row` refers to the actual inner list inside the matrix. It is not a separate copy.

**Q6. What is the difference between `reverse()` and `[::-1]`?**

`reverse()` modifies the original list, whereas `[::-1]` creates a new reversed list.

**Q7. What is the time complexity?**

O(N²), because we process the matrix elements during transposition and row reversal.

**Q8. What is the auxiliary space complexity?**

O(1), because we modify the original matrix without allocating another matrix.

**Q9. Can we rotate the matrix without transposing?**

Yes. We can use layer-by-layer four-way swapping.

**Q10. Why does this solution require a square matrix?**

The problem requires an N x N matrix. Transposing a non-square matrix changes its dimensions, making this particular in-place approach unsuitable without additional rearrangement.

---

## 10. Key Takeaways

Remember these four things:

1. **In-place:** Modify the original matrix without creating another matrix.
2. **Transpose:** Swap `matrix[i][j]` with `matrix[j][i]`.
3. **Avoid duplicate swaps:** Start the inner loop at `i + 1`.
4. **Reverse rows:** Use `for row in matrix: row.reverse()`.

### Final Complexity

| Complexity | Value |
|---|---|
| Time Complexity | O(N²) |
| Auxiliary Space | O(1) |
| Approach | Transpose + Reverse Rows |
| In-place | Yes |

---
