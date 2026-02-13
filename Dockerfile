FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

# Install project dependencies from pyproject.toml
RUN pip install .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
