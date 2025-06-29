FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
COPY weather_wardrobe ./weather_wardrobe

RUN poetry config virtualenvs.create false \
 && poetry install --without dev --no-root

EXPOSE 5000
CMD ["python", "-m", "weather_wardrobe.main"]

