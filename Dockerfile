FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python3.7 RandomForest_Model.py
RUN python3.7 CNN_Model.py
RUN pip freeze 
CMD gunicorn -w 2 app:app -b 0.0.0.0:80