import os
from multiprocessing import Pool
import pandas as pd
from tqdm import tqdm

SRC_DIR = '/Users/xujiayu/python/scandata1/201710'
DEST_DIR = '/Users/xujiayu/毕设/data/clean_data'
# SRC_DIR = '/apps/jy/code/data/201710'
# DEST_DIR = '/apps/jy/code/data/clean_data'

def main(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		for filename in tqdm(os.listdir(dir)):
		# for filename in os.listdir(dir):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, '%s.csv' % filename)
			data = pd.read_csv(src_path, sep='|', names=['user_mac_addr', 'rss', 'ts'])
			data = filter_invalid_data(data)
			add_col_AP(data, AP)
			data.to_csv(dest_path, index=False, sep='|')
	except Exception as e:
		print("main error: %s" % e)

def filter_invalid_data(data):
	try:
		return data[(data['rss'].astype(str).str.len() == 3) & (data['ts'].astype(str).str.len() == 10)]
	except Exception as e:
		print("filter_invalid_data error: %s" % e)

def add_col_AP(data, AP):
	try:
		data['AP'] = AP
	except Exception as e:
		print("add_col_AP error: %s" % e)

def aux():
	try:
		dir = '/Users/xujiayu/python/scandata1/201710/0C8268F17F60'
		AP = os.path.basename(dir)
		for filename in os.listdir(dir):
			if filename.startswith('.'):
				continue
			src_path = os.path.join(dir, filename)
			data = pd.read_csv(src_path, sep='|', names=['user_mac_addr', 'rss', 'ts'])
			print(data.shape)
			data = filter_invalid_data(data)
			print(data.shape)
			add_col_AP(data, AP)
			print(data.shape)
	except Exception as e:
		print("aux error: %s" % e)

if __name__ == '__main__':
	try:
		dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		pool = Pool(4)
		res_list = [pool.apply_async(main, (dir,)) for dir in dir_list]
		pool.close()
		pool.join()
		# aux()
	except Exception as e:
		raise e