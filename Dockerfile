FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
ENV ATLAS_URI="mongodb+srv://angularmoneygroup:5139bpOk9VR1GeI7@ingressosaqui.t49bdes.mongodb.net/ingressosAqui?retryWrites=true&w=majority"
ENV DB_NAME="ingressosAqui"
CMD ["python", "main.py"]
