FROM python:3.12.8-slim-bookworm

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install poetry

COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY src/ ./src/

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]