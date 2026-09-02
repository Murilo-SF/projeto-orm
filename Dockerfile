FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./Projeto_ORM

CMD ["python","-m","Projeto_ORM.app"]