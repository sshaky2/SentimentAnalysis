FROM python:3.5-onbuild

EXPOSE 5000

CMD gunicorn sentiment:app --log-file - --bind 0.0.0.0:5000