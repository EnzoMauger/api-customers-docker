#Dernière version de python (Au moins 3.10, support natif des types)
FROM python:latest

WORKDIR /code

#RUN ["apt", "update"]
#RUN ["apt", "install", "libmariadb3", "-y"]

#Installation des librairies nécessaires
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

#Lancement de l'api via l'utilitaire adapté (voir doc FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

MAINTAINER Enzo Mauger
