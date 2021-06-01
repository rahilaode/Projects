# Bangkit Final Project - Export Commodity Demands Prediction

1. Download the dataset ( https://www.kaggle.com/unitednations/global-commodity-trade-statistics ), 
2. Import dependencies library (tensorflow, keras, scikit-learn, numpy, pandas, flask, and os)
3. Data Preprocessing
4. Create model using LSTM
5. Training and validating model
6. Save the model to h5 format
7. Pick the last three years as input for the model to predict the next three years
8. Deploying on google cloud

# Installation 
Use pip to install prerequisites on requirements.txt, if you on google colab you can skip the process.

# Datasets 
Global Commodity Trade Statistics in three decades of global trade flows https://www.kaggle.com/unitednations/global-commodity-trade-statistics
Size archive : 120.26 MB, Size csv in archive : 1.14 GB

# Result 
## Baseline Model ( Example : Model for Potatoes, fresh or chilled except seed import demands in Denmark )

### Dataset before transform in range 0 - 1 look like
![image](https://user-images.githubusercontent.com/80165152/120360690-9aa62a80-c33b-11eb-9154-545197c027f0.png)

### Data after transform in range 0 - 1 look like
![image](https://user-images.githubusercontent.com/80165152/120359541-5c5c3b80-c33a-11eb-9c39-75365e29a4ed.png)

### Loss training
![image](https://user-images.githubusercontent.com/80165152/120360828-c75a4200-c33b-11eb-93d3-d87f5597f362.png)

### Val training
![image](https://user-images.githubusercontent.com/80165152/120360879-d2ad6d80-c33b-11eb-8b4d-4b3a648176eb.png)

### Model Summary
![image](https://user-images.githubusercontent.com/80165152/120361279-3f286c80-c33c-11eb-9cf6-5eb567e1a921.png)

### RMSE
![image](https://user-images.githubusercontent.com/80165152/120361000-f07ad280-c33b-11eb-9d19-7059aaf4187c.png)


