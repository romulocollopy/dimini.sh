FROM python:3-slim as base

ARG USER_NAME=app
ARG HOME_DIR=/home/${USER_NAME}/
ARG APP_DIR=/app/
ARG SECRET_KEY=SUPERSECRET
ARG VIRTUAL_ENV=${HOME_DIR}.venv/

ENV SECRET_KEY=${SECRET_KEY}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="${VIRTUAL_ENV}bin:$PATH"

RUN apt-get update \
  && apt-get install gcc git -y \
  && apt-get clean

RUN useradd -m -d ${HOME_DIR} ${USER_NAME} -u 1001
RUN mkdir -p ${APP_DIR} \
  && chown ${USER_NAME} -R ${APP_DIR}

USER ${USER_NAME}

RUN python -m venv ${VIRTUAL_ENV} \
  && ${VIRTUAL_ENV}bin/pip install --upgrade pip poetry \
  && poetry config virtualenvs.in-project true

WORKDIR ${APP_DIR}

COPY settings.example.ini ${APP_DIR}settings.ini
COPY pyproject.toml ${APP_DIR}

RUN poetry install


FROM python:3-slim as production

ARG USER_NAME=app
ARG HOME_DIR=/home/${USER_NAME}/
ARG APP_DIR=/app/
ARG SECRET_KEY=SUPERSECRET
ARG VIRTUAL_ENV=${HOME_DIR}.venv/

ENV SECRET_KEY=${SECRET_KEY}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -m -d ${HOME_DIR} ${USER_NAME} -u 1001
RUN mkdir -p ${APP_DIR}
RUN chown ${USER_NAME} -R ${APP_DIR}

USER ${USER_NAME}

ENV PATH="${VIRTUAL_ENV}bin:$PATH"

WORKDIR ${APP_DIR}

COPY --from=base ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=base $APP_DIR $APP_DIR
COPY . ${APP_DIR}

RUN poetry shell

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
