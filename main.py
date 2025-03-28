import os
import sys
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    # 启动开发服务器（修改端口号为8001）
    execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8001'])