import datetime
import sys
if(len(sys.argv) != 3):
	print("用法：datatime 2020-1-1 32，意思是2020年1月1日后的32天")
in_date = sys.argv[1]
offset = int(sys.argv[2])
dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
out_date = (dt + datetime.timedelta(days=offset)).strftime("%Y-%m-%d")
print(out_date)
