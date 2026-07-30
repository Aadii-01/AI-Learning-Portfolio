# Tensors (Important Concept for Machine Learning & Deep Learning)

---

# What is a Tensor?

A **Tensor** is simply a **data structure used to store numbers**.

It is the fundamental data structure used throughout **Machine Learning** and **Deep Learning**.

Almost every ML/DL library internally works with tensors.

Examples:
- Scikit-Learn
- TensorFlow
- PyTorch
- JAX
- NumPy (ND Arrays)

Although tensors can technically store strings or characters, **they are almost always used to store numerical data**.

---

# Why Should We Learn Tensors?

Every Machine Learning problem eventually converts data into tensors.

Examples:

- Images → Tensors
- Audio → Tensors
- Videos → Tensors
- Text → Tensors
- Tabular datasets → Tensors

Without understanding tensors, it becomes difficult to understand:

- Neural Networks
- TensorFlow
- PyTorch
- Matrix Operations
- Deep Learning Mathematics

---

# Tensor = N-Dimensional Array

A tensor is simply an **N-Dimensional Array (ND Array).**

| Dimension | Name |
|-----------|------|
| 0 | Scalar |
| 1 | Vector |
| 2 | Matrix |
| 3 | 3D Tensor |
| n | n-D Tensor |

---

# 1. 0-D Tensor (Scalar)

A tensor containing **only one value**.

Examples

```
2
```

```
15
```

```
-8
```

Dimension

```
ndim = 0
```

Diagram

```
+----+
|  5 |
+----+
```

There are **no axes**.

---

# 2. 1-D Tensor (Vector)

A collection of numbers arranged in one direction.

Example

```t
[1,2,3,4]
```

Also called

- Vector
- Array
- 1D Array
- 1D Tensor

Dimension

```t
ndim = 1
```

Rank

```t
Rank = 1
```

Shape

```t
(4,)
```

because it contains four elements.

Diagram

```t
Axis 0

[1] [2] [3] [4]
```

Only one axis exists.

---

## Vector Dimension vs Tensor Dimension

Consider

```
[8.1,91,0]
```

This is

- 1-D Tensor ✔
- Vector of Dimension 3 ✔

The tensor dimension is still **1** because it has only one axis.

The vector dimension is **3** because it contains three components.

---

# Student Database Example (1D Tensor)

Suppose the database columns are

| CGPA | IQ | State |
|------|----|-------|
| 8.1 | 91 | 0 |

One student's record becomes

```t
[8.1,91,0]
```

Visualization

```text
           IQ
            ^
            |
            |
            |
            |
            |
            |
            O---------> CGPA
           /
          /
         /
      State
```

The vector has **3 components**, but it is still a **1D Tensor**.

---

# Important Formula

An **n-D Tensor** is formed by collecting multiple **(n−1)-D Tensors**.

Examples

```t
Collection of Scalars
        ↓
1D Tensor

Collection of 1D Tensors
        ↓
2D Tensor

Collection of 2D Tensors
        ↓
3D Tensor
```

---

# 3. 2-D Tensor (Matrix)

A collection of multiple vectors.

Example

```text
[
 [1,2,3],
 [2,3,4]
]
```

Dimension

```text
ndim = 2
```

Rank

```text
2
```

Shape

```t
(2,3)
```

Meaning

- 2 rows
- 3 columns

Diagram

```t
        Axis 1
      ------------
Axis0 |1 2 3|
      |2 3 4|
      ------------
```

Two axes exist.

---

# Student Database Example (2D Tensor)

Each row is one student.

| CGPA | IQ | State |
|------|----|-------|
|8.1|91|0|
|7.5|84|1|
|9.0|105|0|
|8.7|95|1|

Tensor

```t
[
 [8.1,91,0],
 [7.5,84,1],
 [9.0,105,0],
 [8.7,95,1]
]
```

This is simply a collection of multiple 1D tensors.

---

# 4. 3-D Tensor

A collection of multiple matrices.

Think of stacking matrices one behind another.

Diagram

```t
Layer 1

┌─────────┐
│ Matrix  │
└─────────┘

Layer 2

┌─────────┐
│ Matrix  │
└─────────┘

Layer 3

┌─────────┐
│ Matrix  │
└─────────┘
```

Shape Example

```t
(3,4,5)

3 matrices
4 rows
5 columns
```

---

# NLP Example (3D Tensor)

Suppose we have two sentences

```t
Hi A

Hi B
```

Vocabulary

```t
Hi
A
B
C
```

One-hot Encoding

| Word | Vector |
|-------|---------|
|Hi|[1,0,0,0]|
|A|[0,1,0,0]|
|B|[0,0,1,0]|
|C|[0,0,0,1]|

Now

Sentence 1

```t
Hi A
```

becomes

```t
[
 [1,0,0,0],
 [0,1,0,0]
]
```

Sentence 2

```t
Hi B
```

becomes

```
[
 [1,0,0,0],
 [0,0,1,0]
]
```

The entire dataset becomes

```t
[
 [
  [1,0,0,0],
  [0,1,0,0]
 ],

 [
  [1,0,0,0],
  [0,0,1,0]
 ]
]
```

This is a **3D Tensor**.

---

# 5. 4-D Tensor

A collection of multiple 3D tensors.

Most commonly used for **Image Datasets**.

Each image consists of

- Height
- Width
- RGB Channels

Dataset consists of many images.

Diagram

```t
Dataset
   │
   ├── Image 1
   │      ├── R
   │      ├── G
   │      └── B
   │
   ├── Image 2
   │      ├── R
   │      ├── G
   │      └── B
   │
   └── Image n
```

Typical Shape

```t
(Number of Images,
 Height,
 Width,
 Channels)
```

Example

```t
(1000,224,224,3)
```

Meaning

- 1000 Images
- 224 Height
- 224 Width
- RGB Channels

---

# 6. 5-D Tensor

Most commonly used for **Video Processing**.

A video is a collection of frames.

Each frame is an image.

Images already require 4 dimensions.

Therefore,

Videos require one more dimension.

Example

Suppose

- 4 videos
- 60 seconds
- 30 FPS
- Resolution = 480 × 720
- RGB channels

Frames

```
60 × 30 = 1800 frames
```

Tensor Shape

```
(
4,
1800,
480,
720,
3
)
```

Meaning

| Dimension | Meaning |
|-----------|---------|
|4|Videos|
|1800|Frames|
|480|Height|
|720|Width|
|3|RGB Channels|

---

# Rank

Rank means

- Number of Dimensions
- Number of Axes

Examples

| Tensor | Rank |
|---------|------|
|5|0|
|[1,2,3]|1|
|[[1,2],[3,4]]|2|
|3D Tensor|3|
|Image Dataset|4|

---

# Shape

Shape tells **how many elements exist along each axis**.

Examples

| Tensor | Shape |
|---------|--------|
|5|()|
|[1,2,3]|(3,)|
|[[1,2],[3,4]]|(2,2)|
|Image Dataset|(1000,224,224,3)|

---

# Rank vs Shape

| Rank | Shape |
|------|--------|
|Number of axes|Size along each axis|
|Integer|Tuple|
|Represents dimensions|Represents structure|

Example

Tensor

```t
[
 [1,2,3],
 [4,5,6]
]
```

Rank

```t
2
```

Shape

```t
(2,3)
```

---

# Summary

| Tensor Type | Real-life Example |
|-------------|-------------------|
|0D|Single Number|
|1D|One Student Record|
|2D|Student Database|
|3D|Collection of Sentences / NLP Data|
|4D|Image Dataset|
|5D|Video Dataset|

---

# Key Takeaways

- Tensor = N-Dimensional Array.
- Rank = Number of Dimensions (Axes).
- Shape = Number of values along each axis.
- An n-D tensor is formed by combining multiple (n−1)-D tensors.
- Images are generally represented as 4D tensors.
- Videos are generally represented as 5D tensors.
- Understanding tensors is essential before learning TensorFlow, PyTorch, CNNs, and Deep Learning.