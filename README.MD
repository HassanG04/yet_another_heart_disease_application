# 🫀 Heart Disease Prediction: AI Performance Analysis

## Overview
This project is a reimplementation of the research paper *"Heart disease prediction using distinct artificial intelligence techniques: performance analysis and comparison"* (Hossain et al., 2023). Following the CRISP-DM framework, this notebook evaluates and compares seven different machine learning algorithms for the classification of heart disease. 

The methodology leverages **Correlation-Based Feature Selection (CFS)** to eliminate noisy clinical features from the **UCI Cleveland Heart Disease dataset**, ultimately optimizing the predictive accuracy of the models.

### Models Evaluated
1. Logistic Regression
2. Gaussian Naive Bayes
3. K-Nearest Neighbors (KNN)
4. Support Vector Machine (SVM)
5. Decision Tree
6. Random Forest
7. Multi-Layer Perceptron (MLP) Neural Network

---

## ⚙️ Prerequisites & Dependencies

To run this project, you need **Python 3.x** installed along with the following libraries:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `scikit-learn`
* `jupyter`

You can install all required dependencies by running the following command in your terminal:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```
## How to Run the Project
1. Clone or Download the project files to your local machine.

2. Ensure the Dataset is present: Make sure the UCI Cleveland dataset (heart.csv or similar) is located in the same directory as the notebook (or adjust the file path in the data loading cell).

3. Launch Jupyter Notebook: Open your terminal or command prompt, navigate to the project folder, and run:
```bash
jupyter notebook
```
4. Open the Notebook: Click on Final_project.ipynb in the Jupyter interface.

5. Run the Code: Execute the cells sequentially by clicking Run or pressing Shift + Enter.
## References
- Original Research Paper: Hossain, et al. (2023). "Heart disease prediction using distinct artificial intelligence techniques: performance analysis and comparison."

- Dataset: UCI Machine Learning Repository - Cleveland Heart Disease Dataset