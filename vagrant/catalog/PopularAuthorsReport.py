#select name, sum(artcnt) as authcnt
# from
#      (select replace(path, '/article/', '') as slug, count(path) as artcnt
#         from log where path like '/article/%' and status = '200 OK'
#         group by path) as subqry,
#       articles, authors
# where articles.slug = subqry.slug
# and authors.id = author
# group by authors.name
# order by authcnt desc;
#
#  select name, count(name) as authcnt
# from sluglog, articles, authors
# where articles.slug = sluglog.slug
# and authors.id = author
# group by authors.name
# order by authcnt desc

import psycopg2

DBNAME = "news"

def get_pop_authors():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(" select name, count(name) as authcnt from sluglog, articles, authors where articles.slug = sluglog.slug and authors.id = author group by authors.name order by authcnt desc")
  articles = c.fetchall()
  db.close
  return articles
