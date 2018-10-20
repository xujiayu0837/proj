# coding=utf8
import os
from multiprocessing import Pool
import csv
import pickle
import pandas as pd
# from tqdm import tqdm
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

SRC_DIR = '/usr/local/data/hours_window'
# SRC_DIR_KMEANS = '/Users/xujiayu/毕设/data/user_AP_cnt'
# DEST_DIR = '/Users/xujiayu/毕设/data/24h_users_rule'
# DEST_DIR_KMEANS = '/Users/xujiayu/毕设/data/24h_users_kmeans'
PICKLE_DIR_KMEANS = '/usr/local/data/24h_users_list'
PICKLE_DIR = '/usr/local/data/24h_users_pickle'
K=2
LABEL_OUTLIER = 1

# 把40个pickle文件合并为1个pickle文件
def find_24h_users():
	try:
		users_set = set()
		# for filename in os.listdir(PICKLE_DIR_KMEANS):
		# 	with open(os.path.join(PICKLE_DIR_KMEANS, filename), 'rb') as fr:
		# 		users_set = {item for item in pickle.load(fr)}
		with open(os.path.join(PICKLE_DIR, '24h_users_pickle.pickle'), 'wb') as fw:
			pickle.dump(users_set, fw)
		return users_set
	except Exception as e:
		print "find_24h_users error: %s" % e

# def detect_outlier(dir):
# 	try:
# 		user_set = set()
# 		AP = os.path.basename(dir)
# 		dest_path = os.path.join(DEST_DIR, '-'.join([os.path.basename(DEST_DIR), AP]))
# 		# for filename in tqdm(os.listdir(dir)):
# 		for filename in os.listdir(dir):
# 			src_path = os.path.join(dir, filename)
# 			date = filename.split(".")[0]
# 			hours_df = pd.read_csv(src_path, sep='|')
# 			hours_df = hours_df[hours_df['hours'].astype(str).str.startswith(date)]
# 			user_AP_cnt_df = hours_df.groupby('user_mac_addr').size().reset_index(name='user_AP_cnt')
# 			filter_df = user_AP_cnt_df[user_AP_cnt_df['user_AP_cnt'] == 24]
# 			if filter_df.shape[0] > 0:
# 				user_set |= filter_df.apply(set)['user_mac_addr']
# 		# write_to_file(dir, user_set, '')
# 		return user_set
# 	except Exception as e:
# 		print "detect_outlier error: %s" % e

# def detect_outlier_kmeans(dir):
# 	try:
# 		user_cnt_dict = {}
# 		AP = os.path.basename(dir)
# 		dest_path = os.path.join(DEST_DIR_KMEANS, '-'.join([os.path.basename(DEST_DIR_KMEANS), AP]))
# 		# for filename in tqdm(os.listdir(dir)):
# 		for filename in os.listdir(dir):
# 			with open(os.path.join(dir, filename), 'r') as csvfile:
# 				user_cnt_dict = {row['user_mac_addr']: user_cnt_dict[row['user_mac_addr']] + int(row['user_AP_cnt']) if row['user_mac_addr'] in user_cnt_dict else int(row['user_AP_cnt']) for row in csv.DictReader(csvfile)}
# 			# plt.hist(user_cnt_dict.values(), 2)
# 		# pickle_dump(dir, user_cnt_dict)
# 		# data = user_cnt_dict.values()
# 		# indices = np.arange(len(data))
# 		# label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(list(data)).reshape(-1, 1))
# 		# plt.scatter(indices, data, c=label, marker='x')
# 		# plt.show()
# 		sorted_users = sorted(user_cnt_dict, key=user_cnt_dict.get)
# 		label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(sorted(user_cnt_dict.values())).reshape(-1, 1))
# 		users_list = sorted_users[len(label[label != label[-1]]):]
# 		# write_to_file(dir, users_list, 'k-means')
# 		return users_list
# 	except Exception as e:
# 		print "detect_outlier_kmeans error: %s" % e

def hours_count_user_AP_pair(dir):
	try:
		concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
		data = pd.concat(concat_list, ignore_index=True)
		hours_user_AP_cnt_df = data.groupby('user_mac_addr').size().reset_index(name='hours_user_AP_cnt')
		# label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(hours_user_AP_cnt_df['hours_user_AP_cnt']).reshape(-1, 1))
		kmeans = KMeans(n_clusters=2, random_state=1993).fit(np.array(hours_user_AP_cnt_df['hours_user_AP_cnt']).reshape(-1, 1))
		label = kmeans.labels_
		users_list = hours_user_AP_cnt_df['user_mac_addr'][label == np.argmax(kmeans.cluster_centers_)]
		pickle_dump(dir, users_list)
		print(kmeans.cluster_centers_)
		print('%s, %s' % (len(users_list), hours_user_AP_cnt_df.shape[0]))
	except Exception as e:
		print "hours_count_user_AP_pair error: %s" % e

def pickle_dump(dir, data):
	try:
		AP = os.path.basename(dir)
		with open(os.path.join(PICKLE_DIR_KMEANS, '%s.pickle' % AP), 'wb') as fw:
			pickle.dump(data, fw)
	except Exception as e:
		print "pickle_dump error: %s" % e

# def count_user_monthly():
# 	try:
# 		for filename in os.listdir(PICKLE_DIR_KMEANS):
# 			user_cnt_dict = {}
# 			with open(os.path.join(PICKLE_DIR_KMEANS, filename), 'rb') as fr:
# 				user_cnt_dict = pickle.load(fr)
# 			print(filename)
# 			plt.hist(user_cnt_dict.values(), 2)
# 			plt.show()
# 	except Exception as e:
# 		raise e

# def write_to_file(dir, data, sol):
# 	try:
# 		AP = os.path.basename(dir)
# 		if sol == 'k-means':
# 			dest_path = os.path.join(DEST_DIR_KMEANS, '-'.join([os.path.basename(DEST_DIR_KMEANS), AP]))
# 			with open(dest_path, 'w') as fw:
# 				fw.write(', '.join(data))
# 		else:
# 			dest_path = os.path.join(DEST_DIR, '-'.join([os.path.basename(DEST_DIR), AP]))
# 			with open(dest_path, 'w') as fw:
# 				fw.write(', '.join(list(data)))
# 	except Exception as e:
# 		print "write_to_file error: %s" % e

# def write_to_file_both(sub_dir):
# 	try:
# 		dest_path = os.path.join(DEST_DIR, '-'.join([os.path.basename(DEST_DIR), sub_dir]))
# 		dest_path_kmeans = os.path.join(DEST_DIR_KMEANS, '-'.join([os.path.basename(DEST_DIR_KMEANS), sub_dir]))
# 		users_list = list(detect_outlier(os.path.join(SRC_DIR, sub_dir)))
# 		users_list_kmeans = detect_outlier_kmeans(os.path.join(SRC_DIR_KMEANS, sub_dir))
# 		with open(dest_path, 'w') as fw:
# 			fw.write(', '.join(users_list))
# 		with open(dest_path_kmeans, 'w') as fw:
# 			fw.write(', '.join(users_list_kmeans))
# 	except Exception as e:
# 		raise e

# def cmp_two_sol(sub_dir):
# 	try:
# 		users_set = detect_outlier(os.path.join(SRC_DIR, sub_dir))
# 		users_set_kmeans = set(detect_outlier_kmeans(os.path.join(SRC_DIR_KMEANS, sub_dir)))
# 		print('%s|%s\n' % (users_set - users_set_kmeans, users_set_kmeans - users_set))
# 	except Exception as e:
# 		print "cmp_two_sol error: %s" % e

# def aux():
# 	try:
# 		# dir = '/Users/xujiayu/毕设/data/hours_window_process/085700411A86'
# 		# for filename in os.listdir(dir):
# 		# 	src_path = os.path.join(dir, filename)
# 		# 	date = filename.split(".")[0]
# 		# 	hours_df = pd.read_csv(src_path, sep='|')
# 		# 	hours_df = hours_df[hours_df['hours'].astype(str).str.startswith(date)]
# 		# 	user_AP_cnt_df = hours_df.groupby('user_mac_addr').size().reset_index(name='user_AP_cnt')
# 		# 	# plt.plot(user_AP_cnt_df['user_AP_cnt'])
# 		# 	plt.hist(user_AP_cnt_df['user_AP_cnt'], 10)

# 		# dir = '/Users/xujiayu/毕设/data/user_AP_cnt/085700411A86'
# 		# for filename in os.listdir(dir):
# 		# 	user_cnt_dict = {}
# 		# 	with open(os.path.join(dir, filename), 'r') as csvfile:
# 		# 		user_cnt_dict = {row['user_mac_addr']: user_cnt_dict[row['user_mac_addr']] + int(row['user_AP_cnt']) if row['user_mac_addr'] in user_cnt_dict else int(row['user_AP_cnt']) for row in csv.DictReader(csvfile)}
# 		# 	plt.hist(user_cnt_dict.values(), 2)

# 		for sub_dir in os.listdir(SRC_DIR):
# 			if sub_dir.startswith('.'):
# 				continue
# 			dir = os.path.join(SRC_DIR, sub_dir)
# 			concat_list = [pd.read_csv(os.path.join(dir, filename), sep='|') for filename in os.listdir(dir)]
# 			data = pd.concat(concat_list, ignore_index=True)
# 			hours_user_AP_cnt_df = data.groupby('user_mac_addr').size().reset_index(name='hours_user_AP_cnt')
# 			data['days'] = data['hours'].astype(str).str.slice(0, 8)
# 			data = data.drop('hours', axis=1)
# 			days_cnt_df = data.groupby('user_mac_addr')['days'].nunique().reset_index(name='days_cnt')
# 			cnt_df = hours_user_AP_cnt_df.join(days_cnt_df.set_index('user_mac_addr'), on='user_mac_addr')
# 			cnt_df['cnt'] = cnt_df['hours_user_AP_cnt'] / cnt_df['days_cnt']
# 			# cnt_df = cnt_df[cnt_df['cnt'] > 1]
# 			# min = np.min(cnt_df['cnt'])
# 			# max = np.max(cnt_df['cnt'])
# 			# cnt_df['min_max'] = (cnt_df['cnt'] - min) / (max - min)
# 			label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(cnt_df['hours_user_AP_cnt']).reshape(-1, 1))
# 			# label = KMeans(n_clusters=K, random_state=1993).fit_predict(np.array(cnt_df[['cnt', 'hours_user_AP_cnt']]))
# 			# gmm = GaussianMixture(n_components=K, random_state=1993)
# 			# gmm.fit(np.array(cnt_df['cnt']).reshape(-1, 1))
# 			# label = gmm.predict(np.array(np.log(cnt_df['cnt'])).reshape(-1, 1))
# 			# gmm.fit(np.array(cnt_df[['cnt', 'hours_user_AP_cnt']]))
# 			# label = gmm.predict(np.array(cnt_df[['cnt', 'hours_user_AP_cnt']]))
# 			# print('%s\n\n%s\n\n\n\n' % (gmm.means_, gmm.covariances_))
# 			# plt.scatter(cnt_df['hours_user_AP_cnt'], label, marker='x')
# 			plt.scatter(cnt_df['hours_user_AP_cnt'], np.zeros(cnt_df.shape[0]), c=label, marker='x')
# 			# plt.scatter(cnt_df['cnt'], cnt_df['hours_user_AP_cnt'], c=label, marker='x')
# 			# plt.hist(cnt_df['cnt'], K)
# 			plt.show()
# 			# users_list = cnt_df['user_mac_addr'][label == LABEL_OUTLIER]
# 	except Exception as e:
# 		print "aux error: %s" % e

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		
		# dir_list_kmeans = [os.path.join(SRC_DIR_KMEANS, sub_dir) for sub_dir in os.listdir(SRC_DIR_KMEANS) if not sub_dir.startswith('.')]
		# pool = Pool(4)
		# pool.map(hours_count_user_AP_pair, dir_list)

		# pool.map(detect_outlier, dir_list)
		# pool.map(detect_outlier_kmeans, dir_list_kmeans)
		# pool.map(cmp_two_sol, os.listdir(SRC_DIR))
		# pool.close()
		# pool.join()

		# count_user_monthly()
		# aux()
		find_24h_users()
	except Exception as e:
		raise e