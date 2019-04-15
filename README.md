# Logs Analysis

This project work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.
Exploring a large database with over a million rows we building and refine complex queries and use them to draw business conclusions from data.

For this project three questions will be ansewred:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

## Getting Started
This project use a webserver with PostgreSQL and Python3. You can run this in a real server or in a virtual machine. If you need help to install and setup a virtual machine with VirtualBox and Vagrant, check the reference link bellow on Resources.


### Prerequisites
* [Python3](https://www.python.org/ "Python Homepage")
* [PostgreSQL](https://www.postgresql.org/ "PostgreSQL Homepage")
* [Web Server](https://en.wikipedia.org/wiki/Web_server/ "Wikipedia article about Web Servers")

### Installing and Running
1. Clone this git repositoriy:
    ```
      $ git clone https://github.com/psaviott/Logs-Analysis.git'
    ```
2. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "download newsdata.sql") the newsdata file.

3. Setup database

  * Create a database named news
    ```psql
      user=> CREATE DATABASE news;
    ```
  * Load newsdata.sql into local database:
    ```
      $ psql -d news -f newsdata.sql
    ```
4. Runnig the program with:
  ```python
    $ python3 log-analysis.py
  ```
  you can see a return like [this:](/results.txt)

## Built With

* [Python3](https://docs.python.org/ "Python3 documentation") Programming Language
* [PostgreSQL](https://www.postgresql.org "PostgreSQL documentation") Relational Database

## Authors

* Philipe Saviott - [psaviott](https://github.com/psaviott)

## Acknowledgments
* [PostgreSQL](https://www.postgresql.org/docs/10/index.html "PostgreSQL documentation") documentation
* [Python3](https://docs.python.org/3.6/index.html "Python3 documentation") documentation
* [VirtualBox and Vagrant](https://www.taniarascia.com/what-are-vagrant-and-virtualbox-and-how-do-i-use-them/ "How to use Vagrant and VirtualBox") by Tania Rascia
