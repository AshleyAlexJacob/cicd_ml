FROM python:3.10.13 as build
WORKDIR /app

# copy files
COPY ./models/ ./models/
COPY ./model_v1.0.pkl ./model_v1.0.pkl
COPY ./prediction.py ./prediction.py
COPY ./requirements.txt ./requirements.txt

ENV VIRTUAL_ENV=/home/packages/.venv
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 777 /install.sh && /install.sh && rm /install.sh

RUN /root/.cargo/bin/uv venv /home/packages/.venv

RUN /root/.cargo/bin/uv pip install --no-cache --system  -r requirements.txt
# run local
CMD ["python", "prediction.py"]