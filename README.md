# 🍦 Ice Cream Sales Prediction with Machine Learning

## Overview

This project demonstrates how Machine Learning can be used to predict ice cream sales based on daily temperature. The goal is to help businesses anticipate customer demand and make better production decisions.

The scenario is inspired by a fictional ice cream shop called **Gelato Mágico**, located in a coastal city where sales vary significantly depending on the weather. By analyzing historical temperature data and sales patterns, we can train a predictive model capable of estimating how many ice creams will be sold on a given day.

Using data-driven predictions, businesses can reduce waste, optimize production, and improve profitability.

---

## Business Problem

Ice cream sales are strongly influenced by temperature. Without accurate forecasting, a business may:

- Produce **too much**, resulting in waste and financial losses
- Produce **too little**, missing potential sales opportunities

To address this problem, this project applies **Machine Learning regression techniques** to estimate daily ice cream sales based on temperature.

---

## Project Objectives

The main goals of this project are:

- Train a **Machine Learning regression model** to predict ice cream sales
- Track experiments and models using **MLflow**
- Structure the project in a reproducible workflow
- Demonstrate how predictive analytics can support business decision-making

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- MLflow
- Machine Learning Regression
- Git & GitHub

---

## Dataset Example

| Temperature (°C) | Ice Cream Sales |
|------------------|----------------|
| 20 | 100 |
| 22 | 120 |
| 25 | 150 |
| 28 | 180 |
| 30 | 200 |
| 32 | 220 |
| 35 | 250 |

The dataset shows the relationship between **temperature and ice cream sales**, allowing the model to learn patterns and generate predictions.

---

## Machine Learning Model

A **Linear Regression model** was used to capture the relationship between temperature and sales.

The model learns the correlation between these variables and generates predictions for future temperatures.

Example:

Temperature: **29°C**  
Predicted Sales: **~190 ice creams**

---

## Project Structure

```
ice-cream-sales-prediction-ml
|
|-- inputs
| |-- data.txt
|
|-- model
| |-- train_model.py
|
|-- notebook
| |-- icecream_prediction.ipynb
|
|-- README.md
|
|-- requirements.txt

```
## Experiment Tracking with MLflow

MLflow is used to:

- Track model parameters
- Log metrics and predictions
- Store trained models
- Ensure reproducibility of experiments

This allows developers and data scientists to monitor experiments and compare model performance efficiently.

---

## Results

The model successfully captures the positive correlation between temperature and ice cream sales.

As temperature increases, predicted sales also increase, which aligns with real-world consumer behavior.

---

## Business Impact

Using this predictive model, an ice cream shop could:

- Forecast daily demand
- Optimize production levels
- Reduce waste
- Increase profitability
- Improve operational planning

---

## Future Improvements

Possible enhancements for this project include:

- Using larger and more realistic datasets
- Adding additional variables such as humidity, day of the week, or holidays
- Deploying the model in a cloud environment
- Building an API for real-time predictions
- Creating dashboards for business analytics

---

## Author

**Cláudio Menezes de Oliveira Santos**

Junior IT Support Analyst transitioning into **Cloud, AI, and Machine Learning**.

GitHub:  
https://github.com/cmosantos

LinkedIn:  
https://www.linkedin.com/in/claudiomenesesantos

---

## Final Thoughts

This project highlights how even simple Machine Learning models can provide valuable insights for real-world business problems. Predictive analytics can help companies make smarter decisions and operate more efficiently.

Machine Learning is not only about algorithms — it is about solving problems and creating impact.
