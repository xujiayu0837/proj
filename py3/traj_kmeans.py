import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from constants import AP_LOC_DICT

SRC_DIR = '/Users/xujiayu/毕设/data/user_data'
DEST_DIR = '/Users/xujiayu/毕设/data/traj_kmeans'

def main(filename, k):
	try:
		src_path = os.path.join(SRC_DIR, filename)
		minutes_df = pd.read_csv(src_path, sep='|')
		minutes_df['loc'] = [AP_LOC_DICT[AP] for AP in minutes_df['AP']]
		minutes_df = minutes_df.drop('AP', axis=1)
		minutes_df['minutes'] = minutes_df['minutes'].astype(str)
		minutes_df = minutes_df.drop_duplicates(['minutes', 'rss', 'loc'])
		max_rss_df = minutes_df.groupby('minutes').agg({'rss': 'max'})
		minutes_df = pd.merge(max_rss_df, minutes_df, on=['minutes', 'rss'], how='left')
		minutes_df['date'] = minutes_df['minutes'].str.slice(0, 8)
		minutes_df['hour'] = minutes_df['minutes'].str.slice(8, 10)
		minutes_df = minutes_df.drop('minutes', axis=1)
		pivot_df = pd.pivot_table(minutes_df, values='loc', index='date', columns='hour', aggfunc=' '.join, fill_value='')
		data = np.array([CountVectorizer().fit(AP_LOC_DICT.values()).transform(np.array(pivot_df)[i]).toarray() for i in range(pivot_df.shape[0])])
		# data = data.reshape(data.shape[0], -1)
		data = data.reshape(-1, data.shape[-1])
		label = KMeans(n_clusters=k, random_state=1993).fit_predict(data)
		# data = np.c_[data, label]
		data = pd.DataFrame(data)
		data['label'] = label
		dest_filename = '%s-k%s.csv' % (filename.split(".")[0], str(k))
		dest_path = os.path.join(DEST_DIR, dest_filename)
		data.to_csv(dest_path, index=False)
	except Exception as e:
		print("main error: %s" % e)

if __name__ == '__main__':
	try:
		main('000000000000.csv', k=9)
	except Exception as e:
		raise e