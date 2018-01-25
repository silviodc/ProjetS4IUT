ARG http_proxy
ARG https_proxy
ARG no_proxy

FROM jupyter/base-notebook:417e06bfc446

RUN echo $http_proxy

RUN export http_proxy=$http_proxy \
  && export https_proxy=$https_proxy \
  && export no_proxy=$no_proxy

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        unzip \
        libxml2-dev \
        libxslt-dev \
		    libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && chown 1000 -R /home/jovyan/work

USER jovyan

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8888

WORKDIR /home/jovyan/work

CMD ["start-notebook.sh", "--NotebookApp.token=''"]
