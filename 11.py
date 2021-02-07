
import jsonpath
aa={"currentPage":1,"pageSize":10,"paramMap":{"includeDelete":true}}
bb = jsonpath.jsonpath(aa,$.currentPage)
