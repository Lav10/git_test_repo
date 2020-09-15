import sys
from datetime import datetime

name = sys.argv[1]

with open('/home/airflow/test.txt','w+') as f:
    text = f.read()
    text=text+"\nHello "+str(name)+", the current date and time is "+str(datetime.now())+". And this is check the git code update.\n"
    f.write(text)