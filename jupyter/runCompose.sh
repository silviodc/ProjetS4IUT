#!/bin/bash
export http_proxy=http://proxy.iut-orsay.fr:3128
export https_proxy=https://proxy.iut-orsay.fr:3128
export no_proxy=localhost,127.0.0.1
docker-compose up
