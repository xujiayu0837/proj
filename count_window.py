import os
import datetime
import pandas as pd
from tqdm import tqdm
import numpy as np
from sklearn.cluster import KMeans

SRC_DIR = '/Users/xujiayu/毕设/data/user_data'
DEST_DIR = '/Users/xujiayu/毕设/data/count_period'

# 提取某个用户某段时间(以7点到9点为例, 或者11点到13点, 或者17点到19点)的数据, 按时间切片(时间窗口长度以5分钟或者10分钟为例)聚类, 特征为次数
def main(filename, k, start_hour='07', end_hour='09'):
	try:
		minutes_df = pd.read_csv(os.path.join(SRC_DIR, filename), sep='|')
		minutes_df['user_mac_addr'] = minutes_df['user_mac_addr'].astype(str)
		minutes_df['hour'] = minutes_df['minutes'].astype(str).str.slice(8, 10)
		minutes_df = minutes_df[(minutes_df['hour'] >= start_hour) & (minutes_df['hour'] <= end_hour)]
		minutes_df = minutes_df.drop('hour', axis=1)
		minutes_df['dt'] = pd.to_datetime(minutes_df['minutes'], format="%Y%m%d%H%M") + datetime.timedelta(hours=-8)
		minutes_df = minutes_df.drop('minutes', axis=1)
		minutes_df['ts'] = minutes_df['dt'].astype(int) // 10 ** 9
		minutes_df = minutes_df.drop('dt', axis=1)
		minutes_df['5_minutes'] = (minutes_df['ts'] / 60 / 5).astype(int)
		minutes_df = minutes_df.drop('ts', axis=1)
		pivot_df = pd.pivot_table(minutes_df, values='rss', index=['user_mac_addr', '5_minutes'], columns='AP', aggfunc=len, fill_value=0)
		if k == 0:
			print(len(pivot_df.columns))
			label = KMeans(n_clusters=len(pivot_df.columns), random_state=1993).fit_predict(pivot_df)
		else:
			label = KMeans(n_clusters=k, random_state=1993).fit_predict(pivot_df)
		pivot_df['label'] = label
		dest_filename = '%s-%s_%s-k%s.csv' % (filename.split(".")[0], start_hour, end_hour, str(k))
		pivot_df.to_csv(os.path.join(DEST_DIR, dest_filename), index=False)
	except Exception as e:
		print("main error: %s" % e)

if __name__ == '__main__':
	try:
		main('000000000000.csv', k=0, start_hour='11', end_hour='13')
	except Exception as e:
		raise e