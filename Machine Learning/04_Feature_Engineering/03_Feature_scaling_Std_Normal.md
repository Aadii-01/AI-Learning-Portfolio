# Feature Scaling

## Introduction

**Feature Scaling** is a data preprocessing technique used to bring numerical features onto a common scale. Since different features can have vastly different ranges (e.g., Age: 18–60 vs Salary: 20,000–2,000,000), scaling ensures that no single feature dominates the learning process.

Feature scaling is generally divided into two major techniques:

1. **Standardization (Z-Score Normalization)**
2. **Normalization**

---

# Why is Feature Scaling Needed?

Feature scaling is performed to ensure **fairness** and **efficiency** during model training.

### Benefits

- Prevents features with larger values from dominating smaller-valued features.
- Makes all features contribute equally.
- Accelerates convergence during optimization.
- Improves model accuracy for many Machine Learning algorithms.
- Makes distance calculations more meaningful.

---

# Standardization (Z-Score Normalization)

## Definition

**Standardization** (also called **Z-Score Normalization**) transforms data so that it has:

- **Mean = 0**
- **Standard Deviation = 1**

Instead of restricting data to a fixed range, it centers the data around zero while preserving the original distribution.

---

## Formula

\[
z = \frac{x_i - \bar{x}}{\sigma}
\]

where,

- \(x_i\) = Current value
- \(\bar{x}\) = Mean of the feature
- \(\sigma\) = Standard deviation

---

## Properties

After standardization:

- Mean = **0**
- Standard Deviation = **1**
- Data is centered around zero.
- Original distribution is preserved.

This process is known as **Mean Centering** because every value is shifted relative to the mean.

---

## Effect of Standard Deviation

### If Standard Deviation > 1

Data values are **compressed (squished)** closer together after scaling.

```text
Original Data

|     |          |      |        |

After Standardization

|  | | | | |
```

---

### If Standard Deviation < 1

Data values are **expanded** farther apart after scaling.

```text
Original Data

| | | | |

After Standardization

|      |         |          |          |
```

---

## Why Logistic Regression Needs Standardization

Although Logistic Regression can work without scaling, **standardization generally improves performance** because:

- Gradient Descent converges faster.
- Feature weights are learned more efficiently.
- Numerical optimization becomes more stable.
- Accuracy may improve, especially when feature ranges differ significantly.

---

# When Should Standardization Be Used?

| Algorithm | Why Standardization is Applied |
|-----------|--------------------------------|
| **K-Means Clustering** | Uses Euclidean distance; features with larger scales dominate the distance calculation. |
| **K-Nearest Neighbors (KNN)** | Distance between samples is directly affected by feature magnitudes. |
| **Principal Component Analysis (PCA)** | PCA finds directions of maximum variance. Features with larger scales can dominate the principal components. |
| **Artificial Neural Networks (ANNs)** | Helps Gradient Descent converge faster and improves training stability. |
| **Gradient Descent-based Algorithms** | Faster and smoother optimization due to similarly scaled features. |

---

# Normalization

## Definition

**Normalization** is a feature scaling technique that transforms numerical values to a common scale **without distorting the relationships between data points**.

Unlike standardization, normalization typically scales values to a fixed range such as **[0,1]**.

---

## Types of Normalization

- Min-Max Scaling
- Mean Normalization
- Max Absolute Scaling
- Robust Scaling

---

# 1. Min-Max Scaling

## Formula

\[
x_i'=\frac{x_i-x_{min}}{x_{max}-x_{min}}
\]

### Range

\[
[0,1]
\]

### Geometric Representation

```text
Original Scale

20-------------------------80-------------------------150

Min-Max Scaling

0--------------------------0.46------------------------1
```

### Advantages

- Most commonly used normalization technique.
- Preserves relationships between values.
- Produces values strictly between 0 and 1.

---

# 2. Mean Normalization

## Formula

\[
x_i'=\frac{x_i-\bar{x}}{x_{max}-x_{min}}
\]

where

- \(\bar{x}\) = Mean of the feature

### Properties

- Values less than the mean become **negative**.
- Values greater than the mean become **positive**.
- Mean becomes approximately zero.

### Useful When

Algorithms require centered data while keeping values within a limited range.

---

# 3. Max Absolute Scaling

## Formula

\[
x_i'=\frac{x_i}{|x_{max}|}
\]

where

- \(|x_{max}|\) = Maximum absolute value

### Properties

- Values lie between **-1 and 1**.
- Does not shift the data.
- Preserves sparsity.

### Useful For

Sparse datasets containing many zero values (e.g., text data represented using TF-IDF or Bag of Words).

---

# 4. Robust Scaling

## Formula

\[
x_i'=\frac{x_i-\text{Median}}{\text{IQR}}
\]

where

\[
IQR=Q_3-Q_1
\]

- \(Q_3\) = 75th Percentile
- \(Q_1\) = 25th Percentile

### Properties

- Uses **Median** instead of Mean.
- Uses **Interquartile Range (IQR)** instead of Standard Deviation.
- Much less affected by outliers.

### Suitable When

The dataset contains a large number of outliers.

> **Scikit-learn Class:** `RobustScaler`

---

# Standardization vs Normalization

| Feature | Standardization | Normalization |
|----------|-----------------|---------------|
| Also Known As | Z-Score Normalization | Feature Normalization |
| Output Range | No fixed range | Usually [0,1] or [-1,1] |
| Centered Around Zero | Yes | Depends on the method |
| Uses Mean | Yes | Sometimes |
| Sensitive to Outliers | Yes | Depends on the normalization technique |
| Most Commonly Used | Yes | Only for specific use cases |

---

# Which One Should You Use?

### Standardization

Use when:

- Most Machine Learning algorithms are being used.
- Features have different units.
- Data approximately follows a normal distribution.
- Using Logistic Regression, SVM, KNN, PCA, Neural Networks, or Gradient Descent-based models.

---

### Normalization

Use when:

- The minimum and maximum values of features are known.
- A fixed range (such as [0,1]) is required.
- Working with image processing, deep learning inputs, or algorithms expecting bounded values.

---

# Key Takeaways

- **Feature Scaling** improves fairness, optimization, and model performance.
- **Standardization (Z-Score Normalization)** transforms data to have **Mean = 0** and **Standard Deviation = 1**.
- **Normalization** rescales values to a fixed range, most commonly **[0,1]**.
- Standardization is generally the preferred choice for most Machine Learning algorithms.
- Min-Max Scaling is useful when the feature's minimum and maximum values are known.
- Robust Scaling is the best choice when the dataset contains many outliers.