# 🦸 Marvel Character Classification using Computer Vision

An end-to-end Computer Vision project that builds a custom Marvel Cinematic Universe (MCU) image dataset from scratch and trains a Convolutional Neural Network (CNN) to classify Marvel characters.

The project covers the complete machine learning workflow, including data collection, exploratory data analysis, dataset cleaning, model training, evaluation, and prediction on unseen images.

---

## 📌 Project Overview

Public datasets containing high-quality images of specific MCU characters are limited or unavailable. To address this problem, a custom dataset was created by automatically collecting images from Google Images using Selenium.

The collected images were manually reviewed and cleaned before training a baseline CNN for multi-class image classification.

This project demonstrates not only model development but also the complete data engineering process required for real-world computer vision applications.

---

## 🚀 Workflow

```text
Google Images
        │
        ▼
Web Scraping (Selenium)
        │
        ▼
Custom Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Dataset Cleaning
        │
        ▼
CNN Training
        │
        ▼
Model Evaluation
        │
        ▼
Prediction on New Images
```

---

## 📂 Dataset

Since no suitable public dataset was available for this task, a custom dataset was created from scratch (test.py file).

The dataset creation process consisted of:

- Web scraping Google Images using Selenium
- Downloading approximately 100 images per search query
- Organizing images by character
- Manual inspection and removal of irrelevant images
- Removing low-resolution images
- Removing duplicate images using perceptual hashing (pHash)
- Converting every image to RGB format
- Uploading the cleaned dataset to Kaggle for reproducibility

> **Note:** The dataset is hosted on Kaggle and downloaded directly within the notebook.

---

## 📊 Exploratory Data Analysis

The notebook includes an extensive exploratory analysis covering:

- Dataset overview
- Number of images per character
- Image resolution analysis
- Width and height distributions
- Aspect ratio analysis
- Detection of corrupted images
- Detection of low-resolution images

---

## 🧹 Dataset Cleaning

Several preprocessing steps were applied before training:

- Removing corrupted files
- Removing low-resolution images
- Removing duplicate images
- Standardizing image color format (RGB)

These steps improve the consistency and overall quality of the dataset.

---

## 🧠 Model

A baseline Convolutional Neural Network (CNN) was implemented using TensorFlow/Keras.

Architecture:

- Data augmentation
- Rescaling layer
- 3 Convolutional blocks
- MaxPooling
- Dense layers
- Softmax output

The objective of this model is to establish a baseline for future experiments using more advanced architectures.

---

## 📈 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The notebook also includes:

- Learning curves
- Classification report
- Prediction on unseen images
- Top-5 predicted classes

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- Selenium
- BeautifulSoup
- Pillow
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Kaggle API

---

## 📷 Example Prediction

Input image:

*(Insert example image here)*

Prediction:

```
Spider-Man
Confidence: 93.7%
```

Top-5 predictions:

```
Spider-Man ..........93.7%
Iron Man .............3.4%
Black Panther.........1.5%
Thor..................0.8%
Hulk..................0.6%
```

---

## 💡 Future Work

Possible improvements include:

- Transfer Learning (ResNet50, EfficientNet, ConvNeXt)
- Data augmentation
- Hyperparameter optimization
- Increasing the number of images per class
- Object detection using YOLO
- Grad-CAM for model interpretability

---

## 📖 How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/Marvel-Character-Classification.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your Kaggle API credentials

```
~/.kaggle/kaggle.json
```

Run the notebook.

---

## 👤 Author

**Luceth Caterine Argote Radillo**

Applied Mathematics & Computer Science

GitHub: https://github.com/bl8dyg1rl
