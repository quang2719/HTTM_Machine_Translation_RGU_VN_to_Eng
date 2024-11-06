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
[![Dataset](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/train-test-size.png?raw=true)](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/train-test-size.png?raw=true)

* Our dataset comprises parallel Vietnamese-English sentence pairs from Hugging Face, containing samples for training and evaluation.



### 📝 Sample Data

* Training sample:<br> [![image](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/training_set.png?raw=true)](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/training_set.png?raw=true)
* Test sample:<br> [![image](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/test_set.png?raw=true)](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/test_set.png?raw=true)

## 📊 Exploratory Data Analysis (EDA)

### Data Analysis Focus
- Word frequency distribution
<br> ![anh](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/eng-frequence-bar-chart.png?raw=true)
<br> ![anh](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/nv-frequence-bar-chart.png?raw=true)

### 📈 Visualizations

#### Vietnamese Vocabulary Distribution
![Vietnamese Vocabulary][viet-viz-link]
<br> ![anh](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/vn-wordcloud-visual.png?raw=true)
#### English Vocabulary Distribution
<br> ![anh](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/english-wordcloud-visual.png?raw=true)

## 🏋️ Training Process

### Configuration
- **Epochs**: 50
- **Time per Epoch**: 20-30 minutes
- **Objective**: Minimize translation error

## 🧪 Evaluation

### BLEU Score Analysis
![bleu](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/bleu-score.png)

## 💬 Demo Examples

### Translation Sample
![demo](https://github.com/quang2719/Project---Machine_Translation_RGU_VN_to_Eng-PTHTTM/blob/main/demo%20image/demo.png)
