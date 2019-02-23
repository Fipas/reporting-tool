# Project 3 - Log Analysis

Log Analysis is a python script created to generate reports about a news database.\
The script was designed as part of the Udacity Web Full Stack Nanodegree.

# Getting Started

To be able to run the script, Python 2.7.15 and PostgreSQL 9.5.14 are required. \
For more information about how to install Python, please visit https://www.python.org/about/gettingstarted/ \
If you need help installing PostgreSQL, please go to https://www.postgresql.org/download/

# Populating the database

All queries are executed in a database called **news**. \
Before running the script, ensure the database is created, populated and running. \
To create the database and populate it with data:

1. Download ``news_data.sql`` from the link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Use ``news_data.sql`` to create and load the database with ``psql -d news -f newsdata.sql``

For more information about table structure, please read ``news_data.sql`` or use interactive commands from ``psql`` cli 

# Usage

To run the script, from the root directory execute
```
python reporting_tool.py
```
An output example is available in file ``output_example.txt``

# Running from a Virtual Machine

If you want to run the script using a virtual machine, we supply one with Python and PostgreSQL already installed. \
Ensure that you have VirtualBox 5.1 and the latest version of Vagrant installed. \
If you need help installing VirtualBox 5.1, visit https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 \
To install Vagrant, visit https://www.vagrantup.com/downloads.html

You can download an already prepared virtual machine from \
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

To set it up, unzip it, navigate to the directory called **vagrant** and run ``vagrant up``\
After it finishes setting up, use ``vagrant ssh`` to access the virtual machine \
All files inside the **vagrant** folder of the host machine show up inside the **/vagrant** in the guest, so put the \
script and sql files in this folder and refer to previous sections on how to populate the database and use the tool.


# Authors
* Udacity Team
* Felipe Freitas Fonseca

# License

This project is licensed under the MIT License. For more information about it, please visit https://opensource.org/licenses/MIT
