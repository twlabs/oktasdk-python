FROM node:6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
COPY package.json /usr/src/app/
COPY requirements.txt /usr/src/app/
RUN npm install && npm cache clean
RUN pip install -r requirements.txt
COPY . /usr/src/app
