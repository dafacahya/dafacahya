import numpy as np 
from sklearn.cluster import KMeans

data=np.genfromtxt("dollar_inflation.csv", delimiter=";", skip_header=1, usecols=(0,1,2,3))
data=data[~np.isnan(data).any(axis=1)]
KM=KMeans(n_clusters=5, max_iter=10000, random_state=False)
KM.fit(data)
print("Centroid : ", KM.cluster_centers_)
print("ClusterL : ", KM.labels_)
datalength=len(KM.labels_)
cluster=np.array((0,0,0,0,0))
dataReport=[]
for i in range (datalength):
    if (KM.labels_[i]==0):
        cluster[0]+=1
    if (KM.labels_[i]==1):
        cluster[1]+=1
    if (KM.labels_[i]==2):
        cluster[2]+=1
    if (KM.labels_[i]==3):
        cluster[3]+=1
    if (KM.labels_[i]==4):
        cluster[4]+=1
    dataReport.append([np.int32(i),KM.labels_[i]])

print("NCluster 1: ", cluster[0], "NCluster 2: ", cluster[1], "NCLuster 3: ", cluster[2],"NCLuster 4: ", cluster[3],"NCLuster 5: ", cluster[4])
np.savetxt("DataReportInflation.csv", dataReport, delimiter=",", fmt="%d,%d")