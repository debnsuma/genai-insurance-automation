<div align="center">
  <h1 style="color: #2F80ED; font-size: 3em; margin-bottom: 0;">
    🚗 Insurance Operations Automation with Generative AI
  </h1>
  
  <div style="margin: 20px 0;">
    <a href="https://reinvent.awsevents.com/">
      <img src="https://img.shields.io/badge/AWS_re:Invent_2024-DEV333-FF9900?style=for-the-badge&logo=amazon-aws" alt="AWS re:Invent 2024"/>
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/>
    </a>
  </div>

  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px 0; color: white;">
    <p style="font-size: 1.2em; margin: 0;">
      Supporting repository for AWS re:Invent 2024 session <strong>DEV333</strong>: Automating insurance claims and policy management using generative AI
    </p>
  </div>
</div>

<h2 align="center" style="color: #4A5568; border-bottom: 2px solid #4A5568; padding-bottom: 10px;">
  📋 Overview
</h2>

<div style="background-color: #F7FAFC; border-left: 4px solid #4299E1; padding: 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
  Insurance companies manage extensive procedure documents, making manual processing time-consuming and complex. This repository demonstrates a generative AI-based solution to automate and scale these operations. Learn how to build an end-to-end generative AI-based robotic process automation (RPA) solution to understand procedure documents with rules, tables, and images and perform operations according to customers' data by leveraging generative AI and large language models (LLMs).
</div>

<h2 align="center" style="color: #4A5568; border-bottom: 2px solid #4A5568; padding-bottom: 10px;">
  🎯 Repository Structure
</h2>

This repository is divided into two main sections:

<div style="background: linear-gradient(135deg, #48BB78 0%, #38B2AC 100%); color: white; padding: 2px; border-radius: 10px; margin: 20px 0;">
  <h3 style="background: white; color: #2D3748; margin: 0; padding: 15px; border-radius: 8px 8px 0 0;">
    Part 1: Beginner's Guide - Insurance Renewal Prediction 🔮
  </h3>
  <div style="padding: 20px;">
    <img src="https://decoratex.biz/bsn/fr/static/img/a/42515/466437/77586.jpg" alt="Insurance Renewal Prediction" style="width: 100%; border-radius: 8px; margin-bottom: 20px;">
    
    <p style="color: white; font-size: 1.1em;">
      A comprehensive solution demonstrating how to leverage generative AI to create ML models for predicting insurance renewal likelihood using Amazon Bedrock.
    </p>
  </div>
</div>

<div style="background-color: #EBF8FF; border-radius: 10px; padding: 20px; margin: 20px 0;">
  <h4 style="color: #2B6CB0; margin-top: 0;">Business Context</h4>
  <ul style="list-style-type: none; padding-left: 0;">
    <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #4299E1;">
      🚘 <strong style="color: #2C5282;">Domain:</strong> Automobile Insurance
    </li>
    <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #4299E1;">
      🛡️ <strong style="color: #2C5282;">Coverage:</strong> Physical damage, bodily injury, theft, fire, flood protection
    </li>
    <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #4299E1;">
      📊 <strong style="color: #2C5282;">Challenge:</strong> Optimizing customer renewal outreach
    </li>
    <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #4299E1;">
      💼 <strong style="color: #2C5282;">Market Reality:</strong> Only ~14% of customers agree to renewal
    </li>
  </ul>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #4299E1 0%, #3182CE 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="color: white; margin-top: 0; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 10px;">
      🛠️ Technical Stack
    </h4>
    <ul style="list-style-type: none; padding-left: 0;">
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        ⚡ Amazon Bedrock with Claude model
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🐍 Python ML libraries (scikit-learn)
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        📊 Pandas for data processing
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🔧 AWS SDK for Python (Boto3)
      </li>
    </ul>
  </div>

  <div style="background: linear-gradient(135deg, #48BB78 0%, #38A169 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="color: white; margin-top: 0; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 10px;">
      📈 Model Performance
    </h4>
    <ul style="list-style-type: none; padding-left: 0;">
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🎯 <strong>Accuracy:</strong> 87%
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        ✨ <strong>Precision:</strong> 68%
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🔍 <strong>Recall:</strong> 16%
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        ⚖️ <strong>F1-score:</strong> 26%
      </li>
    </ul>
  </div>
</div>

<div style="background: linear-gradient(135deg, #805AD5 0%, #6B46C1 100%); color: white; padding: 2px; border-radius: 10px; margin: 20px 0;">
  <h3 style="background: white; color: #2D3748; margin: 0; padding: 15px; border-radius: 8px 8px 0 0;">
    Part 2: Advanced Implementation - Intelligent Claims Processing 🤖
  </h3>
  <div style="padding: 20px;">
    <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 8px; margin-bottom: 20px;">
      <img src="Part2-Insurance Claim Lifecycle/design/agent-overview.png" alt="Architecture Diagram" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
      <em style="color: rgba(255,255,255,0.8);">Diagram 1: Agents and Knowledge Bases for Amazon Bedrock Architecture Overview</em>
    </div>
  </div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #ED8936 0%, #DD6B20 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="color: white; margin-top: 0; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 10px;">
      💰 Cost Estimation (Monthly)
    </h4>
    <ul style="list-style-type: none; padding-left: 0;">
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        📦 <strong>Amazon S3:</strong> $121.11
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🔍 <strong>Amazon OpenSearch:</strong> $591.36
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        λ <strong>AWS Lambda:</strong> $0.10
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🤖 <strong>Agents and Knowledge Bases:</strong> $54.00
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.2); padding: 12px; border-radius: 5px; font-size: 1.1em;">
        💵 <strong>Total:</strong> $766.57
      </li>
    </ul>
  </div>

  <div style="background: linear-gradient(135deg, #4FD1C5 0%, #319795 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="color: white; margin-top: 0; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 10px;">
      🔥 Key Capabilities
    </h4>
    <ul style="list-style-type: none; padding-left: 0;">
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🤖 Task Orchestration
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🔄 Interactive Data Collection
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        🔌 Task Fulfillment
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        💬 System Integration
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        📚 Data Querying
      </li>
      <li style="margin: 8px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px;">
        📋 Source Attribution
      </li>
    </ul>
  </div>
</div>

<h2 align="center" style="color: #4A5568; border-bottom: 2px solid #4A5568; padding-bottom: 10px;">
  🚀 Getting Started
</h2>

<div style="background: linear-gradient(135deg, #F6E05E 0%, #ECC94B 100%); padding: 2px; border-radius: 10px; margin: 20px 0;">
  <div style="background: white; padding: 20px; border-radius: 8px;">
    <h4 style="color: #744210; margin-top: 0;">1. Clone the Repository</h4>
    
    ```bash
    git clone https://github.com/yourusername/insurance-genai-automation.git
    ```

    <h4 style="color: #744210;">2. Navigate to Desired Section</h4>
    
    ```bash
    cd Part1-Code Generation
    # or
    cd Part2-Insurance-Claim-Lifecycle
    ```

    <h4 style="color: #744210;">3. Install Dependencies</h4>
    
    ```bash
    pip install -r requirements.txt
    ```

    <h4 style="color: #744210;">4. Configure AWS Credentials</h4>
    
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
  </div>
</div>

<h2 align="center" style="color: #4A5568; border-bottom: 2px solid #4A5568; padding-bottom: 10px;">
  📊 Project Structure
</h2>

<div style="background: linear-gradient(135deg, #9F7AEA 0%, #805AD5 100%); padding: 2px; border-radius: 10px; margin: 20px 0;">
  <div style="background: white; padding: 20px; border-radius: 8px;">
    <pre style="background-color: #F7FAFC; padding: 15px; border-radius: 5px; overflow-x: auto;">
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
└── README.md</pre>

    <div style="margin-top: 20px; padding: 15px; background-color: #F7FAFC; border-radius: 5px;">
      <h4 style="color: #2D3748; margin-top: 0;">Directory Structure Overview</h4>
      <ul style="list-style-type: none; padding-left: 0;">
        <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #805AD5;">
          <strong style="color: #4A5568;">Part1-Code Generation:</strong> Contains the beginner's guide implementation for insurance renewal prediction
        </li>
        <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #805AD5;">
          <strong style="color: #4A5568;">Part2-Insurance-Claim-Lifecycle:</strong> Houses the advanced implementation using Amazon Bedrock Agents
        </li>
        <li style="margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px; border-left: 4px solid #805AD5;">
          <strong style="color: #4A5568;">Documentation:</strong> Comprehensive guides for deployment, testing, and cleanup
        </li>
      </ul>
    </div>
  </div>
</div>
