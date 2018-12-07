# coding=utf8
import os
from multiprocessing import Pool
import pandas as pd

SRC_DIR = '/usr/local/data/minutes_window'
DEST_DIR = '/usr/local/data/user_AP_cnt'

def main(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		filename_list = os.listdir(dir)
		# for filename in tqdm(filename_list):
		for filename in filename_list:
			src_path = os.path.join(dir, filename)
			dest_path = os.path.join(dest, filename)
			minutes_df = pd.read_csv(src_path, sep='|', dtype={'AP': 'str'})
			user_AP_cnt_df = minutes_df.groupby(['user_mac_addr', 'AP']).size().reset_index(name='user_AP_cnt')
			user_AP_cnt_df.to_csv(dest_path, index=False)
	except Exception as e:
		print "main error: %s" % e

if __name__ == '__main__':
	try:
		dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		pool = Pool(4)
		res_list = [pool.apply_async(main, (dir,)) for dir in dir_list]
		# pool.map(main, dir_list)
		pool.close()
		pool.join()
	except Exception as e:
		raise e