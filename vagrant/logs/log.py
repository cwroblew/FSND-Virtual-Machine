import psycopg2
import os

DBNAME = "news"

def get_pop_three():
  """Return three most popular articles."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(title) as artcnt from sluglog, articles where status = '200 OK' and articles.slug = sluglog.slug group by title order by artcnt desc limit 3")
  articles = c.fetchall()
  db.close
  return articles

def get_pop_authors():
  """Return Most popular authors."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(" select name, count(name) as authcnt from sluglog, articles, authors where articles.slug = sluglog.slug and authors.id = author group by authors.name order by authcnt desc")
  articles = c.fetchall()
  db.close
  return articles

def get_1perc_error():
  """Return dates with an error greater than 1% of all requests."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  stmt = "select totdt, badcnt * 1.0 / count as errors " \
         "from dailylogcnt, badsrch " \
         "where srchbaddt = totdt and badcnt > count * 0.01 order by totdt limit 10"
  c.execute(stmt)
  articles = c.fetchall()
  db.close
  return articles

# Clear screen
clear = lambda: os.system('clear') #on Linux System
clear()

articles = get_pop_three()
print("{:40s} {:s}".format("Title", "Views"))
print("{:-<40} {:-<7}".format("", ""))
for article in articles:
    print ("{:40s} {:s}".format(article[0],str("{:,}".format(article[1]).rjust(7))))

print ("\n")
authors = get_pop_authors()
print("{:30s} {:s}".format("Author", "Views"))
print("{:-<30} {:-<7}".format("", ""))
for author in authors:
    print ("{:30s} {:s}".format(author[0],str("{:,}".format(author[1]).rjust(7))))

print ("\n")
errors = get_1perc_error()
print("{:30s} {:s}".format("Date", "Errors"))
print("{:-<30} {:-<6}".format("", ""))
for error in errors:
    print ("{:30s} {:.1%}".format(error[0].strftime("%B %d, %Y"), error[1]))

print ("\n")
