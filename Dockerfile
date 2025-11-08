FROM python:3.11

WORKDIR /test
RUN pip install --no-cache-dir uv
RUN uv venv
COPY ./requirements.txt ./requirements.txt
RUN uv pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]