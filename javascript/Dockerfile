FROM bitnami/apache:latest

USER root

ARG http_proxy
ARG https_proxy
ARG no_proxy

RUN export http_proxy=$http_proxy \
  && export https_proxy=$https_proxy \
  && export no_proxy=$no_proxy

EXPOSE 80
EXPOSE 443
