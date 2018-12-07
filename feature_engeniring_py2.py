# coding=utf8
import os
import datetime
import time
import pandas as pd
from tqdm import tqdm
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from constants import AP_LOC_DICT
from utils import convert_minutes

SRC_DIR = '/Users/xujiayu/毕设/data/user_data'
DEST_DIR_RSS = '/Users/xujiayu/毕设/data/rss_kmeans'
# DEST_DIR_CNT = '/Users/xujiayu/毕设/data/count_kmeans'

# 单个用户分析, 特征为信号强度
def rss_kmeans(filename):
	try:
		pivot_df = rss_kmeans_helper(filename)
		label = KMeans(n_clusters=len(pivot_df.columns), random_state=1993).fit_predict(pivot_df)
		pivot_df.columns = [AP_LOC_DICT[AP] for AP in pivot_df.columns.values]
		pivot_df['label'] = label
		pivot_df.to_csv(os.path.join(DEST_DIR_RSS, filename), index=False)
	except Exception as e:
		print "rss_kmeans error: %s" % e

def rss_center_kmeans(num_sample, k0, k1):
	try:
		concat_list = []
		for i in range(num_sample):
			pivot_df = rss_kmeans_helper(os.listdir(SRC_DIR)[i])
			if k0 == 0:
				concat_list.append(pd.DataFrame(KMeans(n_clusters=len(pivot_df.columns), random_state=1993).fit(pivot_df).cluster_centers_, columns=pivot_df.columns))
			else:
				concat_list.append(pd.DataFrame(KMeans(n_clusters=k0, random_state=1993).fit(pivot_df).cluster_centers_, columns=pivot_df.columns))
		center_df = pd.concat(concat_list, axis=0, ignore_index=True).fillna(-90)
		label = KMeans(n_clusters=k1, random_state=1993).fit_predict(center_df)
		center_df.columns = [AP_LOC_DICT[AP] for AP in center_df.columns.values]
		center_df['label'] = label
		dest_filename = 'rss_center_kmeans-%s-k_%s_%s-%s.csv' % (str(num_sample), str(k0), str(k1), str(int(time.time())))
		center_df.to_csv(os.path.join(DEST_DIR_RSS, dest_filename), index=False)
	except Exception as e:
		print "rss_center_kmeans error: %s" % e

def rss_kmeans_helper(filename):
	try:
		minutes_df = pd.read_csv(os.path.join(SRC_DIR, filename), sep='|')
		minutes_df = convert_minutes(minutes_df)
		minutes_df['user_mac_addr'] = minutes_df['user_mac_addr'].astype(str)
		# pivot_df = pd.pivot_table(minutes_df, values='rss', index=['user_mac_addr', 'minutes'], columns='AP', fill_value=-90)
		pivot_df = pd.pivot_table(minutes_df, values='rss', index=['user_mac_addr', '5_minutes'], columns='AP', fill_value=-90)
		return pivot_df
	except Exception as e:
		print "rss_kmeans_helper error: %s" % e

def count_kmeans(filename):
	try:
		pivot_df = count_kmeans_helper(filename)
		label = KMeans(n_clusters=len(pivot_df.columns), random_state=1993).fit_predict(pivot_df)
		pivot_df.columns = [AP_LOC_DICT[AP] for AP in pivot_df.columns.values]
		pivot_df['label'] = label
		pivot_df.to_csv(os.path.join(DEST_DIR_CNT, filename), index=False)
	except Exception as e:
		print "count_kmeans error: %s" % e

# 多个用户的聚类中心再次聚类, 特征为次数
def count_center_kmeans(num_sample, k0, k1):
	try:
		concat_list = []
		for i in range(num_sample):
			pivot_df = count_kmeans_helper(os.listdir(SRC_DIR)[i])
			if k0 == 0:
				concat_list.append(pd.DataFrame(KMeans(n_clusters=len(pivot_df.columns), random_state=1993).fit(pivot_df).cluster_centers_, columns=pivot_df.columns))
			else:
				concat_list.append(pd.DataFrame(KMeans(n_clusters=k0, random_state=1993).fit(pivot_df).cluster_centers_, columns=pivot_df.columns))
		center_df = pd.concat(concat_list, axis=0, ignore_index=True).fillna(0)
		label = KMeans(n_clusters=k1, random_state=1993).fit_predict(center_df)
		center_df.columns = [AP_LOC_DICT[AP] for AP in center_df.columns.values]
		center_df['label'] = label
		dest_filename = 'count_center_kmeans-%s-k_%s_%s-%s.csv' % (str(num_sample), str(k0), str(k1), str(int(time.time())))
		center_df.to_csv(os.path.join(DEST_DIR_CNT, dest_filename), index=False)
	except Exception as e:
		print "count_center_kmeans error: %s" % e

# 多个用户原始数据聚类, 特征为次数
def count_sample_kmeans(num_sample, k):
	try:
		concat_list = [pd.read_csv(os.path.join(SRC_DIR, os.listdir(SRC_DIR)[i]), sep='|') for i in range(num_sample)]
		sample_df = pd.concat(concat_list, axis=0, ignore_index=True)
		sample_df['user_mac_addr'] = sample_df['user_mac_addr'].astype(str)
		sample_df['hours'] = sample_df['minutes'].astype(str).str.slice(0, 10)
		pivot_df = pd.pivot_table(sample_df, values='rss', index=['user_mac_addr', 'hours'], columns='AP', aggfunc=len, fill_value=0)
		if k == 0:
			k = len(pivot_df.columns)
		label = KMeans(n_clusters=k, random_state=1993).fit_predict(pivot_df)
		pivot_df.columns = [AP_LOC_DICT[AP] for AP in pivot_df.columns.values]
		pivot_df['label'] = label
		dest_filename = 'count_sample_kmeans-%s-k%s-%s.csv' % (str(num_sample), str(k), str(int(time.time())))
		pivot_df.to_csv(os.path.join(DEST_DIR_CNT, dest_filename), index=False)
	except Exception as e:
		print "count_sample_kmeans error: %s" % e

def count_kmeans_helper(filename):
	try:
		minutes_df = pd.read_csv(os.path.join(SRC_DIR, filename), sep='|')
		minutes_df['user_mac_addr'] = minutes_df['user_mac_addr'].astype(str)
		minutes_df['hours'] = minutes_df['minutes'].astype(str).str.slice(0, 10)
		pivot_df = pd.pivot_table(minutes_df, values='rss', index=['user_mac_addr', 'hours'], columns='AP', aggfunc=len, fill_value=0)
		return pivot_df
	except Exception as e:
		print "count_kmeans_helper error: %s" % e

def init_cnt_df():
	try:
		sample_df = pd.DataFrame({'user_mac_addr': [], 'hours': []}).set_index(['user_mac_addr', 'hours'])
	except Exception as e:
		print "init_cnt_df error: %s" % e

def aux():
	try:
		# pair_dist_dict = {}
		# dist_list = [euclidean_distances(np.array(pivot_df[pivot_df['label'] == i].drop('label', axis=1))) for i in range(k)]
		# pivot_df[pivot_df['label'] == 1].head()
		# pivot_df[pivot_df['label'] == 1].index.values[-1][0]

		num_sample = 2
		k = 0
		concat_list = [count_kmeans_helper(os.listdir(SRC_DIR)[i]) for i in range(num_sample)]
		sample_df = pd.concat(concat_list, axis=0, ignore_index=True).fillna(0)
		if k == 0:
			k = len(sample_df.columns)
		label = KMeans(n_clusters=k, random_state=1993).fit_predict(sample_df)
		sample_df['label'] = label
		dest_filename = 'count_sample_kmeans-%s-k%s-%s.csv' % (str(num_sample), str(k), str(int(time.time())))
		sample_df.to_csv(os.path.join(DEST_DIR_CNT, dest_filename), index=False)

		# sample_df = pd.DataFrame({'user_mac_addr': [], 'hours': []}).set_index(['user_mac_addr', 'hours'])
		# for i in range(num_sample):
		# 	pivot_df = count_kmeans_helper(os.listdir(SRC_DIR)[i])
		# 	sample_df = pd.merge(sample_df, pivot_df, on=['user_mac_addr', 'hours'], how='outer').fillna(0)
		# label = KMeans(n_clusters=len(sample_df.columns), random_state=1993).fit_predict(sample_df)
		# sample_df['label'] = label
		# dest_filename = '.'.join(['-'.join(['count_sample_kmeans', str(num_sample), str(int(time.time()))]), 'csv'])
		# sample_df.to_csv(os.path.join(DEST_DIR_CNT, dest_filename), index=False)
	except Exception as e:
		print "aux error: %s" % e

if __name__ == '__main__':
	try:
		rss_kmeans('00044B6631FD.csv')
		# rss_center_kmeans(2, k0=0, k1=4)
		# count_kmeans('000000000000.csv')
		# count_sample_kmeans(3, k=31)
		# count_center_kmeans(2, k0=0, k1=3)
		# aux()
	except Exception as e:
		raise e