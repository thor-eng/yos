FROM python:3.11-slim
WORKDIR /app
COPY . /app 
RUN pip install --upgrade pip
RUN pip install Flask==2.3.2
EXPOSE 5000
ENV key=app.py
ENV RUN=0.0.0.0
CMD ["flask","run"]

