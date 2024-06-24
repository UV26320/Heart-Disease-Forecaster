# Heart Disease Predictors

This project aims to predict the presence of heart disease in patients using machine learning models. The models are trained on a dataset containing various health metrics and then deployed using a Flask web application for real-time predictions.


## Introduction

Heart disease is one of the leading causes of death globally. Early prediction and diagnosis can significantly improve the chances of treatment and survival. This project uses machine learning techniques to predict heart disease based on various health parameters.

## Dataset

The dataset used in this project is the "Heart.csv" file. It contains the following features:

- `age`: Age of the patient
- `sex`: Gender of the patient
- `cp`: Chest pain type
- `trestbps`: Resting blood pressure
- `chol`: Serum cholesterol
- `fbs`: Fasting blood sugar
- `restecg`: Resting electrocardiographic results
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise-induced angina
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: The slope of the peak exercise ST segment
- `ca`: Number of major vessels (0-3) colored by fluoroscopy
- `thal`: Thalassemia
- `target`: Target variable (1 indicates the presence of heart disease, 0 indicates absence)

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed to understand the distribution of the data and the relationships between features. Key steps include:

- Plotting the distribution of each feature
- Calculating the correlation matrix
- Normalizing features with high variance

## Models Used

The following machine learning models were used in this project:

1. **Logistic Regression**
2. **Gradient Boosting**
3. **Random Forest**
4. **XGBoost**

Each model's performance is evaluated using accuracy scores on both training and testing datasets.

## Usage

### Predictive System

A predictive system is built to allow users to input patient data and receive predictions on the likelihood of heart disease. The system is implemented using Flask and can be accessed via a web interface.

### Flask Application

The Flask application (`app.py`) serves as the front-end for the predictive system. Users can input their data through an HTML form, and the model predicts the presence of heart disease.

## Installation

### Requirements

- Python 3.7.9
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/heart-disease-predictors.git
   ```
2. Navigate to the project directory:
   ```sh
   cd heart-disease-predictors
   ```
3. Create a virtual environment:
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```
4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```sh
   python app.py
   ```

