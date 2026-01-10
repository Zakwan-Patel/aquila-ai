FROM python:3.10-slim

WORKDIR /ui

COPY requirements-ui.txt .

RUN pip install --no-cache-dir -r requirements-ui.txt

COPY ui ui

EXPOSE 8501

CMD ["streamlit", "run", "ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
