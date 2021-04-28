import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
tsne = TSNE(n_components=2, random_state=10)


X = np.loadtxt('test.out')
print(X)
X = StandardScaler().fit_transform(X)
tsne_obj= tsne.fit_transform(X)

db = DBSCAN(eps=4, min_samples=6).fit(tsne_obj)

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels))
print(np.sort(labels))
n_noise_ = list(labels).count(-1)
colors=['purple','red','orange','brown','blue',
                       'dodgerblue','green','lightgreen','darkcyan', 'black']
tsne_df = pd.DataFrame({'X':tsne_obj[:,0],
                        'Y':tsne_obj[:,1],
                        'digit':labels})

print(tsne_df.head(5))

sns.scatterplot(x='X', y='Y', data=tsne_df, palette=colors[0:n_clusters_], legend='full', hue='digit')
plt.show()

