#!/usr/bin/python2
# -*- coding: utf-8 -*-
# A reporting tool for a news database

import datetime
import psycopg2

DBNAME = 'news'


class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls):
        if cls.connection is None:
            try:
                cls.connection = psycopg2.connect(database=DBNAME)
            except psycopg2.Error as e:
                print "Unable to connect to the database"
                print e.pgerror
                print e.diag.message_detail

        return cls.connection

    @classmethod
    def close_connection(cls):
        if cls.connection is not None:
            cls.connection.close()
            cls.connection = None


def get_top_three_articles():
    """Return the most popular three articles of all time from database"""
    db = DBConnection.get_connection()
    c = db.cursor()
    c.execute("select title, count(*) as views from articles, log \
            where log.path like '%' || articles.slug || '%' and \
            log.status = '200 OK' \
            group by title order by views desc limit 3")
    artciles = c.fetchall()

    return artciles


def get_most_popular_authors():
    """Return the most popular three articles of all time from database"""
    db = DBConnection.get_connection()
    c = db.cursor()
    c.execute("select name, count(*) as views from authors, articles, log \
            where log.path like '%' || articles.slug || '%' and \
            authors.id = articles.author and \
            log.status = '200 OK' \
            group by name order by views desc")
    authors = c.fetchall()

    return authors


def get_days_with_many_errors():
    """Return the most popular three articles of all time from database"""
    db = DBConnection.get_connection()
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

DBConnection.close_connection()
