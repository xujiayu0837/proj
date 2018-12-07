import os
import calendar
import datetime
from multiprocessing import Pool
import threading
import argparse
import paramiko

IP = '10.205.29.46'
PORT = 22
USR = 'xujiayu'
PASS = 'xujiayu63300716'
SRC_DIR = '/home/data/scandata'
DEST_DIR = '/Users/xujiayu/python/scandata1/201510'
AP_LIST = ['0C8268EE3F32', '0C8268F15C64', '0C8268F15CB2', '0C8268F17F60', '0C8268F17FB8',
'0C8268F90E64', '0C8268F93B0A', '0C8268F933A2', '0C8268F1648E', '0C8268F9314E', '5C63BFD90AE2', '388345A236BE', '085700411A86', '085700412D4E', '0857004127E2', 'EC172FE3B340']
PARSER = argparse.ArgumentParser()
PARSER.add_argument("--date")
PARSER.add_argument("--year")
PARSER.add_argument("--month")
ARGS = PARSER.parse_args()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IP, PORT, USR, PASS)
sftp = ssh.open_sftp()
# sftp.put('/home/data/scandata/0C8268F9314E/20170928', '/Users/xujiayu/python/scandata/201709/20170928/0C8268F9314E')

def scp_by_date():
	try:
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			src_path = os.path.join(dir, ARGS.date)
			dest = os.path.join(DEST_DIR, ARGS.date)
			dest_path = os.path.join(dest, sub_dir)
			if os.path.exists(src_path):
				sftp.put(src_path, dest_path)


		# dest = os.path.join(DEST_DIR, ARGS.date)
		# # if not os.path.exists(dest):
		# # 	os.mkdir(dest)
		# dir = os.path.join(SRC_DIR, sub_dir)
		# src_path = os.path.join(dir, ARGS.date)
		# dest_path = os.path.join(dest, sub_dir)
		# # print "dest_path: %s" % dest_path
		# sftp.put(src_path, dest_path)
	except Exception as e:
		raise e

def scp_monthly():
	try:
		date_list = concat_date()
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			for date in date_list:
				src_path = os.path.join(dir, date)
				dest = os.path.join(DEST_DIR, date)
				dest_path = os.path.join(dest, sub_dir)
				if os.path.exists(src_path):
					sftp.put(src_path, dest_path)
	except Exception as e:
		# print "scp_monthly error: %s" % e
		raise e

def scp_oct():
	try:
		for filename in os.listdir(SRC_DIR):
			src_path = os.path.join(SRC_DIR, filename)
			dest_path = os.path.join(DEST_DIR, filename)
			if os.path.exists(src_path):
				sftp.put(src_path, dest_path)
	except Exception as e:
		raise e

def scp_old():
	try:
		date_list = concat_date()
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			dest = os.path.join(DEST_DIR, sub_dir)
			for date in date_list:
				src_path = os.path.join(dir, date)
				dest_path = os.path.join(dest, date)
				if os.path.exists(src_path):
					sftp.put(src_path, dest_path)
	except Exception as e:
		raise e

def concat_dir():
	try:
		dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR)]
		return dir_list
	except Exception as e:
		# print "error: %s" % e
		raise e

def scp(dir):
	try:
		AP = os.path.basename(dir)
		dest = os.path.join(DEST_DIR, AP)
		date_list = concat_date()
		for date in date_list:
			src_path = os.path.join(dir, date)
			dest_path = os.path.join(dest, date)
			if os.path.exists(src_path):
				print "src_path: %s, dest_path: %s" % (src_path, dest_path)
				sftp.put(src_path, dest_path)
	except Exception as e:
		print "scp eror: %s" % e

def concat_date():
	try:
		num_days = calendar.monthrange(int(ARGS.year), int(ARGS.month))[1]
		dt = datetime.datetime.strptime(''.join([ARGS.year, ARGS.month]), "%Y%m")
		date_list = [(dt + datetime.timedelta(days=i)).strftime("%Y%m%d") for i in range(num_days)]
		return date_list
	except Exception as e:
		# print "concat_date error: %s" % e
		raise e

def check_path_exists():
	try:
		date_list = concat_date()
		for sub_dir in os.listdir(SRC_DIR):
			dir = os.path.join(SRC_DIR, sub_dir)
			for date in date_list:
				src_path = os.path.join(dir, date)
				dest = os.path.join(DEST_DIR, date)
				dest_path = os.path.join(dest, sub_dir)
				if not os.path.exists(src_path):
					# print "src_path: %s" % src_path
					print("src_path: %s" % src_path)
	except Exception as e:
		raise e

def aux():
	try:
		date_list = concat_date()
		for sub_dir in AP_LIST:
			dir = os.path.join(SRC_DIR, sub_dir)
			dest = os.path.join(DEST_DIR, sub_dir)
			for date in date_list:
				src_path = os.path.join(dir, date)
				dest_path = os.path.join(dest, date)
				if os.path.exists(src_path):
					sftp.put(src_path, dest_path)
	except Exception as e:
		raise e

if __name__ == '__main__':
	try:
		# scp_old()
		# scp_oct()
		# check_path_exists()
		# scp_monthly()
		# scp_by_date()
		# dir_list = os.listdir(SRC_DIR)
		aux()
		# dir_list = [os.path.join(SRC_DIR, sub_dir) for sub_dir in os.listdir(SRC_DIR) if not sub_dir.startswith('.')]
		# pool = Pool(4)
		# res_list = [pool.apply_async(scp, (dir,)) for dir in dir_list]
		# pool.close()
		# pool.join()
	except Exception as e:
		raise e