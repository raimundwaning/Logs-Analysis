#!/usr/bin/env python3

# logs analysis project, udacity fswd nd
import psycopg2

DBNAME = "news"

# establishing db connection and initializing cursor
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
# 1. What are the most popular three articles of all time?
c.execute(
    "WITH popular_articles AS (SELECT path, count(*) AS popularity "
    "FROM log WHERE status LIKE '%200%' AND path <> '/' GROUP BY path "
    "ORDER BY popularity desc limit 3)"
    "SELECT title, popularity FROM articles, popular_articles "
    "WHERE popular_articles.path LIKE CONCAT('%', articles.slug, '%');")
firstresult = c.fetchall()
print('\nThe most popular articles are:')
for i in range(0, len(firstresult)):
    print "\"" + firstresult[i][0] + "\" with " + str(firstresult[i][1])
    + " views"

# 2. Who are the most popular article authors of all time?
c.execute(
    "WITH popular_articles AS (SELECT path, count(*) AS popularity "
    "FROM log WHERE status LIKE '%200%' AND path <> '/' GROUP BY path ),"
    "popular_authors AS (SELECT author, popularity "
    "FROM articles,popular_articles "
    "WHERE popular_articles.path LIKE CONCAT('%', articles.slug, '%')) "
    "SELECT authors.name, SUM(popularity) AS popularity "
    "FROM authors, popular_authors "
    "WHERE popular_authors.author = authors.id "
    "GROUP BY authors.name ORDER BY popularity DESC LIMIT 10;")
secondresult = c.fetchall()
print('\nThe most popular article authors of all time are: ')
for i in range(0, len(secondresult)):
    print "\"" + secondresult[i][0] + "\" with " + str(secondresult[i][1]) +
    " views"

# 3. On which days did more than 1% of requests lead to errors?
c.execute(
    "WITH errors_per_day AS (SELECT date_trunc('day', log.time) AS day, "
    "count(*) AS errors "
    "FROM log WHERE status NOT LIKE '%200%' GROUP BY day),"
    "total_requests AS (SELECT date_trunc('day', log.time) AS day, "
    "COUNT(*) AS requests FROM log GROUP BY day) "
    "SELECT total_requests.day::date AS day, "
    "(CAST (errors_per_day.errors as FLOAT) / "
    "CAST(total_requests.requests as FLOAT)) AS error_percentage "
    "FROM errors_per_day, total_requests "
    "WHERE errors_per_day.day = total_requests.day AND "
    "(CAST (errors_per_day.errors as FLOAT) / "
    "CAST(total_requests.requests as FLOAT)) > 0.01 "
    "ORDER BY error_percentage desc;")
thirdresult = c. fetchall()
print('\nMore than 1% of requests lead to errors on these day(s): ')
for i in range(0, len(thirdresult)):
    print "\"" + str(thirdresult[i][0]) + "\" with " +
    str(thirdresult[i][1]*100) + " percent erroneous requests"
