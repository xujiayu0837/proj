import os
from multiprocessing import Pool
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from constants import AP_LOC_DICT

SRC_DIR = '/Users/xujiayu/毕设/data/hours_window_process'
DEST_DIR = '/Users/xujiayu/毕设/data/AP_cnt'
K = 2

# 单个AP每小时流量聚类
def main(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		dest_path = os.path.join(dest, 'AP_cnt-k%s.csv' % str(K))
		concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
		data = pd.concat(concat_list, ignore_index=True)
		data['hours'] = data['hours'].astype(str)
		data['date'] = data['hours'].str.slice(0, 8)
		data['hour'] = data['hours'].str.slice(8, 10)
		pivot_df = pd.pivot_table(data, values='rss', index='date', columns='hour', aggfunc=len, fill_value=0)
		label = KMeans(n_clusters=K, random_state=1993).fit_predict(pivot_df)
		pivot_df['label'] = label
		pivot_df.to_csv(dest_path, index=False)
	except Exception as e:
		print("main error: %s" % e)

def aux():
	try:
		dir = '/Users/xujiayu/毕设/data/hours_window_process/14E4E6E173FE'
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		dest_path = os.path.join(dest, 'AP_cnt-k%s.csv' % str(K))
		concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
		data = pd.concat(concat_list, ignore_index=True)
		data['hours'] = data['hours'].astype(str)
		data['date'] = data['hours'].str.slice(0, 8)
		data['hour'] = data['hours'].str.slice(8, 10)
		pivot_df = pd.pivot_table(data, values='rss', index='date', columns='hour', aggfunc=len, fill_value=0)
		label = KMeans(n_clusters=K, random_state=1993).fit_predict(pivot_df)
		pivot_df['label'] = label
		pivot_df.to_csv(dest_path, index=False)
	except Exception as e:
		print("aux error: %s" % e)

if __name__ == '__main__':
	try:
		dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		pool = Pool(4)
		pool.map(main, dir_list)
		pool.close()
		pool.join()
		# aux()
	except Exception as e:
		raise e