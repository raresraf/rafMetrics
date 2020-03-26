FROM mysql:5.6 as builder

RUN ["sed", "-i", "s/exec \"$@\"/echo \"not running $@\"/", "/usr/local/bin/docker-entrypoint.sh"]

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=WebMonitoring

COPY mysql_config/init.sql /docker-entrypoint-initdb.d/

RUN ["/usr/local/bin/docker-entrypoint.sh", "mysqld", "--datadir", "/initialized-db"]

FROM mysql:5.6
COPY --from=builder /initialized-db /var/lib/mysql

