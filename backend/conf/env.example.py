import os

from application.settings import BASE_DIR

# ================================================= #
# ************** 数据库 配置  ************** #
# ================================================= #
#
# 数据库 ENGINE ，默认演示使用 sqlite3 数据库，正式环境建议使用 mysql 数据库
DATABASE_ENGINE = "django.db.backends.sqlite3"
# 数据库名
DATABASE_NAME = os.path.join(BASE_DIR, 'db.sqlite3')
# 数据库地址 改为自己数据库地址
DATABASE_HOST = "127.0.0.1"
# 数据库端口
DATABASE_PORT = 3306
# 数据库用户名
DATABASE_USER = "root"
# 数据库密码
DATABASE_PASSWORD = "123456"
# ================================================= #
# ************** redis配置，无redis 可不进行配置  ************** #
# ================================================= #
# REDIS_PASSWORD = ''
# REDIS_HOST = '127.0.0.1'
# REDIS_URL = f'redis://:{REDIS_PASSWORD or ""}@{REDIS_HOST}:6380'
# ================================================= #
# ************** 其他 配置  ************** #
# ================================================= #
DEBUG = True  # 线上环境请设置为True
ALLOWED_HOSTS = ["*"]
LOGIN_NO_CAPTCHA_AUTH = True  # 登录接口 /api/token/ 是否需要验证码认证，用于测试，正式环境建议取消
