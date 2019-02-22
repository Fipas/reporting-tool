#!/usr/bin/python2
# -*- coding: utf-8 -*-
# A reporting tool for a news database

import datetime
import psycopg2

DBNAME = 'news'


def get_top_three_articles():
    """Return the most popular three articles of all time from database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as views from articles, log \
            where log.path like '%' || articles.slug || '%' \
            group by title order by views desc limit 3")
    artciles = c.fetchall()
    db.close()

    return artciles


def get_most_popular_authors():
    """Return the most popular three articles of all time from database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as views from authors, articles, log \
            where log.path like '%' || articles.slug || '%' and \
            authors.id = articles.author group by name order by views desc")
    authors = c.fetchall()
    db.close()

    return authors


def get_days_with_many_errors():
    """Return the most popular three articles of all time from database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select subq1.day, \
            (subq2.errors / subq1.requests) * 100 as p_errors from \
            (select date(time) as day, cast(count(status) as float) \
            as requests from log group by day) as subq1, \
            (select date(time) as day, cast(count(status) as float) as errors \
            from log where status != '200 OK' group by day) as subq2 \
            where subq1.day = subq2.day and \
            (subq2.errors / subq1.requests) * 100 > 1 order by subq1.day")
    days = c.fetchall()
    db.close()

    return days


print "What are the most popular three articles of all time?\n"
articles = get_top_three_articles()
for article in articles:
    print "{} — {} views".format(article[0], article[1])

print "\n\nWho are the most popular article authors of all time?\n"
authors = get_most_popular_authors()
for author in authors:
    print "{} — {} views".format(author[0], author[1])

print "\n\nOn which days did more than 1% of requests lead to errors?\n"
days = get_days_with_many_errors()
for day in days:
    print "{} — {:.2f}% errors".format(day[0], day[1])
