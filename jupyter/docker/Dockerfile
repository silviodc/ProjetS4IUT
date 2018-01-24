FROM jupyter/base-notebook:417e06bfc446

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        unzip \
        libxml2-dev \
        libxslt-dev \
		    libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER jovyan

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["start-notebook.sh", "--NotebookApp.token=''"]
