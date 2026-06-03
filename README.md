# Xiaohongshu (Little Red Book) ROI Decision Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Submission for the Google Cloud Rapid Agent Hackathon 2026**

## 🎯 About The Project

AI that doesn't just provide answers—it helps you take action. 

This project is an AI Agent powered by **Gemini 3** and **Google Cloud Agent Builder**, designed to solve a real-world challenge for content creators on Xiaohongshu (Little Red Book), China's premier lifestyle community platform.

### The Challenge
Creators often struggle to decide which topics ("选题") are worth their time. Creating high-quality content takes hours, and guessing what the audience wants leads to low Return on Investment (ROI).

### The Solution: The ROI Decision Agent
This Agent acts as a data-driven decision-maker. Before a creator starts working on a topic, they ask the Agent: *"Is this topic worth doing?"*

The Agent orchestrates a multi-step mission to find the answer:
1. **Query Historical Data**: Uses the **MongoDB MCP Server** to analyze the user's past content performance, engagement rates, and monetization history.
2. **Scan Market Trends**: Uses the **Elastic MCP Server** to search current platform hot words, competitor data, and blue-ocean opportunities.
3. **Predict ROI**: Gemini 3 reasons over this data to calculate an expected ROI score, predicted engagement, and monetization potential, giving a final 1-10 recommendation.

## 🚀 Built With

* **Brain**: Gemini 3 
* **Orchestration**: Google GenAI SDK & MCP (Model Context Protocol)
* **Partner Power 1**: MongoDB MCP Server (User's Historical Data)
* **Partner Power 2**: Elastic MCP Server (Market Trends & Competitor Data)
* **Frontend**: Streamlit

## 🏁 Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud Vertex AI access (Gemini 3)
- MongoDB Atlas cluster
- Elastic Cloud deployment

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your-username/xiaohongshu-roi-agent.git
   cd xiaohongshu-roi-agent
   ```
2. Set up the virtual environment
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`
   ```sh
   GOOGLE_API_KEY="your_api_key"
   MONGODB_URI="your_mongodb_uri"
   ELASTIC_ENDPOINT="your_elastic_endpoint"
   ELASTIC_API_KEY="your_elastic_api_key"
   ```

### Running the Agent

1. Generate mock data to test the pipeline:
   ```sh
   python scripts/generate_mock_data.py
   python scripts/upload_to_mongodb.py
   python scripts/upload_to_elastic.py
   ```
2. Start the Streamlit UI:
   ```sh
   streamlit run app.py
   ```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
