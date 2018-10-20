import sys
import os

def get_path():
	try:
		pwd = sys.path[0]
		return os.path.abspath(pwd)
	except Exception as e:
		raise e

if __name__ == '__main__':
	try:
		path = get_path()
		print("path: %s" % path)
	except Exception as e:
		raise e