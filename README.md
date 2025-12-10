# 🛡️ Credit Card Fraud Detection — Machine Learning Project

## ⭐ Overview
This repository contains an end-to-end Machine Learning project for **credit card fraud detection**, built using the popular Kaggle dataset. The problem is challenging due to **extreme class imbalance** (~0.17% fraud cases).  
This project demonstrates techniques for handling imbalanced data, training multiple models, optimizing thresholds, and evaluating the system for real-world deployment.

---

## 📂 Project Structure
```
credit-card-fraud-detection/
├── credit_card_fraud_detection.ipynb
├── README.md
├── requirements.txt
├── LICENSE
```
## 🛠️ How to run
1. Clone the repository:
```bash
git clone https://github.com/<Amit-712>/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Launch Jupyter Notebook / Colab:
```bash
jupyter notebook
# or upload the notebook to Google Colab
```

## 📊 Dataset (details)

**Dataset used:** *Kaggle — Credit Card Fraud Detection* (`creditcard.csv`)

**Overview**
- The dataset contains anonymized real-world credit card transactions collected over two days.
- Features `V1` — `V28` are the result of a PCA transformation applied by the dataset provider (to protect confidentiality).
- `Time` — seconds elapsed between this transaction and the first transaction in the dataset.
- `Amount` — transaction amount.
- `Class` — target variable (0: non-fraud, 1: fraud).

**Key facts**
- Number of rows: ~284,807 (typical Kaggle version)
- Number of features: 30 (`Time`, `Amount`, `V1`...`V28`) + `Class`
- Class imbalance: fraud cases are extremely rare (~0.17% of all transactions)
- Because of the imbalance, accuracy is not a meaningful metric — we focus on **recall, precision, F1**, and **PR-AUC**.


## 🧾 License
This project is licensed under the MIT License - see the `LICENSE` file for details.


### 🏁 Conclusion and Result

This project shows how to design, build, and optimize a fraud detection system appropriate for real-world use. Through oversampling and threshold tuning, the final model achieves a strong balance between detecting fraud and minimizing customer inconvenience.

| Model                                | Precision | Recall   | F1-score   | ROC-AUC |
| ------------------------------------ | --------- | -------- | ---------- | ------- |
| Logistic Regression                  | 0.06      | **0.92** | 0.11       | 0.9721  |
| Random Forest                        | **0.96**  | 0.75     | 0.8457     | 0.9572  |
| RF + Oversampling                    | 0.95      | 0.78     | 0.8539     | 0.9667  |
| RF + Oversampling + Threshold (0.40) | 0.93      | 0.82     | **0.8696** | 0.9667  |


## ✉️ Contact
Feel free to connect if you have questions or want help understanding any part of the project:  
- 👤 Name: Amit Singh  
- 📧 Email: amit39836@gmail.com  
- 🔗 LinkedIn: https://www.linkedin.com/in/amit712   
- 💻 GitHub: github.com/Amit-712



