from datetime import datetime

	# 현재 : 2021-01-09 21:30:12.050111
date_to_compare1 = datetime.strptime("20221125", "%Y%m%d")
date_to_compare = datetime.strptime("20201225", "%Y%m%d")

date_diff = date_to_compare1 - date_to_compare
print("차이 :", date_diff)	