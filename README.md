<div align="center">  
  <h1 style="color: #2F80ED; font-size: 3em; margin-bottom: 0;">
    🚗 Insurance Operations Automation with Generative AI using Amazon Bedrock
  </h1>

  <div style="margin: 20px 0;">
    <a href="https://reinvent.awsevents.com/">
      <img src="https://img.shields.io/badge/AWS_re:Invent_2024-DEV333-FF9900?style=for-the-badge&logo=amazon-aws" alt="AWS re:Invent 2024"/>
    </a>
    <a href="https://github.com/debnsuma/genai-insurance-automation/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-FF9900?style=for-the-badge" alt="License: MIT"/>
    </a>
    <a href="https://github.com/debnsuma/genai-insurance-automation/stargazers">
      <img src="https://img.shields.io/github/stars/build-on-aws?style=for-the-badge&color=blue" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/debnsuma/genai-insurance-automation/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/debnsuma/genai-insurance-automation?style=for-the-badge&color=green" alt="GitHub license"/>
    </a>
  </div>
</div>

## 📋 Overview

Insurance companies manage extensive procedure documents, making manual processing time-consuming and complex. This repo contains the code used for building an Automation Solution for Insurance Operation Process via Text-to-Code.This repository also demonstrates a generative AI-based solution to automate and scale these operations. Learn how to build an end-to-end generative AI-based robotic process automation (RPA) solution to understand procedure documents with rules, tables, and images and perform operations according to customers' data by leveraging generative AI and large language models (LLMs) using Amazon Bedrock. 

## 🎯 Repository Structure

This repository is divided into two main sections:

- [Part 1: Beginner's Guide - Insurance Renewal Prediction 🔮](Part1-Code%20Generation/README.md)
- [Part 2: Advanced Implementation - Intelligent Claims Processing 🤖](Part2-Insurance%20Claim%20Lifecycle/README.md)

## 📊 Project Structure

Follow the directory structure below to navigate through the code:
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


## [Part 1: Beginner's Guide - Insurance Renewal Prediction 🔮](Part1-Code%20Generation/README.md)

This section demonstrates how to leverage generative AI to create a machine learning model for predicting insurance renewal likelihood. We use Amazon Bedrock's Claude model to generate production-ready Python code for data analysis and model training.

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

## [Part 2: Advanced Implementation - Intelligent Claims Processing 🤖](Part2-Insurance%20Claim%20Lifecycle/README.md)

You can now use [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) and [Knowledge Bases for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) to configure specialized agents that seamlessly run actions based on user input and your organization's data. These managed agents play conductor, orchestrating interactions between foundation models (FMs), API integrations, user conversations, and knowledge bases loaded with your data. 

This sample solution highlights how you can use Agents and Knowledge Bases for Amazon Bedrock to **build on existing enterprise resources** to automate the tasks associated with the insurance claim lifecycle, efficiently scale and improve customer service, and enhance decision support through improved knowledge management. Your Bedrock-powered insurance agent can assist human agents by creating new claims, sending pending document reminders for open claims, gathering claims evidence, and searching for information across existing claims and customer knowledge repositories.

### Agents and Knowledge Bases for Amazon Bedrock

Agents and Knowledge Bases for Amazon Bedrock work together to provide the following set of capabilities:

- **Task Orchestration** - Agents expand FMs to understand natural language user inquiries and dissect multi-step tasks into smaller, executable steps.
- **Interactive Data Collection** - Agents engage in natural conversations to gather supplementary information from users.
- **Task Fulfillment** - Agents complete customer requests through series of reasoning steps and corresponding actions based on [ReAct prompting](https://www.promptingguide.ai/techniques/react).
- **System Integration** - Agents make API calls to integrated company systems to run specific actions.
- **Data Querying** - Knowledge bases enhance accuracy and performance through fully-managed [retrieval augmented generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) using customer specific data sources.
- **Source Attribution** - Agents conduct source attribution, identifying and tracing the origin of information or actions through chain-of-thought reasoning.

### Agents and Knowledge Bases Architecture

The workflow consists of the following steps:

![Architecture Diagram](Part2-Insurance%20Claim%20Lifecycle/design/agent-overview.png)

1. Users provide natural language inputs to the agent.

    **Sample Prompts:**
    - _Create a new claim._
    - _Send a pending documents reminder to the policy holder of claim ID 2s34w-8x._
    - _Gather evidence for claim ID 5t16u-7v._
    - _What is the total claim amount for claim ID 3b45c-9d?_
    - _What is the total repair estimate for that same claim?_
    - _What factors determine my car insurance premium?_
    - _How can I lower my car insurance rates?_
    - _Which claims have open status?_
    - _Send pending document reminders to all policy holders with open claims._
      
2. During **pre-processing**, the agent validates, contextualizes, and categorizes user input. The user input (or _Task_) is interpreted by the agent using chat history and the instructions and underlying foundation model that were specified during [agent creation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html). The agent's [instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) are descriptive guidelines outlining the agent's intended actions. Also, you can optionally configure [advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html), which allow you to boost your agent's precision by employing more detailed configurations and offering manually selected examples for few-shot prompting. This method allows you to enhance the model's performance by providing labeled examples associated with a particular task. 

3. [Action groups](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-setup.html) are a set of APIs and corresponding business logic, whose OpenAPI schema is defined as JSON files stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (S3). The schema allows the agent to reason around the function of each API. Each action group can specify one or more API paths, whose business logic is run through the [AWS Lambda](http://aws.amazon.com/lambda) function associated with the action group.

4. Knowledge bases provide fully-managed RAG to supply the agent with access to your data. You first configure the knowledge base by specifying a description that instructs the agent when to use your knowledge base. Then you point the knowledge base to your Amazon S3 data source. Finally, you specify an embedding model and choose to use your existing vector store or allow Bedrock to create the vector store on your behalf. Once configured, each [data source sync](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ingest.html) creates vector embeddings of your data that the agent can use to return information to the user or augment subsequent FM prompts.

5. During **orchestration**, the agent develops a _rational_ with the logical steps of which action group API invocations and knowledge base queries are needed to generate an _observation_ that can be used to augment the base prompt for the underlying FM. This ReAct style of prompting serves as the input for activating the FM, which then anticipates the most optimal sequence of actions to complete the user's task.

6. During **post-processing**, once all _orchestration_ iterations are complete, the agent curates a final response. Post-processing is disabled by default.

## 🚀 Getting Started

```bash
# Clone the Repository
git clone https://github.com/yourusername/insurance-genai-automation.git

# Navigate to Desired Section
cd Part2-Insurance-Claim-Lifecycle

# Install Dependencies
pip install -r requirements.txt
```

## Configure AWS Credentials
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

## Directory Structure Overview

- [**Part1-Code Generation**](Part1-Code%20Generation/README.md): Contains the beginner's guide implementation for insurance renewal prediction
- [**Part2-Insurance-Claim-Lifecycle**](Part2-Insurance%20Claim%20Lifecycle/README.md): Houses the advanced implementation using Amazon Bedrock Agents
- [**Documentation**](Part2-Insurance%20Claim%20Lifecycle/documentation/README.md): Comprehensive guides for deployment, testing, and cleanup
