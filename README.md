# LogsAnalysis

[Movie Trailer Website](https://github.com/jjsuper/LogsAnalysis) 
is the solution of Logs Analysis project in Udacity.

# Overview
Create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

# Quickstart

#### Download data
[Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
Need to unzip this file after downloading it. 

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
<br />
Here are ```create view``` the statements.

```
create view alog as
select substring(path from 10) as slug, id
from log
where path like '/article/%';
```

```
create view dailyErrorLog as
select time::date as date, count(*) as error
from log
where status NOT Like '%OK'
group by date;
```

```
create view dailyLog as
select time::date as date, count(*) as total
from log group
by date;
```



