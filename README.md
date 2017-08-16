# LogsAnalysis

[Movie Trailer Website](https://github.com/jjsuper/LogsAnalysis) 
is the solution of Logs Analysis project in Udacity.

# Overview
Create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

# Quickstart
#### Command Line

```
psql -d news -f newsdata.sql
python2 newsdb.py
```

#### Report

This tool saves the report in ```./answers.txt``` .

#### Database Views

This tool relies on views created in the database. 
However, views are created inside python code. 
They are deleted in the end of python code.
Users do not need to recreate them.
<\br>
Here are ```create view``` the statements.



