FROM python:3.9

EXPOSE 80

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


CMD ["uvicorn", "app.core.app:app", "--host", "0.0.0.0", "--port", "80"]