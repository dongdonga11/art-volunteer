from flask import Flask
from config import config
from utils.logger import setup_logger
from routes.schools import schools_bp
from routes.volunteers import volunteers_bp
from models.models import db
import os

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(config[config_name])
    
    # 设置日志
    setup_logger(app)
    
    # 初始化数据库
    db.init_app(app)
    
    # 注册蓝图
    app.register_blueprint(schools_bp)
    app.register_blueprint(volunteers_bp)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run(host='0.0.0.0', port=3000) 