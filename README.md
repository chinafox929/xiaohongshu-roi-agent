# Xiaohongshu (Little Red Book) ROI Decision Agent / 小红书 ROI 决策 Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Submission for the Google Cloud Rapid Agent Hackathon 2026** / **Google Cloud Rapid Agent 黑客松 2026 参赛作品**

## 🎯 About The Project (项目简介)

AI that doesn't just provide answers—it helps you take action. / 一个不仅能回答问题，还能指导你采取行动的 AI。

This project is an AI Agent powered by **Gemini** and designed to solve a real-world challenge for content creators on Xiaohongshu (Little Red Book), China's premier lifestyle community platform.
本项目是一个基于 **Gemini** 的 AI Agent，专为解决中国头部生活方式社区“小红书”内容创作者在现实中遇到的挑战而设计。

### The Challenge (痛点挑战)
Creators often struggle to decide which topics ("选题") are worth their time. Creating high-quality content takes hours, and guessing what the audience wants leads to low Return on Investment (ROI).
创作者经常纠结于哪些“选题”值得投入时间。制作高质量内容需要耗费数小时，而盲目猜测受众喜好往往导致投资回报率（ROI）极低。

### The Solution: The ROI Decision Agent (解决方案)
This Agent acts as a data-driven decision-maker. Before a creator starts working on a topic, they ask the Agent: *"Is this topic worth doing?"*
这个 Agent 扮演了数据驱动的决策者角色。在创作者开始动笔前，他们只需向 Agent 提问：“这个选题值得做吗？”

The Agent orchestrates a multi-step mission to find the answer:
Agent 会在后台执行多步任务来寻找答案：
1. **Query Historical Data (查询历史数据)**: Connects to **MongoDB Atlas** to analyze the user's past content performance, engagement rates, and monetization history. / 直连 **MongoDB Atlas** 集群，分析用户过去的内容表现、互动率和变现历史。
2. **Scan Market Trends (扫描市场大盘)**: Connects to **Elastic Cloud** to search current platform hot words, competitor data, and blue-ocean opportunities. / 直连 **Elastic Cloud**，检索当前平台热词、竞品数据和蓝海机会。
3. **Predict ROI (预测 ROI)**: Gemini reasons over this data to calculate an expected ROI score, predicted engagement, and monetization potential, giving a final 1-10 recommendation. / Gemini 结合以上数据进行推理计算，预估 ROI 评分、互动潜力和变现可能，最终给出 1-10 分的行动建议。

## 🚀 Built With (技术栈)

* **Brain**: Gemini 1.5 Flash (Fallback logic implemented for API limits)
* **Partner Power 1**: MongoDB Atlas (Cloud Database for User's Historical Data)
* **Partner Power 2**: Elastic Cloud Serverless (Search Engine for Market Trends)
* **Frontend**: Streamlit

## 🏁 Getting Started (如何运行)

### Prerequisites (前置要求)

- Python 3.10+
- Google Gemini API Key
- MongoDB Atlas Cluster URI
- Elastic Cloud Endpoint & API Key

### Installation (安装步骤)

1. Clone the repo (克隆仓库)
   ```sh
   git clone https://github.com/chinafox929/xiaohongshu-roi-agent.git
   cd xiaohongshu-roi-agent
   ```
2. Set up the virtual environment (配置虚拟环境)
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies (安装依赖)
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env` (配置环境变量)
   ```sh
   GOOGLE_API_KEY="your_api_key"
   MONGODB_URI="your_mongodb_uri"
   ELASTIC_ENDPOINT="your_elastic_endpoint"
   ELASTIC_API_KEY="your_elastic_api_key"
   ```

### Running the Agent (运行 Agent)

1. Initialize Cloud Databases with sample data (将初始数据注入云端数据库):
   ```sh
   python scripts/init_mongo.py
   python scripts/init_elastic.py
   ```
2. Start the Streamlit UI (启动界面):
   ```sh
   streamlit run app.py
   ```

## 📜 License (开源协议)

Distributed under the MIT License. See `LICENSE` for more information.
