FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python main.py --set-broker mosquitto 1883

CMD ["python", "main.py", "--no-gui"]