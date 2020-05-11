# 时间序列
# Pandas在对频率转换进行重新采样时拥有简单、强大且高效的功能（如将按秒采样的数据转换为按5分钟为单位进行采样的数据）。这种操作在金融领域非常常见。

import pandas as pd
import numpy as np

# rng = pd.date_range('1/1/2012',periods=100,freq='S')
# ts = pd.Series(np.random.randint(0,500,len(rng)),index=rng)
# print(ts.resample('5Min',how='sum'))

# 1. 时区表示
rng = pd.date_range('3/6/2012 00:00',periods=5,freq='D')
ts = pd.Series(np.random.randn(len(rng)),rng)
print(ts)

ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print('========================================')

# 2. 时区转换
print(ts_utc.tz_convert('US/Eastern'))
print('========================================')

# 3. 时间跨度转换
rng = pd.date_range('1/1/2012',periods=5,freq='M')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
print(ts)
print('----------------------------------------')
ps = ts.to_period()
print(ps)
print('----------------------------------------')

print(ps.to_timestamp())
print('========================================')

# 4. 时期和时间戳之间的转换使得可以使用一些方便的算术函数
# prng = pd.period_range('1990Q1','2000Q4',freq='Q-NOV')
# ts = pd.Series(np.random.randn(len(prng)),prng)
# ts.index(prng.asfreq('M','e') + 1).asfreq('H','s') + 9
# print(ts.head())
