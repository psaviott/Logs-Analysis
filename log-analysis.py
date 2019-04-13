#! /usr/bin/env python3

import psycopg2


# Query 1: What are the three most popular articles of all time?
query1 = """select title, count(path)
            from articles
            inner join log on ('/article/' || articles.slug = log.path)
            group by articles.title
            order by count desc
            fetch first 3 row only;"""


# Query 2: Who are the most popular article authors of all time?
query2 = """select name, count(path)
            from authors, log
            inner join articles on ('/article/' || articles.slug = log.path)
            where authors.id = articles.author
            group by authors.name
            order by count desc;"""

# Query 3: On which day did more than 1% of requests lead to errors?
query3 = """select date(time),
                    cast((count(log.status)*100.0)/num as decimal(6,1)) as x
            from log, (select date(time), count(status) as num
                from log
                group by date(time)) as perc
            where date(time) = date
            and log.status = '404 NOT FOUND'
            group by date(time), num
            having count(log.status) > num/100
            order by x desc;"""


# Open and close the connection
def do_query(query):
    data = psycopg2.connect(database="news")
    consult = data.cursor()
    consult.execute(query)
    qresult = consult.fetchall()
    data.close()
    return qresult


# Print report
def print_querys():

    # Print top articles
    articles = do_query(query1)
    print("\n\t Top articles of all time \n")
    for title, count in articles:
        print(title, "-", count, "views")

    # Print top authors
    authors = do_query(query2)
    print("\n\t Top authors of all time \n")
    for name, count in authors:
        print(name, "-", count, "views")

    # Print high error day
    errors = do_query(query3)
    print("\n\t Days with more than ""1%"" of bad requests \n")
    for date, x in errors:
        print(date, "-", x, """% errors""" "\n")


if __name__ == '__main__':
    print_querys()
