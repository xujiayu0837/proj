import os
from multiprocessing import Pool
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from constants import AP_LOC_DICT

SRC_DIR = '/Users/xujiayu/毕设/data-180908/hours_window'
# DEST_DIR = '/Users/xujiayu/毕设/data-180908/AP_cnt'
DEST_DIR = '/Users/xujiayu/毕设/data-180908/AP_cnt_day_sum'
# SRC_DIR = '/Users/xujiayu/毕设/data/hours_window_process'
# DEST_DIR = '/Users/xujiayu/毕设/data/AP_cnt'
K = 3
AP_LIST = ['14E4E6E18658', '14E4E6E1867A', '14E4E6E186A4', '14E6E4E1C510', '388345A236BE', '5C63BFD90AE2', 'EC172FE3B340']

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
		pivot_df.columns = ['_'.join(['hour', hour]) for hour in pivot_df.columns.values]
		pivot_df['label'] = label
		# engine = create_engine('mysql+mysqldb://root:root@localhost:3306/django_tutorial')
		# pivot_df.to_sql('polls_loc_%s' % AP.lower(), con=engine, if_exists='append', index=False)
		# pivot_df.to_csv(dest_path, index=False)
	except Exception as e:
		print("main error: %s" % e)

def count_by_AP():
	try:
		count_list = []
		subdir_list = []
		for sub_dir in os.listdir(SRC_DIR):
			if sub_dir.startswith('.'):
				continue
			subdir_list.append(sub_dir)
			dir = os.path.join(SRC_DIR, sub_dir)
			concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
			count_list.append(len(pd.concat(concat_list, ignore_index=True)))
		label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(count_list).reshape(-1, 1))
		AP_label_dict = dict(zip(subdir_list, label))
		print(AP_label_dict)
	except Exception as e:
		print("count_by_AP error: %s" % e)

def count_by_day():
	try:
		concat_list = []
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			if not os.path.isdir(dir):
				continue
			for filename in os.listdir(dir):
				concat_list.append(pd.read_csv(os.path.join(dir, filename), sep='|'))
		data = pd.concat(concat_list, ignore_index=True)
		data['date'] = data['hours'].astype(str).str.slice(0, 8)
		data = data.drop('hours', axis=1)
		day_df = data.groupby('date').size().reset_index(name='sum')
		clean_df = day_df[day_df['date'].astype(str).str.slice(0, 6) == '201710']
		label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(clean_df['sum']).reshape(-1, 1))
		clean_df['label'] = label
		clean_df.to_csv(os.path.join(DEST_DIR, 'AP_cnt_day_sum-201710-k%s.csv' % str(K)), index=False)
	except Exception as e:
		print("count_by_day error: %s" % e)

def aux():
	try:
		concat_list = []
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			if not os.path.isdir(dir):
				continue
			for filename in os.listdir(dir):
				concat_list.append(pd.read_csv(os.path.join(dir, filename), sep='|'))
		data = pd.concat(concat_list, ignore_index=True)
		data['date'] = data['hours'].astype(str).str.slice(0, 8)
		data = data.drop('hours', axis=1)
		day_df = data.groupby('date').size().reset_index(name='count_by_day')
		# 训练数据
		clean_df = day_df[day_df['date'].astype(str).str.slice(0, 6) == '201710']
		kmeans = KMeans(n_clusters=K, random_state=1993).fit(np.array(clean_df['count_by_day']).reshape(-1, 1))
		max_dist = [max(np.square(clean_df[kmeans.labels_ == i]['count_by_day'] - kmeans.cluster_centers_[i])) for i in range(K)]
		labels = kmeans.predict(np.array(day_df['count_by_day']).reshape(-1, 1))
		# 若样本点到距它最近的聚类中心点的距离大于该类中样本点到中心点距离的最大值，则它为异常点
		print([np.square(day_df['count_by_day'][labels == i] - kmeans.cluster_centers_[i]) <= max_dist[i] for i in range(2)])

		# start_concat_list = []
		# sub_dir = '085700411A86'
		# dir = os.path.join(SRC_DIR, sub_dir)
		# for filename in os.listdir(dir):
		# 	start_concat_list.append(pd.read_csv(os.path.join(dir, filename), sep = '|'))
		# for sub_dir in AP_LIST:
		# 	concat_list = []
		# 	concat_list.extend(start_concat_list)
		# 	print('=====================================================')
		# 	print(sub_dir)
		# 	print('=====================================================')
		# 	dir = os.path.join(SRC_DIR, sub_dir)
		# 	for filename in os.listdir(dir):
		# 		concat_list.append(pd.read_csv(os.path.join(dir, filename), sep='|'))
		# 	data = pd.concat(concat_list, ignore_index=True)
		# 	print(data.head())
		# 	print('=====================================================')

		# dir = '/Users/xujiayu/毕设/data/hours_window_process/14E4E6E173FE'
		# AP = os.path.basename(dir)
		# dest = os.path.join(DEST_DIR, AP)
		# dest_path = os.path.join(dest, 'AP_cnt-k%s.csv' % str(K))
		# concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
		# data = pd.concat(concat_list, ignore_index=True)
		# data['hours'] = data['hours'].astype(str)
		# data['date'] = data['hours'].str.slice(0, 8)
		# data['hour'] = data['hours'].str.slice(8, 10)
		# pivot_df = pd.pivot_table(data, values='rss', index='date', columns='hour', aggfunc=len, fill_value=0)
		# label = KMeans(n_clusters=K, random_state=1993).fit_predict(pivot_df)
		# pivot_df.columns = ['_'.join(['hour', hour]) for hour in pivot_df.columns.values]
		# pivot_df['label'] = label
		# engine = create_engine('mysql+mysqldb://root:root@localhost:3306/django_tutorial')
		# pivot_df.to_sql('polls_loc', con=engine, if_exists='append', index=False)
		# # pivot_df.to_csv(dest_path, index=False)
	except Exception as e:
		print("aux error: %s" % e)

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		# pool = Pool(4)
		# res_list = [pool.apply_async(main, (dir,)) for dir in dir_list]
		# pool.close()
		# pool.join()
		count_by_AP()
		# count_by_day()
		# aux()
	except Exception as e:
		raise e