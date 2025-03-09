ARG PYTHON_VERSION=3.13
# Base Stage
FROM python:$PYTHON_VERSION-slim AS base

RUN apt-get update && apt-get install -y -qq \
        build-essential \
        curl \
        libcurl4-openssl-dev \
        python3-dev \
        libpq-dev \
        libssl-dev \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
	&& rm -rf /var/lib/apt/lists/*


# Poetry Setup
ENV POETRY_VERSION=2.1.1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR /opt/text-processing-fast-api

COPY pyproject.toml poetry.lock ./
COPY src/ src/


ENV PYTHONPATH="$PYTHONPATH:/opt/text-processing-fast-api/src:/opt/text-processing-fast-api/config"
ENV LANG=pt_BR.UTF-8

# Development Stage
FROM base AS dev-image

WORKDIR /opt/text-processing-fast-api

# Install all dependencies
RUN poetry install --no-root

COPY --from=base /opt/text-processing-fast-api /opt/text-processing-fast-api
COPY tests/ tests/

EXPOSE 8000
CMD ["uvicorn", "--factory", "main:start_fast_api", "--host",  "0.0.0.0", "--port", "8000"]