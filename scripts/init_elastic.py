import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

def init_elastic():
    endpoint = os.getenv("ELASTIC_ENDPOINT")
    api_key = os.getenv("ELASTIC_API_KEY")
    
    if not endpoint or not api_key:
        print("Error: 找不到 Elastic 配置信息！")
        return

    print("正在连接 Elastic Cloud...")
    try:
        client = Elasticsearch(
            endpoint,
            api_key=api_key,
            request_timeout=30
        )
        
        # 测试连接
        info = client.info()
        print("Elastic Cloud 连接成功！")
        
        index_name = "xiaohongshu_trends"
        
        # 如果索引不存在，则创建
        if not client.indices.exists(index=index_name):
            client.indices.create(index=index_name)
            print(f"创建索引 {index_name} 成功！")
            
        # 写入一些测试的趋势数据
        trends_data = [
            {"keyword": "35岁未婚女性的财务独立", "trend_score": 88, "competitor_likes": 4500, "competition": "蓝海"},
            {"keyword": "AI工具变现", "trend_score": 95, "competitor_likes": 12000, "competition": "红海"},
            {"keyword": "副业搞钱", "trend_score": 92, "competitor_likes": 8000, "competition": "红海"},
            {"keyword": "情绪价值小红书", "trend_score": 75, "competitor_likes": 2000, "competition": "蓝海"}
        ]
        
        print("正在写入趋势数据...")
        for i, doc in enumerate(trends_data):
            client.index(index=index_name, id=i, document=doc)
            
        print("数据成功导入 Elastic Cloud！")
        
    except Exception as e:
        print(f"Elastic 初始化失败: {e}")

if __name__ == "__main__":
    init_elastic()
