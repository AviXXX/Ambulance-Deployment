import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, kmeans, whiten
from sklearn.cluster import KMeans

'''f = open('LatitudeLongitudeChennai.txt', 'r+')
listLatLng = f.readlines()
f.close()'''

LL=[[0 for i in range(2)] for j in range(72)]
LL=np.genfromtxt('LatitudeLongitudeChennai.txt',dtype=float)

#coordinates=np.array(listLatLng)
#mat =np.matrix(coordinates)
print(LL)
'''LL= np.array([
           [ 44.968046, -94.420307],
           [44.33328, -89.132008],
           [33.755787, -116.359998],
           [33.844843, -116.54911],
           [44.92057, -93.44786],
           [44.240309, -91.493619],
           [44.968041, -94.419696],
           [44.333304, -89.132027],
           [33.755783, -116.360066],
           [33.844847, -116.549069],
           [44.920474, -93.447851],
           [44.240304, -91.493768]
           ])'''
x, y = kmeans2(whiten(LL), 10, iter = 10, minit='points')
#x, y = kmeans(whiten(LL), 10)
#x, y = kmeans2(whiten(LL), 10, iter = 10, minit='points')
#X = np.matrix(zip(coordinates))
#x, y = KMeans(n_clusters=2).fit(X)
#print(x)
#print()
print(y)
print(len(y))
#print(y[1])
plt.scatter(LL[:,0], LL[:,1], c=y);
plt.show()

f = open('chennai.txt', 'r+')
listOfPlaces = f.readlines()
f.close()

n=len(listOfPlaces)
print(n)

Region0=[]
Region1=[]
Region2=[]
Region3=[]
Region4=[]
Region5=[]
Region6=[]
Region7=[]
Region8=[]
Region9=[]
for i in range(72):
    if(y[i]==0):
        Region0.append(listOfPlaces[i])
    if(y[i]==1):
        Region1.append(listOfPlaces[i])
    if(y[i]==2):
        Region2.append(listOfPlaces[i])
    if(y[i]==3):
        Region3.append(listOfPlaces[i])
    if(y[i]==4):
        Region4.append(listOfPlaces[i])
    if(y[i]==5):
        Region5.append(listOfPlaces[i])
    if(y[i]==6):
        Region6.append(listOfPlaces[i])
    if(y[i]==7):
        Region7.append(listOfPlaces[i])
    if(y[i]==8):
        Region8.append(listOfPlaces[i])
    if(y[i]==9):
        Region9.append(listOfPlaces[i])

print(Region0)
with open('Region0.txt','w') as f:
    for item in Region0:
        f.write("%s" % item)
print(Region1)
with open('Region1.txt','w') as f:
    for item in Region1:
        f.write("%s" % item)
print(Region2)
with open('Region2.txt','w') as f:
    for item in Region2:
        f.write("%s" % item)
print(Region3)
with open('Region3.txt','w') as f:
    for item in Region3:
        f.write("%s" % item)
print(Region4)
with open('Region4.txt','w') as f:
    for item in Region4:
        f.write("%s" % item)
print(Region5)
with open('Region5.txt','w') as f:
    for item in Region5:
        f.write("%s" % item)
print(Region6)
with open('Region6.txt','w') as f:
    for item in Region6:
        f.write("%s" % item)
print(Region7)
with open('Region7.txt','w') as f:
    for item in Region7:
        f.write("%s" % item)
print(Region8)
with open('Region8.txt','w') as f:
    for item in Region8:
        f.write("%s" % item)
print(Region9)
with open('Region9.txt','w') as f:
    for item in Region9:
        f.write("%s" % item)
