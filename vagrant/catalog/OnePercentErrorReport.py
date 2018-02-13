#select date_trunc('day', time) as srchdt, badsrch.badcnt, goodsrch.goodcnt
# from log,
#      (select date_trunc('day', time) as srchbaddt, count(status) as badcnt
#         from log where status != '200 OK' group by srchbaddt) as badsrch,
#      (select date_trunc('day', time) as srchgooddt, count(status) as goodcnt
#         from log where status = '200 OK' group by srchgooddt) as goodsrch
# where badsrch.badcnt > goodsrch.goodcnt*.01
# group by srchdt, badsrch.badcnt, goodsrch.goodcnt
# order by srchdt
# limit 10