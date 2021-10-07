# FROM pypi/cairosvg

# WORKDIR /code


# # RUN apt update && apt install freetype2-demos && apt install fonts-noto-cjk
# COPY ./requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
# COPY ./template /code/template

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]

FROM python:3.9

# install
# COPY poetry.lock pyproject.toml ./
# RUN pip install poetry
# RUN poetry config virtualenvs.create false \
#   && poetry install --no-dev

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./templates /code/templates

# templates/fonts配下のフォントを然るべき所にコピー
COPY templates/fonts /usr/share/fonts/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
