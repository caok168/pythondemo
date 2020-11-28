

# 2020-11-01T16:00:00.000Z
from datetime import datetime
import time

import pytz


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%S.%fZ'):
    local_tz = pytz.timezone('Asia/Shanghai')
    local_format = "%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return datetime.fromtimestamp(int(time.mktime(time.strptime(time_str, local_format))))


if __name__ == '__main__':
    res = utc_to_local('2020-11-01T16:00:00.000Z')
    print(res)
