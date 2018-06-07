import os
import calendar
import datetime
import argparse
from multiprocessing.dummy import Pool as Pool
import pickle
import pandas as pd
from tqdm import tqdm

SRC_DIR = '/Users/xujiayu/python/scandata1/201710'
DEST_DIR = '/Users/xujiayu/毕设/data/scandata'
# SRC_DIR = '/Users/xujiayu/毕设/data/scandata_0526'
# DEST_DIR = '/Users/xujiayu/毕设/data/minutes_window'
DIR = '/Users/xujiayu/毕设/data/AP_user_data'
PICKLE_DIR_PATH = '/Users/xujiayu/毕设/data/24h_users_pickle/24h_users_pickle.pickle'
AP_LIST = ['0C8268EE3868', '0C8268EE38EE', '14CF924A98F2', '0C8268C7D518', '0C8268EE7164',
 '14E4E6E172EA', 'EC172FE3B340', '085700411A86', '0C8268C7E138', '0C8268EE3878', 
 '14E4E6E186A4', '14E4E6E17648', '388345A236BE', '14E4E6E17A34', '14E4E6E173FE', 
 '14E6E4E1C510', '0C8268F1648E', '0C8268F90E64', '0C8268F15C64', '0C8268C804F8', 
 '0C8268C7DD6C', '14E4E6E1867A', '0857004127E2', '14E4E6E179F2', '0C8268F17FB8', 
 '085700412D4E', '0C8268F17F60', '0C8268C7D504', '0C8268F93B0A', '14E4E6E16E7A', 
 '0C8268F9314E', '14E4E6E1790A', '14E4E6E17950', '14E4E6E17908', '0C8268F15CB2', 
 '0C8268EE3F32', '14E4E6E176C8', '14E4E6E18658', '0C8268F933A2', '5C63BFD90AE2']
INVALID_STR_LIST = ['1504CBB58A48D4C', '150908900EC0AE78595', '150772BA3CFF5B93', '150DAA1193735ED', '1505CADCF851D9F', '150908904DA1ACBE68AA6',
 '150F0B42994E576', '150F0B42994E576']
PARSER = argparse.ArgumentParser()
PARSER.add_argument("--year")
PARSER.add_argument("--month")
ARGS = PARSER.parse_args()

def add_header():
	try:
		return ','.join(['mac_' + str(i) for i in range(1, 41)]) + ',label'
	except Exception as e:
		raise e

def mkdir_date():
	try:
		date_list = concat_date()
		for date in date_list:
			dir = os.path.join(DIR, date)
			if not os.path.exists(dir):
				os.mkdir(dir)
	except Exception as e:
		raise e

def mkdir_AP():
	try:
		for AP in AP_LIST:
			dir = os.path.join(DIR, AP)
			if not os.path.exists(dir):
				os.mkdir(dir)
	except Exception as e:
		raise e

def concat_date():
	try:
		num_days = calendar.monthrange(int(ARGS.year), int(ARGS.month))[1]
		dt = datetime.datetime.strptime(''.join([ARGS.year, ARGS.month]), "%Y%m")
		date_list = [(dt + datetime.timedelta(days=i)).strftime("%Y%m%d") for i in range(num_days)]
		return date_list
	except Exception as e:
		print("concat_date error: %s" % e)

def add_col_AP_concurrently(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		for filename in os.listdir(dir):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, "%s.csv" % filename)
			data = pd.read_csv(src_path, sep='|', names=['user_mac_addr', 'rss', 'ts'])
			data['AP'] = AP
			data.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("add_col_AP_concurrently error: %s" % e)

def add_col_AP():
	try:
		for sub_dir in os.listdir(SRC_DIR):
			if sub_dir.startswith('.'):
				continue
			concat_list = []
			dir = os.path.join(SRC_DIR, sub_dir)
			dest_path = os.path.join(DEST_DIR, "%s.csv" % sub_dir)
			for AP in os.listdir(dir):
				data = pd.read_csv(os.path.join(dir, AP), sep='|', names=['user_mac_addr', 'rss', 'ts'])
				data['AP'] = AP
				concat_list.append(data)
			concat_data = pd.concat(concat_list, ignore_index=True)
			concat_data.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		raise e

def minutes_handle():
	try:
		# for filename in tqdm(os.listdir(SRC_DIR)):
		for filename in tqdm(FILENAME_LIST):
			data = pd.read_csv(os.path.join(SRC_DIR, filename), sep='|')
			data = data[data['rss'] > -90]
			data['dt'] = pd.to_datetime(data['ts'], unit='s') + datetime.timedelta(hours=8)
			data = data.drop('ts', axis=1)
			data['minutes'] = data['dt'].dt.strftime("%Y%m%d%H%M")
			data = data.drop('dt', axis=1)
			minutes_df = data.groupby(['user_mac_addr', 'AP', 'minutes']).agg({'rss': 'max'}).reset_index()
			dest_path = os.path.join(DEST_DIR, filename)
			minutes_df.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("minutes_handle error: %s" % e)

def check_invalid_str():
	try:
		invalid_str = '1504CBB58A48D4C'
		for sub_dir in tqdm(os.listdir(DIR)):
			if sub_dir.startswith('.'):
				continue
			dir = os.path.join(DIR, sub_dir)
			for filename in os.listdir(dir):
				if filename.startswith('.'):
					continue
				src_path = os.path.join(dir, filename)
				with open(src_path, 'r') as fr:
					for line in fr:
						if invalid_str in line:
							print(src_path)
	except Exception as e:
		raise e

def find_24h_users():
	try:
		with open(PICKLE_DIR_PATH, 'rb') as fr:
			users_set = pickle.load(fr)
		return users_set
	except Exception as e:
		print("find_24h_users error: %s" % e)

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		# pool = Pool(40)
		# pool.map(add_col_AP_concurrently, dir_list)
		# pool.close()
		# pool.join()
		# check_invalid_str()
		# minutes_handle()
		mkdir_AP()
		# add_col_AP()
		# mkdir_date()
		# print(add_header())
	except Exception as e:
		raise e