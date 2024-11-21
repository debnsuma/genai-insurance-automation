<div align="center">  
  <h1 style="color: #2F80ED; font-size: 3em; margin-bottom: 0;">
    🚗 Insurance Operations Automation with Generative AI using Amazon Bedrock
  </h1>

  <div style="margin: 20px 0;">
    <a href="https://reinvent.awsevents.com/">
      <img src="https://img.shields.io/badge/AWS_re:Invent_2024-DEV333-FF9900?style=for-the-badge&logo=amazon-aws" alt="AWS re:Invent 2024"/>
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-FF9900?style=for-the-badge" alt="License: MIT"/>
    </a>
  </div>
</div>

## 📋 Overview

Insurance companies manage extensive procedure documents, making manual processing time-consuming and complex. This repository demonstrates a generative AI-based solution to automate and scale these operations. Learn how to build an end-to-end generative AI-based robotic process automation (RPA) solution to understand procedure documents with rules, tables, and images and perform operations according to customers' data by leveraging generative AI and large language models (LLMs).

## 🎯 Repository Structure

This repository is divided into two main sections:

### [Part 1: Beginner's Guide - Insurance Renewal Prediction 🔮](Part1-Code%20Generation/README.md)

![Insurance Renewal Prediction](img/renewal.jpeg)

A comprehensive solution demonstrating how to leverage generative AI to create ML models for predicting insurance renewal likelihood using Amazon Bedrock.

### Business Context

- 🚘 **Domain:** Automobile Insurance
- 🛡️ **Coverage:** Physical damage, bodily injury, theft, fire, flood protection
- 📊 **Challenge:** Optimizing customer renewal outreach
- 💼 **Market Reality:** Only ~14% of customers agree to renewal

### Technical Stack
- ⚡ Amazon Bedrock with Claude model
- 🐍 Python ML libraries (scikit-learn)
- 📊 Pandas for data processing
- 🔧 AWS SDK for Python (Boto3)

### Model Performance
- 🎯 **Accuracy:** 87%
- ✨ **Precision:** 68%
- 🔍 **Recall:** 16%
- ⚖️ **F1-score:** 26%

### [Part 2: Advanced Implementation - Intelligent Claims Processing 🤖](Part2-Insurance%20Claim%20Lifecycle/README.md)

![Architecture Diagram](Part2-Insurance%20Claim%20Lifecycle/design/agent-overview.png)

### 💰 Cost Estimation (Monthly)

| Service | Cost |
|---------|------|
| 📦 Amazon S3 | $121.11 |
| 🔍 Amazon OpenSearch | $591.36 |
| λ AWS Lambda | $0.10 |
| 🤖 Agents and Knowledge Bases | $54.00 |
| 💵 **Total** | **$766.57** |

### 🔥 Key Capabilities

- 🤖 Task Orchestration
- 🔄 Interactive Data Collection
- 🔌 Task Fulfillment
- 💬 System Integration
- 📚 Data Querying
- 📋 Source Attribution

## 🚀 Getting Started

```bash
# Clone the Repository
git clone https://github.com/yourusername/insurance-genai-automation.git

# Navigate to Desired Section
cd Part1-Code Generation
# or
cd Part2-Insurance-Claim-Lifecycle

# Install Dependencies
pip install -r requirements.txt
```

### Configure AWS Credentials
```python
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 3,
        'mode': 'standard'
    }
)

client = boto3.client("bedrock-runtime", config = my_config)
```

## 📊 Project Structure

```
.
├── Part1-Code Generation/
│   ├── data/
│   │   ├── data_ml.csv
│   │   └── data_ml_test.csv
│   ├── src/
│   │   └── claude_llm_invocation.py
│   ├── playground.ipynb
│   ├── model_code.py
│   └── README.md
├── Part2-Insurance-Claim-Lifecycle/
│   ├── agents/
│   │   ├── action-groups/
│   │   └── prompts/
│   ├── knowledge-base/
│   │   ├── data/
│   │   └── config/
│   ├── design/
│   │   └── agent-overview.png
│   ├── documentation/
│   │   ├── deployment-guide.md
│   │   ├── testing-and-validation.md
│   │   └── clean-up.md
│   └── README.md
├── LICENSE
├── .gitignore
└── README.md
```

### Directory Structure Overview

- **Part1-Code Generation**: Contains the beginner's guide implementation for insurance renewal prediction
- **Part2-Insurance-Claim-Lifecycle**: Houses the advanced implementation using Amazon Bedrock Agents
- **Documentation**: Comprehensive guides for deployment, testing, and cleanup
