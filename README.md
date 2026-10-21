 📱 Social Media Addiction & Brainrot Detection System

A Machine Learning-based web application that predicts social media addiction levels and estimates brainrot score using user behavior data.

Built using Python, Scikit-learn, and Streamlit, this project demonstrates a complete ML pipeline from data preprocessing to deployment.

🚀 Features
🔍 Predicts Addiction Score (Classification)
🧠 Estimates Brainrot Score (Regression)
📊 Real-time predictions via Streamlit UI
⚙️ End-to-end ML pipeline (preprocessing → training → deployment)
📁 Handles categorical data using One-Hot Encoding
📈 Scaled features using StandardScaler
📂 Dataset Information

## Dataset
Kaggle "Students Social Media Addiction" dataset (705 rows, 13 columns).
Brainrot_Score is a derived target 
Brainrot_Score = (
    (Avg_Daily_Usage_Hours) * 2 +
    (Conflicts_Over_Social_Media) * 1.5 -
    (Sleep_Hours_Per_Night) * 1.2 -
    (Mental_Health_Score) * 0.8
).

The dataset contains behavioral and demographic features:

Age
Gender
Academic Level
Country
Avg Daily Usage Hours
Most Used Platform
Affects Academic Performance
Sleep Hours Per Night
Mental Health Score
Relationship Status
Conflicts Over Social Media
Addicted Score (Target - Classification)
Brainrot Score (Target - Regression)

🧠 Machine Learning Models
Task	Model Used
Addiction Prediction	Random Forest Classifier
Brainrot Prediction	Linear Regression

⚙️ Project Workflow
Data Cleaning & Preprocessing
Encoding (One-Hot Encoding using pd.get_dummies)
Feature Scaling (StandardScaler)
Train-Test Split
Model Training
Model Evaluation
Model Saving (pickle)
Deployment using Streamlit

📊 Model Performance
Training Accuracy: ~97%
Testing Accuracy: ~96%
Cross Validation Score: ~87%

🖥️ Streamlit App
The app allows users to:

Input personal and behavioral data
Get instant addiction prediction
View brainrot score and level

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/social-media-addiction-detection.git
cd social-media-addiction-detection
2. Install dependencies
pip install -r requirements.txt
3. Run the Streamlit app
streamlit run app.py

📦 Project Structure

├── app.py
├──  social media addiction and brainrot detection.ipynb
├── addiction_model.pkl
├── brainrot_model.pkl
├── scaler.pkl
├── columns.pkl
├── Students Social Media Addiction.csv
└── README.md

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle

🎯 Key Learnings
Importance of consistent preprocessing between training and inference
Handling categorical variables in ML pipelines
Avoiding data leakage (removing target from features)
Model deployment using Streamlit

🚀 Future Improvements
Add visualization dashboard 📊
Use advanced models (XGBoost, Neural Networks)
Deploy on cloud (Streamlit Cloud / AWS / Render)
Add user authentication system

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License

This project is open-source and available under the MIT License.
