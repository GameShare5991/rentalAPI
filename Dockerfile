FROM python:3
WORKDIR /app
ADD rentalapi.py .
ADD serviceAccountKey.json .
RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
RUN pip install flask
RUN pip install firebase
RUN pip install firebase_admin
RUN pip install flask_cors
EXPOSE 3005
CMD ["python", "rentalapi.py"]
