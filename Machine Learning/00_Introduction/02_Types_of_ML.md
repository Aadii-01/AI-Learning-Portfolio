# **Types of ML (Based on Supervision Required)**
Machine learning can be classified based on how much supervision or labeled output data is available during training.

The main categories are:
- **Supervised Learning**
- **Unsupervised Learning**
- **Semi-Supervised Learning**
- **Reinforcement Learning**

***

## **Supervised Learning**
In supervised learning, the model is trained using both **input data** and the **correct output**. The goal is to learn the relationship between input and output so that when a new input comes, the model can predict the correct output.

In simple words:
```text
Input + Correct Output -> Learn relationship -> Predict output for new input
```

### **Types of Supervised Learning**
The type depends on the nature of the output:

| **Output Type** | **ML Task** | **Meaning** |
|---------|---------|---------|
| Numerical / Continuous | Regression | Predicts a numeric value |
| Categorical / Discrete | Classification | Predicts a category or class |

### **Regression**
Regression is used when the output is a number.

**Examples:**
- Given house features such as area, number of rooms, and location, predict the **house price**.
- Given previous sales data, predict future sales.
- Given temperature and humidity values, predict electricity usage.

### **Classification**
Classification is used when the output belongs to a category.

**Examples:**
- Predict whether an email is **spam or not spam**.
- Predict whether it **will rain or not** based on weather conditions.
- Predict whether a patient has a disease or not.

### **Key Idea**
Supervised learning works well when historical examples with correct answers are available.

***

## **Unsupervised Learning**
In unsupervised learning, only the **input data** is given. There is no output label provided to the model.

The goal is to discover hidden patterns, structures, or relationships inside the data.

In simple words:
```text
Input only -> Find hidden structure / pattern
```

### **Main Types of Unsupervised Learning**
- **Clustering**
- **Dimensionality Reduction**
- **Anomaly Detection**
- **Association Rule Learning**

### **Clustering**
Clustering means grouping similar data points together.

**Example:** Customer segmentation, where users with similar buying behavior are grouped into the same cluster.

### **Dimensionality Reduction**
Dimensionality reduction means reducing the number of input features or columns while keeping the most useful information.

It is helpful for:
- Removing unnecessary columns
- Reducing complexity
- Speeding up training
- Visualization of high-dimensional data

**Example:** In the **MNIST** digit dataset, many pixel values can be compressed into fewer dimensions to visualize handwritten digits more clearly.

### **Anomaly Detection**
Anomaly detection is used to identify unusual or rare data points that do not behave like normal data.

**Examples:**
- Fraud detection in banking transactions
- Detecting faulty sensors
- Finding outliers in a dataset before training

### **Association Rule Learning**
Association rule learning finds relationships between items that often appear together.

**Classic Example:** The famous **diaper and beer** case study in retail, where stores observe that customers who buy diapers may also buy beer. This helps in product placement and recommendations.

***

## **Semi-Supervised Learning**
Semi-supervised learning is a mixture of supervised and unsupervised learning.

In this approach, only some data points are labeled, while the rest are unlabeled. The model uses the small labeled set and the larger unlabeled set together to improve learning.

### **How it works**
A few examples are labeled manually, and then the model tries to label or understand the remaining examples based on similarity and patterns.

**Example:** In **Google Photos**, a user may label one or two photos of a person, and then the system groups and labels similar photos automatically.

### **Why it is useful**
Labeling data manually is expensive and time-consuming. Semi-supervised learning reduces the amount of labeling effort required.

***

## **Reinforcement Learning**
In reinforcement learning, the model is not trained with a fixed labeled dataset in the usual way. Instead, it learns by interacting with an environment, making decisions, and receiving **rewards** or **penalties**.

The goal is to learn what actions lead to the highest long-term reward.

In simple words:
```text
Agent -> Takes action -> Gets reward or punishment -> Improves strategy
```

### **Analogy**
It is similar to training a dog: good behavior gets rewarded, and wrong behavior gets punished.

### **Examples**
- **Self-driving cars**, where the system learns better driving behavior over time.
- **Game-playing agents**, such as DeepMind's **AlphaGo**, which learned to play the game of Go at a very high level.

### **Key Idea**
The model starts learning from scratch and improves through trial and error.

***

## **Quick Comparison of Supervision-Based Types**
| **Type** | **Input Given** | **Output Given** | **Goal** | **Example** |
|---------|------------------|------------------|---------|-------------|
| Supervised | Yes | Yes | Learn input-output mapping | House price prediction |
| Unsupervised | Yes | No | Find hidden patterns | Customer clustering |
| Semi-Supervised | Yes | Partially | Learn from few labels and many unlabeled points | Google Photos face grouping |
| Reinforcement | No fixed labeled dataset | Reward / Punishment signal | Learn through interaction | AlphaGo, self-driving cars |

***

# **Types of ML (Based on Training During Production)**
Another way to classify machine learning is based on **how training happens after deployment or during production use**.

The two major types are:
- **Batch (Offline) Learning**
- **Online Learning**

***

## **Batch / Offline Learning**
In batch learning, the model is trained using the **entire available dataset at once**. After training is complete, the model is deployed to the server for prediction.

### **Flow**
```text
Whole data -> Train model -> Test model -> Deploy to server
```

### **Problem with Batch Learning**
Batch learning usually works on old or previously collected data. If the real-world data keeps changing, the model may become outdated.

This means:
- It is more **static**
- It does not adapt immediately to new data
- Updating the model requires retraining again

### **Retraining Process**
```text
Old data + New data -> Train again in batch -> New model
```

### **Disadvantages**
- Requires a lot of data at once
- Needs strong hardware and storage
- Retraining can be slow
- Not suitable when data changes rapidly

### **Example**
If a major event suddenly changes user behavior, such as a policy change or a big economic event, a batch-trained system may respond late because it updates only after retraining.

***

## **Online Learning**
In online learning, the model is trained **incrementally**. Instead of waiting for the full dataset, it learns from data in small parts, often called mini-batches or sequential updates.

### **Idea**
As more users interact with the product, the model can improve continuously.

### **Flow**
```text
New data arrives -> Small update to model -> Improved model
```

### **Examples**
- Recommendation systems on **YouTube**
- Feed ranking on **Instagram**
- Systems that improve with continuous user interaction

### **When to Use Online Learning**
- When there is **data drift** (data patterns change over time)
- When faster updates are needed
- When it is more cost-effective to train in smaller pieces
- When full retraining is too expensive or too slow

### **How to Implement**
Some common tools and methods are:
- **Scikit-learn**: `SGDRegressor` with `partial_fit()`
- **River library** for streaming machine learning
- **Vowpal Wabbit** for efficient large-scale online learning

### **Learning Rate**
Online learning usually depends heavily on the **learning rate**, which controls how much the model changes after seeing new data.

If the learning rate is too high, learning may become unstable. If it is too low, learning may become very slow.

### **Disadvantages**
- Tricky to design correctly
- Risky if bad data enters continuously
- Errors may spread quickly if monitoring is weak

***

## **Batch vs Online Learning**
| **Feature** | **Batch / Offline Learning** | **Online Learning** |
|---------|-----------------------------|---------------------|
| Training style | Entire dataset at once | Incremental updates |
| Adaptation to new data | Slow | Fast |
| Best for | Stable data | Dynamic or changing data |
| Compute requirement | Heavy training jobs | Smaller frequent updates |
| Retraining | Needed again and again | Continuous improvement possible |
| Risk | Becomes outdated | Can learn wrong patterns if not monitored |

***

# **Types of ML (Based on How the Model Learns)**
Machine learning can also be classified by **how the model learns from data internally**.

The two common categories are:
- **Instance-Based Learning**
- **Model-Based Learning**

***

## **Instance-Based Learning (Lazy Learners)**
Instance-based learning mainly works by **memorizing** training examples.

Instead of building a general formula immediately, it stores the examples and compares new data points with previously seen ones.

### **Why it is called Lazy Learning**
It is called a lazy learner because it does not do much generalization during training. Most of the work happens later at prediction time.

### **Idea**
```text
Store examples -> Compare new input with stored examples -> Predict based on similarity
```

### **Example**
A nearest neighbors model checks which past examples are most similar to the new input and then predicts using those nearby examples.

### **Characteristics**
- Simple and intuitive
- Training is fast because it mostly stores data
- Prediction can be slower because comparisons happen at runtime
- Memory usage can be high

***

## **Model-Based Learning**
Model-based learning tries to learn the **underlying principles**, patterns, or rules present in the data.

Instead of memorizing all examples, it creates a model that captures the important relationship between inputs and outputs.

### **Idea**
```text
Training data -> Learn pattern / equation / structure -> Build model -> Predict on new data
```

### **Example**
Linear regression learns a mathematical relationship between inputs and outputs instead of storing every training point.

### **Characteristics**
- Tries to generalize from data
- Usually faster at prediction time
- Often requires a proper training phase
- Can perform well even without storing all original examples

***

## **Instance-Based vs Model-Based Learning**
| **Feature** | **Instance-Based Learning** | **Model-Based Learning** |
|---------|------------------------------|--------------------------|
| Main idea | Memorize examples | Learn general pattern |
| Training effort | Low | Higher |
| Prediction speed | Slower | Faster |
| Memory usage | High | Usually lower |
| Generalization | Based on similarity to stored data | Based on learned model |
| Example | K-Nearest Neighbors | Linear Regression, Decision Tree |

***

## **Key Points to Remember**
- Supervised learning uses both inputs and outputs.
- Unsupervised learning uses only inputs and finds hidden patterns.
- Semi-supervised learning uses a small amount of labeled data and a large amount of unlabeled data.
- Reinforcement learning learns using rewards and punishments.
- Batch learning trains on full data at once, while online learning updates incrementally.
- Instance-based learning memorizes data, while model-based learning learns patterns.

***

## **One-Line Revision**
Machine learning can be classified based on supervision, production-time training style, and the way the model learns from data.