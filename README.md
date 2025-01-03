# CrimeAgainstWomenClassifier
This repository is a focused analysis project aimed at understanding and evaluating crime data related to women's safety across different states and districts in India. The project emphasizes three main areas: data preprocessing, exploratory data analysis (EDA), and model evaluation for safety classification. 

Project Highlights:

Data Preprocessing: The raw dataset includes various crime types (e.g., rape, kidnapping, assault, domestic violence) and spans multiple years. To ensure effective model performance and accurate analysis, the project involves substantial preprocessing steps, such as handling missing values, removing duplicates, and generating derived features like "Total Crimes" and a safety label. We also apply one-hot encoding to categorical variables, particularly for state and district columns, to prepare the data for machine learning algorithms.

Exploratory Data Analysis (EDA): EDA is performed to identify trends, patterns, and anomalies in the dataset. Visualizations include bar charts and pie charts, helping to uncover relationships between crime rates and regions, as well as changes over time. EDA provides a deeper understanding of which areas report higher instances of specific crimes, assisting in categorizing states and districts based on safety metrics.

Model Evaluation: The project explores and evaluates several machine learning models to classify regions as "Safe" or "Unsafe" based on crime data. Classification models tested include K-Nearest Neighbors (KNN), SVC, Decision Tree, Random Forest, Naive Bayes, and Logistic Regression. Model evaluation is focused on accuracy metrics, revealing that KNN, Decision Tree, and Random Forest models achieve high accuracy, suggesting their effectiveness in this context. In contrast, Naive Bayes shows relatively lower performance, indicating it may be less suited to this particular dataset.
