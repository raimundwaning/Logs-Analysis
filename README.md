# Logs-Analysis
This python program is my solution for the project LogAnalysis of the FullStack Web Developer Nanodegree @Udacity
The python file can be found in this repo at: Logs-Analysis/vagrant/LogsAnalysis/LogsAnalysis.py.

It uses basic python code to connect to a database and extract some data from it with SQL-queries. The database contains the three tables "articles", "authors" and "log" which represents the data a fictional news website stores. In the table "log", requests from visitors are stored, including the http-status, path (which directs to the article, which also stores the author in the articles table), so we know which request was successful and how often which article was requested.
The queries answer the questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Usage
1. You need python installed on your computer to run this program. You can get Python v3 here: https://www.python.org/downloads/
2. In order to run the virtual machine in which you can connect to the database, you need a virtual machine like https://www.virtualbox.org/ .
3. After that, you need a linux instance running in the virtual box. For this program, you need vagrant which you can get here: https://www.vagrantup.com/downloads.html
4. If running windows, get a bash, for example git-bash (https://gitforwindows.org/).
5. Save the vagrant folder on your hard drive. Navigate to the folder in the bash and perform the command "vagrant up" (this will take a while). After that, log into your linux vm using the command "vagrant ssh".
6. Now that you are in the vm, change to the vagrant folder using "cd \vagrant".
7. Now you should be able to run the program with "python LogsAnalysis.py" and then should see the result of the queries in the .py-file.
