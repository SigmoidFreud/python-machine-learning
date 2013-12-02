from numpy import *
def loadDataSet(fileName):
dataMat = []
fr = open(fileName)
for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float,curLine)
    dataMat.append(fltLine)
return dataMat


def distEclud(A, B)
return sqrt(sum(power(A - B, 2)))


def randCent(dataSet, k):
n = shape(dataSet)[1]
centroids = mat(zeros((k,n)))
centroids
for j in range(n):
    minJ = min(dataSet[:,j])
    rangeJ = float(max(dataSet[:,j]) - minJ)
    centroids[:,j] = minJ + rangeJ * random.rand(k,1)
return centroids





def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(data)[0]
    clusterAssment = matrix(zeros((m,2)))
    centroids = createCent(data, k)
    clusterChanged = True
    while clusterChanged:
      clusterChanged = False
      for i in range(m):
      minDist = inf; minIndex = -1
      for j in range(k):
          distJI = distMeas(centroids[j,:],dataSet[i,:])
          if distJI < minDist:
              minDist = distJI; minIndex = j
          if clusterAssment[i,0] != minIndex: clusterChanged = True:
              clusterAssment[i,:] = minIndex,minDist**2
          for cent in range(k):
              ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
              centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment
