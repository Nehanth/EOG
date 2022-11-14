FROM python:3.7

ADD * /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && pip install arrow && pip install pyarrow


CMD [ "python", "./main.py" ]
CMD ["streamlit", "./main.py"]
