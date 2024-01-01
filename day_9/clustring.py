from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
df = pd.read_csv("survey_lung_cancer.csv")
# df.head()

enc = LabelEncoder()
df['GENDER'] = enc.fit_transform(df['GENDER'])
df['LUNG_CANCER']= enc.fit_transform(df['LUNG_CANCER'])
print(df.head())


####Cluster

wcss=[]
for i in range(1,11):
    kmeans= KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,6))
plt.plot(range(1,11),wcss,marker='o',linestyle='-')
plt.show()