# 🏏 IPL Match Winner Prediction System

An end-to-end **Machine Learning + Data Engineering + Deployment** project that predicts the **winner of an IPL match** using historical data and deploys the model as an interactive **Streamlit web application**.

---

## 🚀 Live Features
- 🔮 Predict IPL match winner

- 📈 Winning probability with confidence bar
- 🌗 Dark mode toggle
- ✅ Input validation (realistic match constraints)
- 🧠 Categorical ML using CatBoost
- 🌐 Web deployment using Streamlit

---

## 🚀 Demo 
https://ishivanshh-mlmodel-matchwinner-app-tlzcyt.streamlit.app/


## Github Repo link 
https://github.com/ishivanshh/MLmodel_matchwinner

___

## 🧩 Problem Statement
Cricket match outcomes are influenced by multiple categorical factors such as:
- Teams playing
- Venue
- Toss winner  

The goal is to **predict the winning team before the match starts** using only pre-match information.

---

## 🗂️ Dataset
- Source: kaggle dataset 2008-2025
- Granularity: **Match-level**
- Key columns:
  - `batting_team`
  - `bowling_team`
  - `venue`
  - `toss_winner`
  - `match_won_by`

⚠️ Matches with *no result / abandoned* outcomes are excluded.

---

## 🛠️ ETL Pipeline (Project-Scale)

### **Extract**
- Loaded IPL data from CSV files using Pandas.

### **Transform**
- Removed invalid matches (no result)
- Selected relevant categorical features
- Ensured match-level granularity
- Prepared clean inputs for ML and analytics

### **Load**
- Loaded transformed data into:
  - CatBoost ML model (training)
  - Streamlit app 

---

## 🤖 Machine Learning Model

### Model Used
**CatBoostClassifier**

### Why CatBoost?
- Accuracy: 0.8558257400118617
- Native handling of categorical features
- No need for label encoding
- Reduces overfitting on small datasets
- Ideal for structured sports data


### Features (X)
- Batting team
- Bowling team
- Venue
- Toss winner

### Target (y)
- Match winner (team name)

### Evaluation
- Multi-class classification
- Realistic accuracy range: **80% +**
- Accuracy is intentionally capped due to inherent randomness in cricket

---

## 🎨 Streamlit Application

### User Inputs
- Batting Team
- Bowling Team
- Venue
- Toss Winner *(restricted to selected teams)*

### Validations
- ❌ Same team cannot play against itself
- ❌ Toss winner must be one of the playing teams

### Outputs
- 🏆 Predicted Winner
- 📊 Winning Probability
- 📈 Confidence Progress Bar


### To run streamlit app 
- python3 -m streamlit run app.py





