import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide"
)

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------

from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "iris_decision_tree.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------
DATA_PATH = BASE_DIR / "data" / "iris.csv"

df = pd.read_csv(DATA_PATH)

# ----------------------------------------------------
# Model Evaluation
# ----------------------------------------------------

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

cm = confusion_matrix(y_test, y_pred)



# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("🌸 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Dataset",
        "EDA",
        "Prediction",
        "Model Performance",
        "About"
    ]
)


# ===================================================
# HOME PAGE
# ===================================================

if page == "Home":

    st.title("🌸 Iris Flower Classification")

    st.write("---")

    st.markdown("""
    ## Welcome

    This application predicts the species of an Iris flower
    using Machine Learning.

    ### Flower Species

    - Setosa
    - Versicolor
    - Virginica

    ### Features Used

    - Sepal Length
    - Sepal Width
    - Petal Length
    - Petal Width

    ### Machine Learning Algorithm

    Decision Tree Classifier
    """)

    st.success("Select a page from the sidebar.")


# ===================================================
# DATASET PAGE
# ===================================================

elif page == "Dataset":

    st.title("📊 Dataset")

    st.subheader("First Five Rows")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    st.write(df.shape)

    st.subheader("Columns")

    st.write(df.columns)

    st.subheader("Statistical Summary")

    st.dataframe(df.describe())

    st.subheader("Data Types")

    st.write(df.dtypes)

# ===================================================
# EDA PAGE
# ===================================================

elif page == "EDA":

    st.title("📈 Exploratory Data Analysis")

    st.markdown("""
    Explore the visualizations created during the analysis of the Iris dataset.
    These plots help us understand the relationships, distributions, and importance
    of different flower features.
    """)

    st.divider()

    # -------------------------
    # Row 1
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌸 Count Plot")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(IMAGE_DIR / "countplot.png", use_container_width=True)
        st.caption(
    "Shows the number of flowers belonging to each species. "
    "The dataset is perfectly balanced."
)

    with col2:
        st.subheader("📊 Histogram")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(
            IMAGE_DIR / "histogram.png",
            use_container_width=True
        )
        st.caption(
    "Displays the distribution of each numerical feature."
)

    st.divider()

    # -------------------------
    # Row 2
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔥 Correlation Heatmap")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(IMAGE_DIR / "heatmap.png", use_container_width=True)
        st.caption(
    "Shows correlations between the four flower measurements."
)

    with col2:
        st.subheader("🎯 Scatter Plot")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(
            IMAGE_DIR / "scatterplot.png",
            use_container_width=True
        )
        st.caption(
    "Petal Length and Petal Width clearly separate the species."
)

    st.divider()

    # -------------------------
    # Pair Plot
    # -------------------------

    st.subheader("🌼 Pair Plot")
    IMAGE_DIR = BASE_DIR / "images"

    st.image(
        IMAGE_DIR / "pairplot.png",
        use_container_width=True
    )
    st.caption(
    "Visualizes pairwise relationships among all features."
)

    st.divider()

    # -------------------------
    # Row 3
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Box Plot")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(
            IMAGE_DIR / "boxplot.png",
            use_container_width=True
        )
        st.caption(
    "Highlights the spread of values and potential outliers."
)

    with col2:
        st.subheader("📈 Feature Importance")
        IMAGE_DIR = BASE_DIR / "images"
        st.image(
            IMAGE_DIR / "feature_importance.png",
            use_container_width=True
        )
        st.caption(
    "Displays how much each feature contributes to the Decision Tree's predictions."
)

    st.divider()

    # -------------------------
    # Confusion Matrix
    # -------------------------

    st.subheader("🤖 Confusion Matrix")
    IMAGE_DIR = BASE_DIR / "images"
    st.image(
        IMAGE_DIR / "confusion_matrix.png",
        use_container_width=True
    )
    st.caption(
    "Summarizes the model's prediction performance by comparing actual and predicted classes."
)

    st.success("EDA Completed Successfully ✅")


# ===================================================
# PREDICTION PAGE
# ===================================================



elif page == "Prediction":

    st.title("🤖 Iris Flower Prediction")
    st.info("""
    Typical Iris Measurements

    🌸 Setosa
    Petal Length < 2 cm

    🌿 Versicolor
    Petal Length ≈ 3–5 cm

    🌺 Virginica
    Petal Length > 5 cm
    """)

    st.markdown("""
    Enter the flower measurements below and click **Predict**
    to identify the Iris flower species.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        sepal_length = st.number_input(
            "Sepal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=5.1,
            step=0.1
        )

        sepal_width = st.number_input(
            "Sepal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=3.5,
            step=0.1
        )

    with col2:

        petal_length = st.number_input(
            "Petal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=1.4,
            step=0.1
        )

        petal_width = st.number_input(
            "Petal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=0.2,
            step=0.1
        )

    st.divider()

    if st.button("🌸 Predict Species", use_container_width=True):

        input_data = np.array([
            [
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            ]
        ])

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        st.success("Prediction Completed Successfully!")

        st.subheader("Predicted Species")

        if prediction == "Setosa":
            st.success("🌸 Setosa")

        elif prediction == "Versicolor":
            st.info("🌿 Versicolor")

        else:
            st.warning("🌺 Virginica")

        st.divider()

        st.subheader("Prediction Confidence")

        confidence = pd.DataFrame(
            {
                "Species": model.classes_,
                "Probability": probabilities
            }
        )

        confidence["Probability"] = (
            confidence["Probability"] * 100
        ).round(2)

        st.dataframe(
            confidence,
            use_container_width=True,
            hide_index=True
        )

        st.bar_chart(
            confidence.set_index("Species")
        )

    st.divider()

    st.subheader("Input Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Sepal Length",
            "Sepal Width",
            "Petal Length",
            "Petal Width"
        ],
        "Value": [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )




# ===================================================
# MODEL PERFORMANCE
# ===================================================

elif page == "Model Performance":

    st.title("📊 Model Performance")

    st.markdown("""
    This section evaluates the performance of the trained
    Decision Tree classifier on the testing dataset.
    """)

    st.divider()

    # ------------------------------------------------
    # Accuracy
    # ------------------------------------------------

    st.metric(
        label="Model Accuracy",
        value=f"{accuracy*100:.2f}%"
    )

    st.divider()

    # ------------------------------------------------
    # Classification Report
    # ------------------------------------------------

    st.subheader("Classification Report")

    report_df = pd.DataFrame(report).transpose()

    st.dataframe(
        report_df,
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------
    # Confusion Matrix
    # ------------------------------------------------

    st.subheader("Confusion Matrix")

    st.image(
        "images/confusion_matrix.png",
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------
    # Feature Importance
    # ------------------------------------------------

    st.subheader("Feature Importance")

    st.image(
        "images/feature_importance.png",
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------
    # Test Dataset Size
    # ------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Training Samples",
            len(X_train)
        )

    with col2:
        st.metric(
            "Testing Samples",
            len(X_test)
        )


# ===================================================
# ABOUT PAGE
# ===================================================

elif page == "About":

    st.title("ℹ About This Project")

    st.write("---")

    st.header("Project Overview")

    st.write("""
The Iris Flower Classification project is a beginner-friendly
Machine Learning project that predicts the species of an Iris flower
using four physical measurements.

The project demonstrates the complete Machine Learning workflow,
including data exploration, visualization, model training,
evaluation, prediction, and deployment using Streamlit.
""")

    st.write("---")

    st.header("Problem Statement")

    st.write("""
Predict the species of an Iris flower using:

• Sepal Length

• Sepal Width

• Petal Length

• Petal Width
""")

    st.write("---")

    st.header("Flower Species")

    st.write("""
🌸 Setosa

🌿 Versicolor

🌺 Virginica
""")

    st.write("---")

    st.header("Technologies Used")

    tech_df = pd.DataFrame({
        "Category":[
            "Programming Language",
            "Data Processing",
            "Visualization",
            "Machine Learning",
            "Deployment"
        ],
        "Technology":[
            "Python",
            "NumPy & Pandas",
            "Matplotlib & Seaborn",
            "Scikit-learn",
            "Streamlit"
        ]
    })

    st.dataframe(
        tech_df,
        hide_index=True,
        use_container_width=True
    )

    st.write("---")

    st.header("Machine Learning Workflow")

    st.markdown("""
1. Import Libraries

2. Load Dataset

3. Data Cleaning

4. Exploratory Data Analysis

5. Feature Selection

6. Train-Test Split

7. Train Decision Tree

8. Evaluate Model

9. Predict New Samples

10. Save Model

11. Deploy using Streamlit
""")

    st.write("---")

    st.header("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Samples", len(df))

        st.metric("Features", X.shape[1])

    with col2:
        st.metric("Classes", len(model.classes_))

        st.metric("Algorithm", "Decision Tree")

    st.write("---")

    st.header("Project Structure")

    st.code("""
iris-flower-classification/
│
├── app.py
├── iris_decision_tree.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── iris.csv
│
└── images/
    ├── countplot.png
    ├── histogram.png
    ├── heatmap.png
    ├── scatterplot.png
    ├── pairplot.png
    ├── boxplot.png
    ├── confusion_matrix.png
    └── feature_importance.png
""")

    st.write("---")

    st.header("Future Improvements")

    st.markdown("""
- Compare multiple Machine Learning models

- Hyperparameter tuning

- Cross Validation

- Model Deployment on Cloud

- Docker Containerization

- MLOps Pipeline

- REST API using Flask/FastAPI
""")

    st.write("---")

    st.header("Developer")

    st.info("""
Project developed as part of a Machine Learning learning journey.

Built using Python, Scikit-learn, and Streamlit.
""")

    st.write("---")

    st.success("🌸 Thank you for exploring the Iris Flower Classification project!")