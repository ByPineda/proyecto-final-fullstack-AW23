FROM mysql:latest
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password
ENV MYSQL_ROOT_PASSWORD=password
COPY ./data.sql /docker-entrypoint-initdb.d/data.sql
