FROM node:12.14.1

WORKDIR /com-word-app2/frontend
RUN npm install -g @vue/cli 
COPY  ./package*.json /com-word-app2/frontend/
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080