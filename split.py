import os
from multiprocessing import Pool
import threading
import argparse
import pandas as pd
from tqdm import tqdm
from utils import find_24h_users

SRC_DIR = '/Users/xujiayu/毕设/data/minutes_window'
AP_USER_DIR = '/Users/xujiayu/毕设/data/AP_user_data'
DEST_DIR = '/Users/xujiayu/毕设/data/user_data'
# SRC_DIR = '/apps/jy/code/data/user_data_bak'
# AP_USER_DIR = '/apps/jy/code/data/AP_user_data_bak'
# DEST_DIR = '/apps/jy/code/data/user_data'
USERS_LIST = find_24h_users()
AP_LIST = ['0C8268C7D518', '0C8268C7DD6C', '0C8268C7E138', '0C8268C804F8']
# PARSER = argparse.ArgumentParser()
# PARSER.add_argument("--ap")
# ARGS = PARSER.parse_args()
LOCK = threading.Lock()

def main(dir):
	try:
		AP = os.path.basename(dir)
		for filename in tqdm(os.listdir(dir)):
		# for filename in os.listdir(dir):
			src_path = os.path.join(dir, filename)
			data = pd.read_csv(src_path, sep='|')
			for user_mac_addr in data['user_mac_addr'].unique():
				if user_mac_addr in USERS_LIST:
					# print(user_mac_addr)
					continue
				user_data = data[data['user_mac_addr'] == user_mac_addr]
				dest_path = os.path.join(DEST_DIR, '%s.csv' % user_mac_addr)
				with LOCK:
					user_data.to_csv(dest_path, index=False, mode='a', sep='|')
	except Exception as e:
		print("main error: %s" % e)

def split_by_user(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(AP_USER_DIR, AP)
		for filename in tqdm(os.listdir(dir)):
		# for filename in os.listdir(dir):
			src_path = os.path.join(dir, filename)
			data = pd.read_csv(src_path, sep='|')
			for user_mac_addr in data['user_mac_addr'].unique():
				if user_mac_addr in USERS_LIST:
					# print(user_mac_addr)
					continue
				user_data = data[data['user_mac_addr'] == user_mac_addr]
				dest_path = os.path.join(dest, '%s.csv' % user_mac_addr)
				user_data.to_csv(dest_path, index=False, mode='a', sep='|')
	except Exception as e:
		print("split_by_user error: %s" % e)

def merge_by_user(dir):
	try:
		for filename in tqdm(os.listdir(dir)):
		# for filename in os.listdir(dir):
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(DEST_DIR, filename)
			data = pd.read_csv(src_path, sep='|')
			# data = pd.read_csv(src_path)
			with LOCK:
				data.to_csv(dest_path, index=False, mode='a', sep='|')
	except Exception as e:
		print("merge_by_user error: %s" % e)

def clean_header(filename):
	try:
		data = pd.read_csv(os.path.join(SRC_DIR, filename), sep='|')
		data = data[data['rss'].astype(str) != 'rss']
		data['rss'] = data['rss'].astype(int)
		data.to_csv(os.path.join(DEST_DIR, filename), index=False, sep='|')
	except Exception as e:
		print("clean_header error: %s" % e)

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in ARGS.ap.split(",")]
		# pool = Pool(40)
		pool = Pool(4)
		# pool.map(split_by_user, dir_list)
		# pool.map(merge_by_user, dir_list)
		# pool.map(main, dir_list)
		pool.map(clean_header, os.listdir(SRC_DIR))
		pool.close()
		pool.join()
	except Exception as e:
		raise e