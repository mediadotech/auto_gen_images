FROM python:3.9

WORKDIR /code

COPY . .
COPY ./templates/ticket.svg .
COPY ./templates/fonts /usr/share/fonts/

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# templates/fonts配下のフォントを然るべき所にコピー
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
