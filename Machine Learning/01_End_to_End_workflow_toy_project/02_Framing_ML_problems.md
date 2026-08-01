# Framing the Problem (Business Problem → Machine Learning Problem)

> **Goal:** Convert a real-world business problem into a well-defined Machine Learning problem.

---

# Why Problem Framing is Important

Before writing a single line of ML code, the most important task is understanding:

- What is the business trying to achieve?
- Can Machine Learning solve it?
- Which type of ML problem is it?
- What data is required?
- How will success be measured?

This process is known as **Problem Framing**.

---

# General Workflow

```text
Business Problem
        │
        ▼
Understand Business Objective
        │
        ▼
Convert to ML Problem
        │
        ▼
Collect Data
        │
        ▼
Train ML Model
        │
        ▼
Deploy Model
        │
        ▼
Measure Business Impact
```

---

# Case Study: Netflix

## Business Objective

Netflix wants to **increase its revenue**.

Revenue can be increased in multiple ways:

### 1. Acquire More Customers

- Improve marketing
- Better recommendations
- Increase brand awareness

---

### 2. Increase Revenue from Existing Customers

Examples:

- Upgrade users to premium plans
- Introduce new subscription plans
- Charge more for additional features

---

### 3. Reduce Customer Churn ⭐

The cheapest way to increase revenue is often **retaining existing customers**.

Instead of constantly finding new users, Netflix wants existing users to continue their subscriptions.

---

# What is Churn Rate?

**Churn Rate** = Percentage of customers who stop using the service.

Example:

Total customers = **100**

Customers who leave = **2**

```text
Churn Rate = (2 / 100) × 100
            = 2%
```

Meaning:

- ✅ 98 customers stay
- ❌ 2 customers leave

Lower churn rate = Higher revenue.

---

# Converting Business Problem into an ML Problem

## Business Problem

> Reduce customer churn.

Now ask:

> Can Machine Learning help?

Yes.

The ML model can identify customers who are likely to leave before they actually cancel.

---

# Big Picture Thinking

Always ask:

> **What should the final product do?**

Instead of thinking:

> "I want to build a Random Forest."

Think:

> "I want software that predicts which customers are likely to leave."

The ML algorithm is only one component of the final solution.

---

# ML Problem Statement

Predict whether a customer is likely to leave Netflix.

---

# Possible Solutions After Prediction

Once high-risk customers are identified, Netflix can:

- Offer discounts
- Provide personalized recommendations
- Send retention offers
- Improve content suggestions
- Understand why customers are leaving

The ML model predicts **who may leave**. The business decides **how to retain them**.

---

# Identify the Type of Machine Learning Problem

## Supervised Learning

Historical data contains:

- Customer information
- User behavior
- Whether the customer left or not

Since labeled data is available, this becomes a **Supervised Learning** problem.

---

## Classification Problem

Predict:

```text
Will the customer leave?
```

Possible outputs:

- Leave
- Not Leave

Binary output:

```text
0 → Stay

1 → Leave
```

Therefore:

> **Binary Classification**

---

## Regression (Alternative)

Instead of predicting **Yes/No**, we could predict:

- Probability of leaving
- Expected remaining subscription duration
- Lifetime value of a customer

These are **Regression** problems because the output is continuous.

---

# Existing Solution

Suppose Netflix already has software that estimates churn.

Our objective is to:

- Improve prediction accuracy
- Reduce false alarms
- Predict earlier
- Increase customer retention

This is common in real-world ML projects—you often improve an existing system rather than build one from scratch.

---

# Data Collection

The ML model is only as good as its data.

Possible features include:

| Feature | Why It Matters |
|----------|----------------|
| Watch time | Lower watch time may indicate reduced engagement. |
| Searches with no results | Users unable to find desired content may become dissatisfied. |
| Content abandoned midway | Frequent incomplete viewing may indicate loss of interest. |
| Clicks on recommendations | Measures recommendation quality and user engagement. |

Additional features (possible):

- Subscription plan
- Device type
- Login frequency
- Session duration
- Time since last login
- Ratings provided
- Number of profiles
- Viewing history

---

# Role of the Data Engineer

The data engineer is responsible for collecting and preparing data for ML.

Typical data flow:

```text
Netflix Application
        │
        ▼
OLTP Database
(Transactional Data)
        │
        ▼
ETL / ELT Pipeline
        │
        ▼
Data Warehouse
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Model
```

### OLTP (Online Transaction Processing)

Stores live operational data such as:

- User logins
- Watch history
- Searches
- Recommendations
- Subscription activity

---

### Data Warehouse

Stores cleaned and historical data optimized for analytics and ML.

The warehouse becomes the primary data source for model training.

---

# Choosing Evaluation Metrics

Model performance should be measured objectively.

Examples:

### 1. Compare Predictions with Reality

```text
Actually Left
vs
Predicted Left
```

This is represented using a **Confusion Matrix**.

---

### 2. Check Prediction Quality

Questions to evaluate:

- How many predicted churn users actually left?
- How many customers who left were correctly identified?
- How many loyal customers were incorrectly predicted as churn?

Common evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

# Online Learning vs Batch Learning

## Batch Learning

```text
OLTP
   │
   ▼
Data Warehouse
   │
   ▼
Train Model
   │
   ▼
Deploy
```

Characteristics:

- Model trained periodically
- Suitable when data changes slowly
- Easier to maintain

Example:

Retrain every week or month.

---

## Online Learning

```text
New User Data
        │
        ▼
Model Updates Continuously
```

Characteristics:

- Learns continuously from new data
- Suitable for streaming data
- Adapts quickly to changing user behavior
- More complex to implement

---

# Check Assumptions Before Building the Model

Machine Learning is built on assumptions.

Ask questions such as:

### Should geography matter?

Examples:

- Country
- State
- City

User behavior may vary across different regions.

---

### Should demographics matter?

Examples:

- Age
- Gender
- Language
- Occupation

These attributes may influence viewing preferences and churn.

---

### Other Possible Assumptions

- Does subscription plan affect churn?
- Does device type matter?
- Does internet quality influence engagement?
- Does content availability vary by region?
- Does watch time correlate with churn?

These assumptions should be validated using **Exploratory Data Analysis (EDA)** before finalizing the model.

---

# End-to-End Pipeline

```text
Business Problem
        │
        ▼
Increase Revenue
        │
        ▼
Reduce Customer Churn
        │
        ▼
Frame ML Problem
(Binary Classification)
        │
        ▼
Collect User Data
(OLTP)
        │
        ▼
Data Warehouse
        │
        ▼
Feature Engineering
        │
        ▼
Train Classification Model
        │
        ▼
Evaluate Performance
        │
        ▼
Deploy Model
        │
        ▼
Predict Customers Likely to Churn
        │
        ▼
Business Takes Action
(Discounts, Recommendations, Offers, etc.)
```

---

# Key Takeaways

- Start with the **business problem**, not the algorithm.
- Convert the business objective into a clear **ML problem statement**.
- Think about the **final product** and how it creates business value.
- Identify the appropriate ML task (e.g., classification or regression).
- Collect relevant data and build a reliable data pipeline.
- Evaluate the model using suitable performance metrics.
- Validate assumptions using EDA before training.
- Remember: the ML model predicts outcomes, while the business decides the actions to improve results.