#select title, artcnt
# from (select replace(path, '/article/', '') as slug,
#              count(path) as artcnt
#         from log
#        where path like '/article/%' and status = '200 OK'
#        group by path) as subqry,
#      articles
# where articles.slug = subqry.slug
# order by artcnt desc
# limit 3;
#
#  create view sluglog as
# select replace(path, '/article/', '') as slug, status, method, "time", id
# from log where path like '/article/%'
#
# select title, count(title) as artcnt from sluglog, articles
# where status = '200 OK' and articles.slug = sluglog.slug
# group by title order by artcnt desc limit 3;

import psycopg2

DBNAME = "news"

def get_pop_three():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(title) as artcnt from sluglog, articles where status = '200 OK' and articles.slug = sluglog.slug group by title order by artcnt desc limit 3")
  articles = c.fetchall()
  db.close
  return articles
