# hash:sha256:0c0f6b3e6baf5ccbdd4b63ed98172ccb9dd31e809b57320ff02143fdb125a237
FROM registry.acmecorp-cfn-demo.codeocean.com/codeocean/mambaforge3:22.11.1-4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN mamba install -y \
        fastparquet==2023.7.0 \
        jupyterlab==3.6.0 \
    && mamba clean -ya

RUN pip install -U --no-cache-dir \
    pandas==2.0.2 \
    redshift-connector==2.0.911
