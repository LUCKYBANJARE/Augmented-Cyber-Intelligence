# Augmented Cyber Intelligence (ACI)

## Overview

Augmented Cyber Intelligence (ACI) is an advanced cybersecurity framework designed for **real-time intrusion detection, attack investigation, and immersive cyber situational awareness**.

The project combines machine learning, deep learning, explainable AI, and visualization techniques to detect, analyze, and reconstruct cyber attacks.

The system introduces a novel **Hybrid FRF-LSTM (Fast Random Forest + Long Short-Term Memory)** model for high-accuracy intrusion detection and integrates **Particle Swarm Optimization (PSO)** for hyperparameter tuning.

---

## Research Motivation

Traditional intrusion detection systems often focus only on classification accuracy and fail to support:

* Attack investigation
* Event correlation
* Timeline reconstruction
* Interactive analyst collaboration
* Visual situational awareness

ACI solves this by building a unified intelligent cyber defense platform.

---

## Key Features

### Hybrid Intrusion Detection

* Fast Random Forest (FRF)
* LSTM-based temporal analysis
* Weighted hybrid fusion model

### Optimization Engine

* Particle Swarm Optimization (PSO)
* Automatic hyperparameter tuning

### Explainable AI

* SHAP-based feature contribution analysis
* Improved trust and transparency

### Attack Correlation

* Event linking
* Timeline reconstruction
* Multi-stage attack analysis

### Human-in-the-Loop

* Analyst validation
* Feedback-driven model improvement

### Cyber Visualization

* Interactive attack graphs
* Attack propagation analysis
* Immersive situational awareness

---

## System Architecture

Data Acquisition → Preprocessing → Hybrid Detection → Optimization → Attack Correlation → Visualization → Analyst Feedback

---

## Dataset Used

### UNSW-NB15 Dataset

Primary dataset used for training and evaluation.

Contains:

* ~2.5 Million records
* 49 network features
* 9 attack categories

Attack categories:

* Fuzzers
* Analysis
* Backdoors
* DoS
* Exploits
* Generic
* Reconnaissance
* Shellcode
* Worms

Dataset link:
https://research.unsw.edu.au/projects/unsw-nb15-dataset

Kaggle mirror:
https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15

---

## Model Performance

### Binary Classification

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | 85.77%     |
| Decision Tree       | 87.10%     |
| Random Forest       | 89.95%     |
| CNN                 | 90.05%     |
| Proposed FRF-LSTM   | **97.03%** |

---

### Multiclass Classification

| Model             | Accuracy   |
| ----------------- | ---------- |
| Random Forest     | 78.02%     |
| Decision Tree     | 79.66%     |
| Gradient Boosting | 85.16%     |
| Proposed FRF-LSTM | **87.95%** |

---

### PSO Optimized Hybrid Model

| Metric    | Value      |
| --------- | ---------- |
| Accuracy  | **92.04%** |
| Precision | 0.66       |
| Recall    | 0.68       |
| F1 Score  | 0.67       |

---

## Technologies Used

* Python
* Scikit-learn
* TensorFlow / Keras
* LightGBM
* XGBoost
* SHAP
* Pandas
* NumPy
* Matplotlib
* Plotly
* Flask
* React (planned)
* Globe.gl (planned)

---

## Project Structure

```bash
Augmented-Cyber-Intelligence/
│── src/
│── models/
│── notebooks/
│── dataset/        # ignored
│── results/
│── visualizations/
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Installation

```bash
git clone https://github.com/LUCKYBANJARE/Augmented-Cyber-Intelligence.git
cd Augmented-Cyber-Intelligence
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Future Scope

* Real-time SOC deployment
* Zero-day attack detection
* Edge AI deployment
* IoT security integration
* AR-based collaborative cyber defense
* Threat intelligence API integration

---


## Author

**Lucky Banjare**
Cybersecurity Researcher | AI-ML Engineering Undergraduate(CSE) | Security Visualization Enthusiast

GitHub:
https://github.com/LUCKYBANJARE
