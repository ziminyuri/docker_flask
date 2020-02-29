FROM python:3.7-slim

COPY . .

RUN pip install flask

ENV name="HelloWorld"
ENV hostname="c57429694d84"