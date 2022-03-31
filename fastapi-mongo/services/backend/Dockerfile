FROM python:3.9

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=$PWD

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install requests
COPY src/ .
CMD ["python", "src/app/main.py"]

