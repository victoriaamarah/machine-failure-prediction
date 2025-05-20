# Predictive Maintenance for Milling Machines

## Project Background

Predictive maintenance has become a critical tool for avoiding unexpected machine failures and improving operational reliability. In this project, we apply machine learning techniques to assess the health of milling machines and predict potential failures before they happen.

This project uses the **AI4I 2020 Predictive Maintenance Dataset**, a synthetic dataset designed to mirror real-world industrial machine behavior. It includes sensor readings and operational settings from milling machines under varied conditions. By training machine learning models on this dataset, the project aims to classify failure types (e.g., **tool wear**, **overstrain**, **heat dissipation issues**) and forecast potential malfunctions

**Key Analysis Areas:**

- **Failure Type Classification:** Predict whether an equipment failure will occur and identify which type (e.g., heat-related, mechanical stress).
    
- **Sensor Pattern Analysis:** Understand which machine sensors (torque, tool wear, rotational speed) contribute most to failure predictions.
    
- **Operational Risk Profiling:** Analyze how operating conditions (load, power, usage hours) correlate with failure likelihood.

## Data Structure
The dataset used is the **AI4I 2020 Predictive Maintenance Dataset**, available on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset). **Dataset Size:** 10,000 records · 8 input features · 6 categorical failure labels

#### Data Dictionary

|Column Name|Type|Description|
|---|---|---|
|`UDI`|Integer|Unique identifier for each data record|
|`Product ID`|String|Identifier for the specific product being processed|
|`Type`|Category|Type of machine (`Low`, `Medium`, `High`)|
|`Air temperature [°C]`|Float|Ambient air temperature in degrees Celsius|
|`Process temperature [°C]`|Float|Internal temperature during machining|
|`Rotational speed [rpm]`|Integer|Spindle rotation speed in revolutions per minute|
|`Torque [Nm]`|Float|Torque applied to the spindle, measured in Newton-meters|
|`Tool wear [min]`|Integer|Total duration the tool has been used, measured in minutes|

##### Target Variables

|Column Name|Type|Description|
|---|---|---|
|`Failure Type`|Category|Type of failure event (`No Failure`, `Heat Dissipation`, `Power Failure`, `Overstrain`, `Tool Wear`, `Random Failures`)|
|`Machine Failure`|Boolean|Indicates whether a machine failure occurred (`1` = Failure, `0` = No Failure)|

---

## EDA

<img src="_EDA/histogram.png" width="400"> <img src="_EDA/failure_types.png" width="400"> <img src="_EDA/Correlation_Heatmap.png" width="400"> <img src="_EDA/Quality_Types.png" width="400">

---

## Results
The Decision Tree model used achieved an accuracy of 89% and an F1-Score of 0.85 in predicting machine failures.

**The Key features influencing failures include**:
- **Tool wear time:** had the highest correlation with failure events.
- **Process temperature:** and rotational speed significantly impacted failure likelihood.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/machine-failure-prediction.git
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
