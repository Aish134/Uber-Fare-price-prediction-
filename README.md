# Uber Fare Prediction using Machine Learning
# LIVE PROJECT DEMO
https://hqbht8umyvdsw5xklefmwt.streamlit.app/

##  Project Overview

This project predicts the **fare amount of an Uber ride** based on pickup and drop-off details using Machine Learning models.
The system uses:

* Data preprocessing & cleaning
* Feature engineering (including distance calculation)
* Outlier detection
* Correlation analysis
* Regression models (Linear Regression & Random Forest)

A **Streamlit web application** is also built to allow users to input trip details and get real-time fare predictions.

---

## Objectives

* Predict Uber ride fare accurately
* Handle real-world noisy data
* Compare different regression models
* Deploy model using Streamlit

---

## Project Structure

```
uber-price-prediction/
│
├── data.csv              # Dataset
├── model.py              # Model training script
├── model.pkl             # Trained model (optional)
├── app.py                # Streamlit web app
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Technologies Used
* Python 
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## Dataset Description
The dataset contains Uber ride details such as:

* `pickup_datetime` → Date & time of ride
* `pickup_longitude`, `pickup_latitude`
* `dropoff_longitude`, `dropoff_latitude`
* `passenger_count`
* `fare_amount` (target variable)

---

##  Data Preprocessing Steps

1. **Handling Missing & Invalid Values**

   * Removed NaN values
   * Replaced infinite values (`inf`, `-inf`)
   * Filtered invalid latitude/longitude values

2. **Feature Engineering**

   * Extracted:

     * Hour
     * Day
     * Month
   * Created **distance feature** (important for fare prediction)

3. **Outlier Removal**

   * Removed unrealistic fares:

     * fare < 0
     * fare > 100

---

## Correlation Analysis

Correlation matrix is used to understand relationships between features and fare amount.

---

##  Models Used

### 1. Linear Regression

* Simple baseline model
* Fast but less accurate

### 2. Random Forest Regressor

* Ensemble model
* Higher accuracy
* Handles non-linearity better

---

##  Evaluation Metrics

* **RMSE (Root Mean Squared Error)**
  Measures prediction error magnitude

* **R² Score (Coefficient of Determination)**
  Measures how well the model explains variance

---

##  How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/uber-price-prediction.git
cd uber-price-prediction
```

---

### 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 3: Train Model

```bash
python model.py
```

👉 This will generate:

```
model.pkl
```

---

### 🔹 Step 4: Run Streamlit App

```bash
streamlit run app.py
```

---

## 🌐 Streamlit App Features

* User-friendly interface
* Input ride details
* Predict fare instantly
* Displays estimated fare in ₹

---

## 🚀 Deployment on Streamlit Cloud

1. Push project to GitHub
2. Go to: https://streamlit.io/cloud
3. Click **New App**
4. Select your repository
5. Choose `app.py`
6. Click **Deploy**

---

## ⚠️ Important Notes

* If `model.pkl` is too large (>25MB):

  * Use compression (`joblib`)
  * Or retrain model with fewer trees
  * Or exclude using `.gitignore`

---

## 📌 Future Improvements

* Add map integration (Google Maps API)
* Use advanced models (XGBoost, LightGBM)
* Hyperparameter tuning
* Better distance calculation (Haversine formula)
* Real-time API integration

---

## 📷 Sample Output

```
Estimated Fare: ₹ 245.67
```

---

## 👨‍💻 Author

* Aishwarya Bedge

---

## 📄 License

This project is for educational purposes only.
