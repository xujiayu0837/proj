# coding=utf8
import os
from multiprocessing import Pool
import threading
import pandas as pd
# from tqdm import tqdm
from utils_py2 import find_24h_users

MINUTES_WINDOW = '/usr/local/data/minutes_window'
USER_DATA_WITH_HEADER = '/usr/local/data/user_data_with_header'
USER_DATA = '/usr/local/data/user_data'
USERS_LIST = find_24h_users()
LOCK = threading.Lock()

def main(dir):
	try:
		AP = os.path.basename(dir)
		# for filename in tqdm(os.listdir(dir)):
		for filename in os.listdir(dir):
			src_path = os.path.join(dir, filename)
			data = pd.read_csv(src_path, sep='|')
			for user_mac_addr in data['user_mac_addr'].unique():
				if user_mac_addr in USERS_LIST:
					# print(user_mac_addr)
					continue
				user_data = data[data['user_mac_addr'] == user_mac_addr]
				dest_path = os.path.join(USER_DATA_WITH_HEADER, '%s.csv' % user_mac_addr)
				with LOCK:
					user_data.to_csv(dest_path, index=False, mode='a', sep='|')
	except Exception as e:
		print "main error: %s" % e

def clean_header(filename):
	try:
		data = pd.read_csv(os.path.join(USER_DATA_WITH_HEADER, filename), sep='|')
		data = data[data['rss'].astype(str) != 'rss']
		data['rss'] = data['rss'].astype(int)
		data.to_csv(os.path.join(USER_DATA, filename), index=False, sep='|')
	except Exception as e:
		print "clean_header error: %s" % e

# def aux(dir):
# 	try:
# 		dest = '/Users/xujiayu/Downloads'
# 		AP = os.path.basename(dir)
# 		for filename in tqdm(os.listdir(dir)):
# 		# for filename in os.listdir(dir):
# 			src_path = os.path.join(dir, filename)
# 			data = pd.read_csv(src_path, sep='|')
# 			for user_mac_addr in data['user_mac_addr'].unique():
# 				if user_mac_addr != '000000000000':
# 					continue
# 				user_data = data[data['user_mac_addr'] == user_mac_addr]
# 				dest_path = os.path.join(dest, '%s.csv' % user_mac_addr)
# 				with LOCK:
# 					user_data.to_csv(dest_path, index=False, mode='a', sep='|')
# 	except Exception as e:
# 		print("aux error: %s" % e)

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(MINUTES_WINDOW, sub_dir) for sub_dir in os.listdir(MINUTES_WINDOW) if not sub_dir.startswith('.')]
		pool = Pool(4)
		# res_list = [pool.apply_async(main, (dir,)) for dir in dir_list]
		res_list = [pool.apply_async(clean_header, (filename,)) for filename in os.listdir(USER_DATA_WITH_HEADER)]
		pool.close()
		pool.join()
	except Exception as e:
		raise e
