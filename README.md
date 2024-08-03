# Predicting Remaining Useful Life (RUL) of Lithium-Ion Batteries
This repository contains the implementation of a project aimed at predicting the remaining useful life (RUL) of lithium-ion batteries using various machine learning algorithms and a web interface built with Flask.

# Table of Contents
Project Overview
Dataset
Features
Machine Learning Models
Project Structure
Installation
Usage
Web Interface
Results

# Project Overview
The goal of this project is to predict the remaining useful life (RUL) of lithium-ion batteries using data from the Hawaii Natural Energy Institute. The dataset contains information on 14 NMC-LCO 18650 batteries with a nominal capacity of 2.8 Ah, cycled over 1000 times at 25°C.

# Dataset
The dataset contains 10,000 data points and includes the following features:

Cycle_Index
Discharge Time (s)
Decrement 3.6-3.4V (s)
Max. Voltage Dischar. (V)
Min. Voltage Charg. (V)
Time at 4.15V (s)
Time constant current (s)
Charging time (s)
RUL (Remaining Useful Life)

# Features
Based on feature engineering and selection, the following three features were chosen as the most important for predicting RUL:

Cycle_Index
Max. Voltage Dischar. (V)
Time at 4.15V (s)

# Machine Learning Models
The following machine learning algorithms were evaluated in this project:

Linear Regression
Ridge Regression
Lasso Regression
ElasticNet Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor
XGBoost Regressor
LightGBM Regressor
CatBoost Regressor

RUL_Project_
│   README.md
│   
│   RUL2.ipynb
│
└───data
│   │   your_dataset.csv
│
└───results
│   │   model_performance.png
│
└───webapp
    │   app.py
    │   templates/
    │   static/
