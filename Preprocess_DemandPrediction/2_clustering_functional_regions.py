# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:48:31 2016

perform clustering
"""

import pandas as pd
import os 
import glob
from sklearn import metrics
dir = os.path.dirname(os.path.realpath('__file__'))

ipath= os.path.join(dir, 'data/4h')
opath=os.path.join(dir, 'output/4h_clustering/')
os.chdir(ipath)

files=glob.glob('*.csv')
idx=range(1,(3*len(files))+1)
colName=['Algo','silhouette_score','num_of_clusters','fileName']
dfSum = pd.DataFrame(index=idx, columns=colName)

random_state=0
nrow=1
#clustering algo list, this can be extended for more clustering techniques
kmeans='Kmeans'
Spectral='Spectral'
Hierarchical='Hierarchical'

for f in files :
        df=pd.read_csv(f,header=None)
        df.index += 1 
        idx=range(1,len(df)+1)
        colName=[kmeans,Spectral,Hierarchical]
        dfRes = pd.DataFrame(index=idx, columns=colName)
        print '----------------------------------------------'
        print 'dealing with file:',f
        
                                            
        #Hierarchical clustering, suitable for large number of records
        from sklearn.cluster import AgglomerativeClustering  
        maxValue=0
        maxIdx=0
        for i in range(2,14): 
            clustering_hie=AgglomerativeClustering(linkage='ward', n_clusters=i,affinity="euclidean")  
            clustering_hie.fit(df) 
            labels_hie=clustering_hie.labels_ 
            performValue=metrics.silhouette_score(df, labels_hie, metric='euclidean')
            if (performValue>maxValue):
                maxValue=performValue
                maxIdx=i
                dfRes[Hierarchical]=labels_hie
            print 'k=',i,' performance=', performValue
        print 'Hierarchical clustering max performance value=', maxValue, ' max value index=',maxIdx
        dfSum['Algo'].ix[nrow]=Hierarchical
        dfSum['silhouette_score'].ix[nrow]=maxValue
        dfSum['num_of_clusters'].ix[nrow]=maxIdx
        dfSum['fileName'].ix[nrow]=f
        nrow=nrow+1  
        dfRes.set_index([range(0,106)])
        #pd.DataFrame.to_csv(dfRes, path='result/',f+'_(clusteringResult).csv') 
        frame=[dfRes,df]
        dfRes=pd.concat(frame, axis=1)
        
        pd.DataFrame.to_csv(dfRes,opath+f+'_(clusteringResult).csv')