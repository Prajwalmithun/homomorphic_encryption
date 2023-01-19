FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["python3", "cat_lovers_VS_dog_lovers.py"]