from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt 

data=np.genfromtxt("dollar_inflation.csv", delimiter=";", skip_header=(1), usecols=(0,3))
KM=KMeans(n_clusters=5,random_state=False)
KM.fit(data)
outKM=KM.labels_
print("CLuster : ","\n",outKM)
print("Centroid: ","\n",KM.cluster_centers_)
fig, axs= plt.subplots(2)
plt.suptitle("Before and After Clustering")
axs[0].scatter(data[:,0],data[:,1])
axs[0].set_ylabel("Inflation")
axs[1].scatter(data[:,0],data[:,1],c=outKM)
axs[1].set_ylabel("Inflation")
axs[1].set_xlabel("Years")
plt.show()