# Predictive Maintenance for Milling Machines

## Project Description
This project focuses on predicting the need for maintenance in milling machines to minimize downtime and optimize operations. By analyzing the "AI4I 2020 Predictive Maintenance Dataset" from the UCI Machine Learning Repository, we build machine learning models that can predict potential machine failures, identify critical factors influencing maintenance needs, and recommend actions to prevent unexpected breakdowns.

---

## Problem Statement
Milling machines are essential in many industries, but unexpected failures can lead to costly delays and operational inefficiencies. Predictive maintenance offers a proactive approach by forecasting failures before they occur, enabling timely interventions and reducing downtime. The goal is to develop a predictive model to classify and predict potential failures (e.g., tool wear, overstrain, heat dissipation issues) in milling machines based on real-world sensor data.

---

## Dataset
The dataset used is the **AI4I 2020 Predictive Maintenance Dataset**, available on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset).

**Dataset Features**:
- **UDI**: Unique identifier for each record.
- **Product ID**: Identifier of the product being processed.
- **Type**: Machine type (High, Medium, Low).
- **Air temperature [°C]**: Environmental condition.
- **Process temperature [°C]**: Temperature during machining.
- **Rotational speed [rpm]**: Spindle speed.
- **Torque [Nm]**: Torque applied during machining.
- **Tool wear [min]**: Cumulative tool usage.
- **Target Variables**:
  - **Failure Type** (No Failure, Heat Dissipation, Power Failure, Overstrain, Tool Wear, Random Failures).
  - **Machine Failure** (binary classification).

**Dataset Size**: 10,000 samples, 8 features, and 6 labels.

---

## Key Deliverables
1. **Exploratory Data Analysis (EDA)**
   - Distribution of features and their correlation with failures.
   - Visualization of machine types and their failure trends.

2. **Data Preprocessing**
   - Handling missing values and outliers.
   - Feature scaling and encoding categorical variables.

3. **Modeling**
   - Develop predictive models using:
     - Logistic Regression.
     - Random Forest.
     - Gradient Boosting (e.g., XGBoost, LightGBM).
     - Deep Learning (if applicable).
   - Evaluate models using metrics like F1-Score, Precision, Recall, and ROC-AUC.

4. **Insights and Recommendations**
   - Identify the most critical factors affecting failures.
   - Provide actionable insights for maintenance schedules.

5. **Deployment** (Stretch Goal)
   - Build a simple web app using Streamlit or Flask to predict failures based on user inputs.

---

## Tools and Technologies
- **Programming Language**: Python.
- **Libraries**:
  - Data Analysis: Pandas, NumPy.
  - Visualization: Matplotlib, Seaborn.
  - Machine Learning: Scikit-learn, XGBoost, LightGBM.
  - Deployment: Streamlit, Flask (optional).
- **Version Control**: Git, GitHub.
- **Environment**: Jupyter Notebook, VSCode.

---

## Project Workflow
1. **Problem Understanding**: Define objectives and scope.
2. **Data Understanding**: Explore and preprocess the dataset.
3. **Feature Engineering**: Extract meaningful features and handle data imbalances.
4. **Model Training**: Train multiple models and tune hyperparameters.
5. **Evaluation**: Compare models based on defined metrics.
6. **Documentation**: Write clear code, create visuals, and explain findings.
7. **Presentation**: Deliver insights and recommendations effectively.
8. **Deployment** (if applicable): Create a user-friendly interface.

---

## Results
- Best model achieved an **accuracy of XX%** and an **F1-Score of YY** in predicting machine failures.
- Identified key features influencing failure likelihood:
  - Tool wear time.
  - Process temperature.
  - Rotational speed.
- Proposed an optimized maintenance schedule based on predictive insights.

---

## Challenges
- Dealing with class imbalance in failure types.
- Ensuring model generalization to unseen data.
- Balancing interpretability and predictive power.

---

## Future Work
- Extend analysis to real-time data streams.
- Implement deep learning models for enhanced accuracy.
- Integrate predictions into a manufacturing dashboard.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/predictive-maintenance-milling.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook for EDA and modeling:
   ```bash
   jupyter notebook
   ```

4. (Optional) Launch the web app:
   ```bash
   streamlit run app.py
   ```

---

## References
- Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)
- Machine Learning Zoomcamp: [DataTalksClub](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- Documentation Guidelines: [GitHub Docs](https://docs.github.com/)

---

## Acknowledgments
Special thanks to the UCI Machine Learning Repository for providing the dataset and DataTalksClub for their guidance on machine learning projects.


