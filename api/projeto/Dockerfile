FROM ubuntu:18.04

RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get update --fix-missing -y

RUN apt-get install --fix-missing -y \
    python3 \
    python3-pip \
    python3-setuptools \
    libsm6 \
    libxext6 \
    libfontconfig1 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/* && \
    apt-get purge --auto-remove && \
    apt-get clean


COPY requirements.txt /code
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . projeto

RUN chmod -R +x /code

# RUN APPLICATION
EXPOSE 5000
CMD ["gunicorn", "-c", "projeto/settings.py", "--workers=1", "--worker-class=uvicorn.workers.UvicornWorker", "projeto:app"]
