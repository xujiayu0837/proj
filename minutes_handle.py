import os
import datetime
# from multiprocessing.dummy import Pool as Pool
from multiprocessing import Pool
import pandas as pd
from tqdm import tqdm

SRC_DIR = '/Users/xujiayu/毕设/data/scandata'
DEST_DIR = '/Users/xujiayu/毕设/data/minutes_window_add'
# DEST_DIR = '/Users/xujiayu/毕设/data/hours_window_process'
DIR_LIST = ['EC172FE3B340', '14E4E6E18658', '0C8268F17F60', '0C8268C804F8']

def main(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		# for filename in tqdm(os.listdir(dir)):
		for filename in tqdm(sorted(os.listdir(dir), reverse=True)):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, filename)
			data = pd.read_csv(src_path, sep='|')
			data = data[(data['ts'].astype(str).str.len() == 10) & (data['rss'].astype(str).str.len() == 3)]
			data = data[data['rss'].astype(int) > -90]
			data['dt'] = pd.to_datetime(data['ts'], unit='s') + datetime.timedelta(hours=8)
			data = data.drop('ts', axis=1)
			data['minutes'] = data['dt'].dt.strftime("%Y%m%d%H%M")
			data = data.drop('dt', axis=1)
			minutes_df = data.groupby(['user_mac_addr', 'AP', 'minutes']).agg({'rss': 'max'}).reset_index()
			minutes_df.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("main error: %s" % e)

def hours_handle(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		for filename in tqdm(os.listdir(dir)):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, filename)
			data = pd.read_csv(src_path, sep='|')
			data = data[(data['ts'].astype(str).str.len() == 10) & (data['rss'].astype(str).str.len() == 3)]
			data = data[data['rss'].astype(int) > -90]
			data['dt'] = pd.to_datetime(data['ts'], unit='s') + datetime.timedelta(hours=8)
			data = data.drop('ts', axis=1)
			data['hours'] = data['dt'].dt.strftime("%Y%m%d%H")
			data = data.drop('dt', axis=1)
			hours_df = data.groupby(['user_mac_addr', 'AP', 'hours']).agg({'rss': 'max'}).reset_index()
			hours_df.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("hours_handle error: %s" % e)

def aux():
	try:
		dest = '/Users/xujiayu/Downloads/test'
		dir = '/Users/xujiayu/毕设/data/scandata/14E4E6E17648'
		AP = os.path.basename(dir)
		for filename in tqdm(sorted(os.listdir(dir), reverse=True)):
		# for filename in tqdm(FILENAME_LIST):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, filename)
			data = pd.read_csv(src_path, sep='|')
			data = data[(data['ts'].astype(str).str.len() == 10) & (data['rss'].astype(str).str.len() == 3)]
			data = data[data['rss'].astype(int) > -90]
			data['dt'] = pd.to_datetime(data['ts'], unit='s') + datetime.timedelta(hours=8)
			data = data.drop('ts', axis=1)
			data['minutes'] = data['dt'].dt.strftime("%Y%m%d%H%M")
			data = data.drop('dt', axis=1)
			minutes_df = data.groupby(['user_mac_addr', 'AP', 'minutes']).agg({'rss': 'max'}).reset_index()
			minutes_df.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("aux error: %s" % e)

if __name__ == '__main__':
	try:
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in DIR_LIST]
		pool = Pool(40)
		pool.map(main, dir_list)
		# pool.map(hours_handle, dir_list)
		pool.close()
		pool.join()
		# aux()
	except Exception as e:
		raise e