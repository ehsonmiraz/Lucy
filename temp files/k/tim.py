import time,timestamp
from datetime import datetime
a=timestamp(datetime.now())
time.sleep(10)
b=timestamp(datetime.now())
rs=(b-a)*6*120
print(rs)
