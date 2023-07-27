# hash:sha256:5289ca8a08011a25010aef9a6663e5f6ac5cb20e0126047c6f45f567b1b13958
FROM registry.acmecorp-cfn-demo.codeocean.com/codeocean/jupyterlab:3.0.9-miniconda4.9.2-python3.8-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip install -U --no-cache-dir \
    pandas==2.0.2 \
    redshift-connector==2.0.911
