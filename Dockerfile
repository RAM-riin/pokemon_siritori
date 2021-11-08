# python3.8をインストールしたOS
FROM python:3.8

WORKDIR /app

RUN pip install -U pip

RUN pip install streamlit

RUN pip install pandas

ENTRYPOINT [ "streamlit", "run", "app.py" ]