import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from app import create_app
from models.models import db, School

def init_db():
    app = create_app('development')
    
    with app.app_context():
        # 清空现有数据
        db.drop_all()
        db.create_all()
        
        # 创建示例学校数据
        schools_data = [
            {
                "name": "中央美术学院",
                "location": "北京",
                "type": "美术"
            },
            {
                "name": "清华大学美术学院",
                "location": "北京",
                "type": "美术"
            }
        ]
        
        for school_data in schools_data:
            school = School(**school_data)
            db.session.add(school)
        
        db.session.commit()
        print("数据库初始化完成")

if __name__ == '__main__':
    init_db() 