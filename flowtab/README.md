##从这里开始##  
##下载项目##  
git clone https://github.com/clearlove-luzude/flowtab.git  
本项目建议安装python3.6虚拟环境  
python3.6 -m venv python_env  
##进入虚拟环境##  
source python_env/bin/activate  
##下载关连包##  
pip -r install  requirements.txt  
  
在aliyun/settings.py中修改数据库连接地址  


python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
##启动##  
python manage.py runserver 0.0.0.0:8001  
