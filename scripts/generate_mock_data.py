import pandas as pd
import numpy as np
import datetime
import random
import os

def generate_notes_data(num_records=100):
    """Generate mock Xiaohongshu notes history for the user."""
    categories = ['感情观点', 'AI讨论', '投资思维', '生活分享', '电音文化']
    
    data = []
    start_date = datetime.date(2023, 1, 1)
    
    for i in range(num_records):
        note_id = f"note_{str(i+1).zfill(4)}"
        category = random.choice(categories)
        
        # Base stats depending on category
        if category == '感情观点':
            likes = random.randint(500, 20000)
            revenue = random.randint(0, 5000)
            cost = random.uniform(1.0, 3.0)
        elif category == 'AI讨论':
            likes = random.randint(100, 10000)
            revenue = random.randint(0, 2000)
            cost = random.uniform(2.0, 5.0)
        elif category == '投资思维':
            likes = random.randint(200, 15000)
            revenue = random.randint(1000, 15000)
            cost = random.uniform(3.0, 6.0)
        else:
            likes = random.randint(50, 5000)
            revenue = 0
            cost = random.uniform(0.5, 2.0)
            
        comments = int(likes * random.uniform(0.05, 0.2))
        collects = int(likes * random.uniform(0.1, 0.5))
        shares = int(likes * random.uniform(0.01, 0.1))
        
        total_interaction = likes + comments + collects + shares
        
        # Publish date
        days_offset = random.randint(0, 365)
        publish_date = start_date + datetime.timedelta(days=days_offset)
        
        data.append({
            '笔记ID': note_id,
            '笔记标题': f"关于{category}的{random.randint(1,99)}个思考",
            '发布时间': publish_date.strftime("%Y-%m-%d"),
            '文字内容': f"这是一篇关于{category}的分享内容...",
            '内容分类': category,
            '赞数': likes,
            '评论数': comments,
            '收藏数': collects,
            '分享数': shares,
            '总互动': total_interaction,
            '变现额(元)': revenue,
            '变现方式': '课程' if revenue > 0 else '无',
            '制作成本(小时)': round(cost, 1)
        })
        
    df = pd.DataFrame(data)
    
    # Ensure data dir exists
    os.makedirs('data', exist_ok=True)
    file_path = 'data/xiaohongshu_mock_notes.csv'
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f"Success: {num_records} mock records generated -> {file_path}")
    return file_path

if __name__ == "__main__":
    print("开始生成模拟数据...")
    generate_notes_data(100)
