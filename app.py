import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load env variables
load_dotenv()

st.set_page_config(page_title="小红书 ROI 决策 Agent", page_icon="📈", layout="wide")

# Tools definition
def query_my_notes(category: str, limit: int = 10) -> str:
    """查询用户的历史小红书笔记数据，用于分析历史表现。
    
    Args:
        category: 内容分类（例如: 感情观点, AI讨论, 投资思维, 生活分享）
        limit: 返回的记录数量
    """
    try:
        df = pd.read_csv('data/xiaohongshu_mock_notes.csv', encoding='utf-8')
        filtered = df[df['内容分类'] == category].sort_values(by='总互动', ascending=False).head(limit)
        if filtered.empty:
            return f"没有找到分类为 '{category}' 的历史数据。"
        
        # Calculate averages
        avg_likes = filtered['赞数'].mean()
        avg_revenue = filtered['变现额(元)'].mean()
        
        summary = f"找到 {len(filtered)} 条 '{category}' 的历史笔记。\n"
        summary += f"平均赞数: {avg_likes:.0f}, 平均变现额: ¥{avg_revenue:.2f}\n\n"
        summary += "Top 笔记表现:\n"
        for _, row in filtered.iterrows():
            summary += f"- {row['笔记标题']} (互动:{row['总互动']}, 变现:¥{row['变现额(元)']})\n"
        return summary
    except Exception as e:
        return f"查询失败: {str(e)}"

def search_xiaohongshu_trends(keyword: str, date_range: str = "last_7_days") -> str:
    """搜索小红书市场热词和竞品数据。
    
    Args:
        keyword: 搜索关键词
        date_range: 时间范围
    """
    # 模拟从 Elastic 检索竞品数据
    import random
    trend_score = random.randint(60, 100)
    competitor_likes = random.randint(1000, 50000)
    
    return (
        f"关键词 '{keyword}' 市场分析报告:\n"
        f"- 市场热度指数: {trend_score}/100\n"
        f"- 竞品平均互动量: {competitor_likes}\n"
        f"- 流量竞争程度: {'红海 (激烈)' if trend_score > 85 else '蓝海 (有机会)'}\n"
        f"- 热门内容形式: 视频/图文 结合\n"
    )

def init_agent():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "your_api_key":
        return None
    
    # Read system prompt
    try:
        with open('agent/system_prompt.txt', 'r', encoding='utf-8') as f:
            system_prompt = f.read()
    except:
        system_prompt = "你是一个小红书内容 ROI 决策专家。"
        
    client = genai.Client(api_key=api_key)
    
    # We create a function to call the model
    def ask_agent(user_message):
        response = client.models.generate_content(
            model='gemini-3.1-pro',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[query_my_notes, search_xiaohongshu_trends],
                temperature=0.7,
            )
        )
        return response.text
        
    return ask_agent

# UI Layout
st.title("📈 小红书 ROI 决策 Agent")
st.markdown("""
**Google Cloud Rapid Agent Hackathon 参赛作品**
该 Agent 集成了 Gemini 3 的高级推理能力，并通过连接 MongoDB (你的历史数据) 和 Elastic (市场大盘) 来帮助你做出高 ROI 的内容决策。
*(注意：为方便演示，目前使用的是本地生成的 mock data 工具模拟 MCP server 调用)*
""")

ask_agent_func = init_agent()

if not ask_agent_func:
    st.error("⚠️ 请先在 `.env` 文件中配置 `GOOGLE_API_KEY` (Gemini API Key)。")
    st.stop()

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []
    
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("例：帮我评估一下 '35岁未婚女性的财务独立' 这个选题，我想配一个理财课程变现。"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("Agent 正在查询历史数据并进行市场预测..."):
            try:
                response_text = ask_agent_func(prompt)
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Agent 调用失败: {str(e)}")
