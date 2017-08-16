#!/usr/bin/env python2
# Database code for the DB news.

import psycopg2
import time

DBNAME = "news"
outfile = open("answers.txt", "w")

# Create views
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('''
create view alog as
select substring(path from 10) as slug, id
from log
where path like '/article/%';
''')
c.execute('''
create view dailyErrorLog as
select time::date as date, count(*) as error
from log
where status NOT Like '%OK'
group by date;
''')
c.execute('''
create view dailyLog as
select time::date as date, count(*) as total
from log group
by date;
''')
db.commit()
db.close()


# Query for question 1
def get_popular_articles():
    """Return the most popular three articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
    select articles.title, count(*) as count
    from articles, alog
    where alog.slug = articles.slug
    group by articles.title
    order by count desc
    limit 3;
    ''')
    return c.fetchall()
    db.close()


# Query for question 2
def get_popular_authors():
    """Return the most popular article authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
    select authors.name, count(*) as count
    from authors, articles, alog
    where authors.id = articles.author and articles.slug = alog.slug
    group by authors.name
    order by count desc;
    ''')
    return c.fetchall()
    db.close()


# Query for question 3
def get_error_date():
    """Return the days on which more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
    select dailyLog.date, dailyErrorLog.error::float/dailyLog.total
    as ratio from dailyErrorLog, dailyLog
    where dailyErrorLog.date = dailyLog.date
    and dailyErrorLog.error::float/dailyLog.total > 0.01;
    ''')
    db.commit()
    return c.fetchall()
    db.close()

# Post-Processing
outfile.write("Solution 1.\n")
for title, count in get_popular_articles():
    outfile.write('''"%s" -- %s views\n''' % (title, count))

outfile.write("Solution 2.\n")
for name, count in get_popular_authors():
    outfile.write('''%s -- %s views\n''' % (name, count))

outfile.write("Solution 3.\n")
for date, ratio in get_error_date():
    t = date.strftime("%b %d %Y")
    outfile.write('''%s -- %.1f%% errors\n''' % (t, ratio*100))

# Delete views
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("drop view alog")
c.execute("drop view dailyLog")
c.execute("drop view dailyErrorLog")
db.commit()
db.close()

outfile.close()
