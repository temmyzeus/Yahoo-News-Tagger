FROM conda/miniconda3

WORKDIR /usr/yahoo_news

RUN apt-get update -y && apt-get upgrade -y

COPY . .

RUN pip install jupyterlab notebook numpy pandas scikit-learn gensim hydra-core

RUN [ "python", "--version" ]

ENTRYPOINT [ "jupyter", "lab" ]

CMD [ "--port=8889" ]