# Part 1: Insurance Renewal Prediction with Generative AI 🔮

![Insurance Renewal Prediction](../img/renewal.jpeg)

## 📋 Overview

This section demonstrates how to leverage generative AI to create a machine learning model for predicting insurance renewal likelihood. We use Amazon Bedrock's Claude model to generate production-ready Python code for data analysis and model training.

## 🎯 Business Context

- **Industry**: Automobile Insurance
- **Challenge**: Predicting customer insurance renewal
- **Current State**: Only ~14% customers agree to renewal
- **Goal**: Optimize customer outreach and increase renewal rates

## 📊 Dataset Description

The dataset (`data_ml.csv`) contains customer information including:
- Customer Lifetime Value
- Coverage types
- Education level
- Demographics (Gender, Income)
- Monthly Premium Auto
- Number of Policies
- Total Claim Amount
- Various encoded features (Sales Channel, Vehicle Class, etc.)

## 🛠️ Getting Started

- Clone the repository 
    ```bash
    git clone https://github.com/aws-samples/amazon-bedrock-generative-ai-insurance-renewal-prediction.git
    cd amazon-bedrock-generative-ai-insurance-renewal-prediction/Part1-Code-Generation
    ```
- Open the notebook [insurance_renewal_prediction.ipynb](insurance_renewal_prediction.ipynb)
    ```bash
    jupyter notebook insurance_renewal_prediction.ipynb
    ```
- Follow the instructions in the notebook to run the code

