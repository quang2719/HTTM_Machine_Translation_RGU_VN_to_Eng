# 🤖 HTTM_Machine_Translation_RGU_VN_to_Eng

A Vietnamese to English machine translation system using GRU (Gated Recurrent Unit) network, developed for the Smart System Development course.

## 📚 Project Introduction

This project aims to create an accurate Vietnamese-to-English translation system powered by GRU network architecture. The model processes Vietnamese input sequences and generates corresponding English translations.

### 🔗 Resources
**Wanna test your own sample? All you need here!** <br>
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/code/b21dccn632nvquang/tpu-machine-translation-using-gru) <br>
**Download dataset here!** <br>
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-FFD21E?style=for-the-badge)](https://huggingface.co/datasets/ncduy/mt-en-vi)

## 🗃️ Dataset

Our dataset comprises parallel Vietnamese-English sentence pairs from Hugging Face, containing [Number] samples for training and evaluation.

### 📝 Sample Data

![Sample Data 1][sample1-link]
![Sample Data 2][sample2-link]

## 📊 Exploratory Data Analysis (EDA)

### Data Analysis Focus
- Word frequency distribution
- Sentence length patterns
- Vietnamese-English structural comparison

### 📈 Visualizations

#### Vietnamese Vocabulary Distribution
![Vietnamese Vocabulary][viet-viz-link]

#### English Vocabulary Distribution
![English Vocabulary][eng-viz-link]

## 🏋️ Training Process

### Configuration
- **Epochs**: 50
- **Time per Epoch**: 20-30 minutes
- **Objective**: Minimize translation error

### 📉 Training Metrics

#### Loss Curve
![Loss Curve][loss-curve-link]

#### Performance Metrics
![Training Metrics][metrics-link]

## 🧪 Evaluation

### BLEU Score Analysis
- **Score**: [INSERT_SCORE]
- **Method**: Comparison with human translations

## 💬 Demo Examples

### Translation Sample 1
```plaintext
🇻🇳 Vietnamese: [Input sentence 1]
🇬🇧 English: [Output sentence 1]
