import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def upload_to_mongodb():
    """Uploads the generated mock data to MongoDB."""
    mongo_uri = os.getenv("MONGODB_URI")
    
    if not mongo_uri or mongo_uri == "your_mongodb_uri":
        print("Warning: 未配置 MONGODB_URI，跳过 MongoDB 真实上传。将使用本地 mock 模式演示。")
        return
        
    print(f"Connecting to MongoDB...")
    try:
        client = MongoClient(mongo_uri)
        db = client['xiaohongshu_roi']
        collection = db['notes']
        
        # Read data
        file_path = 'data/xiaohongshu_mock_notes.csv'
        if not os.path.exists(file_path):
            print(f"Error: 数据文件 {file_path} 不存在，请先运行 generate_mock_data.py")
            return
            
        df = pd.read_csv(file_path, encoding='utf-8')
        records = df.to_dict('records')
        
        # Clear old data and insert new
        collection.delete_many({})
        result = collection.insert_many(records)
        
        print(f"Success: 成功导入 {len(result.inserted_ids)} 条记录到 MongoDB!")
        print(f"Stats: 当前数据库中总记录数：{collection.count_documents({})}")
        
    except Exception as e:
        print(f"Error: 连接或上传 MongoDB 失败: {e}")

if __name__ == "__main__":
    upload_to_mongodb()
