#!/bin/bash

# MySQL server credentials
MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"

# List all databases
databases=$(mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema|mysql)")
