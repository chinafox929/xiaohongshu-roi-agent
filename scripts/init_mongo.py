import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def init_mongodb():
    uri = os.getenv("MONGODB_URI")
    if not uri or "<db_password>" in uri:
        print("Error: 请先在 .env 文件中填入真实的 MongoDB 密码！")
        return

    print("正在连接 MongoDB Atlas...")
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # 测试连接
        client.admin.command('ping')
        print("MongoDB 连接成功！")
        
        db = client['xiaohongshu_db']
        collection = db['notes']
        
        print("正在读取本地 CSV 数据...")
        df = pd.read_csv('data/xiaohongshu_mock_notes.csv', encoding='utf-8')
        records = df.to_dict(orient='records')
        
        print(f"准备插入 {len(records)} 条记录...")
        collection.delete_many({}) # 清空旧数据
        collection.insert_many(records)
        print("数据成功导入 MongoDB！")
        
    except Exception as e:
        print(f"MongoDB 初始化失败: {e}")

if __name__ == "__main__":
    init_mongodb()
