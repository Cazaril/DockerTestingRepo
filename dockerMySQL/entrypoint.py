#!/usr/bin/env python
from sh import mysql

text = ""
with open("./sql_schema.sql") as f:
    text = f.read()

mysql("-u", "root", "-ptoor", "-e", text)
