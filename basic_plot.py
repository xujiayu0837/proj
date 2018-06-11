import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from get_path import get_path

path = get_path()
K = 28

def plot_kmeans():
	try:
		# df_0 = pd.read_csv(os.path.join(path, '../centers_prediction_gmm_k3_0.csv'))
		# df_1 = df_0.values.reshape(41, 50)
		# df_0 = pd.read_csv(os.path.join(path, '../centers_prediction_kmeans_k3_0.csv'))
		# df_1 = df_0.values.reshape(41, 50)
		# df_0 = pd.read_csv(os.path.join(path, '../centers_prediction_kmeans_k19_0.csv'))
		# df_1 = df_0.values.reshape(41, 50)
		df_0 = pd.read_csv('/Users/xujiayu/毕设/data/rss_kmeans/000000000000.csv')
		df_1 = df_0.T
		# df_0 = pd.read_csv('/Users/xujiayu/毕设/data/count_kmeans/count_sample_kmeans-3-k30-1528684211.csv')
		# df_1 = df_0.T
		# df_0 = pd.read_csv('/Users/xujiayu/毕设/data/count_window/000000000000-07_09-k0.csv')
		# df_1 = df_0.T
		# df_0 = pd.read_csv('/Users/xujiayu/毕设/data/AP_cnt/14E4E6E173FE/AP_cnt-k2.csv')
		# df_1 = df_0.T
		# df_0 = pd.read_csv('/Users/xujiayu/毕设/data/traj_kmeans/000000000000-k9.csv')
		# df_1 = df_0.T
		for i in range(K):
			df = df_0[df_0['label'] == i]
			for j in range(len(df)):
				r = np.array(df[df['label'] == i].drop('label', axis=1).iloc[j])
				print(r)
				# plt.xlabel('AP')
				# plt.ylabel('rss')
				plt.plot(r)
			plt.show()
	except Exception as e:
		raise e

def plot():
	try:
		df_0 = pd.read_csv(os.path.join(path, '../k_cost_3.csv'))
		plt.plot(df_0['cost'])
		plt.show()
	except Exception as e:
		raise e

if __name__ == '__main__':
	try:
		plot_kmeans()
		# plot()
	except Exception as e:
		raise e