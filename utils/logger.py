import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(app):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )

    file_handler = RotatingFileHandler(
        'logs/art_volunteer.log', 
        maxBytes=10240, 
        backupCount=10
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('艺术生志愿填报系统启动') 