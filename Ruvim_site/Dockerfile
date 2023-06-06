FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requrements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app/
EXPOSE 8000