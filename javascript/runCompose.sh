#!/bin/bash
export http_proxy=http://username:password@proxy.com:port
export https_proxy=http://username:password@proxy.com:port
export no_proxy=localhost,127.0.0.1,company.com
docker-compose up
