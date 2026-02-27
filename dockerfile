FROM python:3.11-slim
WORKDIR /myprog
RUN pip install googletrans==3.1.0a0
ADD . .
CMD [ "python", "Lab_2.py" ]
