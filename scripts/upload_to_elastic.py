import os
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def upload_to_elastic():
    """Uploads the generated mock data to Elasticsearch."""
    es_endpoint = os.getenv("ELASTIC_ENDPOINT")
    es_api_key = os.getenv("ELASTIC_API_KEY")
    
    if not es_endpoint or es_endpoint == "your_elastic_endpoint":
        print("Warning: 未配置 ELASTIC_ENDPOINT，跳过 Elasticsearch 真实上传。将使用本地 mock 模式演示。")
        return
        
    print(f"Connecting to Elasticsearch...")
    try:
        es = Elasticsearch(
            [es_endpoint],
            api_key=es_api_key
        )
        
        # Read data
        file_path = 'data/xiaohongshu_mock_notes.csv'
        if not os.path.exists(file_path):
            print(f"Error: 数据文件 {file_path} 不存在，请先运行 generate_mock_data.py")
            return
            
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # Create bulk actions
        index_name = "xiaohongshu_notes"
        actions = []
        for idx, row in df.iterrows():
            action = {
                "_index": index_name,
                "_id": str(row['笔记ID']),
                "_source": row.to_dict()
            }
            actions.append(action)
        
        # Execute bulk upload
        success, _ = bulk(es, actions)
        print(f"Success: 成功导入 {success} 条记录到 Elasticsearch 索引 '{index_name}'!")
        
        # Verify
        es.indices.refresh(index=index_name)
        count = es.count(index=index_name)
        print(f"Stats: Elasticsearch 中的总记录数：{count['count']}")
        
    except Exception as e:
        print(f"Error: 连接或上传 Elasticsearch 失败: {e}")

if __name__ == "__main__":
    upload_to_elastic()
