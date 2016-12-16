from fsqCateog import *
from timeDetails import *
import csv
import os
dir = os.path.dirname(os.path.realpath('__file__'))
ipath= os.path.join(dir, 'data')
opath=os.path.join(dir, 'data/4h')
os.chdir(ipath)

#change this for specific setting
timeInterval=6

Borough_name = 'Manhattan'

file_name = Borough_name+'.csv'

colnames = ['User_ID', 'Venue_ID', 'Venue_category_ID', 'Venue_category_name', 'Latitude', 'Longitude',
            'Timezone_offset', 'UTC_time']
data = pandas.read_csv(file_name, names=colnames, low_memory=False)

categ_name = data.Venue_category_name.tolist()
utc_time = data.UTC_time.tolist()
latitude = data.Latitude.tolist()
longitude = data.Longitude.tolist()

if 'Venue_category_name' in categ_name:
    categ_name.remove('Venue_category_name')
if 'UTC_time' in utc_time:
    utc_time.remove('UTC_time')
if 'Latitude' in latitude:
    latitude.remove('Latitude')
if 'Longitude' in longitude:
    longitude.remove('Longitude')

found = 'false'
counter = 0
functionalRegions = ['Entertainment', 'Education', 'NightLife', 'Recreation', 'SocialServices',
           'Residence', 'Shopping', 'Traveling', 'Eating']
with open ('NYC_Zip_Codes_Manhattan.geojson', 'r') as geojson:
        js = json.load(geojson)

#Function uniqueZipCodes is to list all zipCodes within certain borough, I/P: Borough name.
def uniqueZipCodes(boroughname):
    zipCodes = []
    for feature in js['features']:
            borough = feature['properties']['borough']
            if borough == boroughname:
                postcode = feature['properties']['postalCode']
                if not zipCodes.__contains__(postcode):
                    zipCodes.append(postcode)
    return zipCodes

#Function functionalMatrix is to form the matrix for functional regions, I/P: Borough name. N.B: No temporal processing at the moment.
def functionalMatrix(boroughname):
    counter = 0
    zipCodesList = uniqueZipCodes(boroughname)
    w = functionalRegions.__len__()
    h = zipCodesList.__len__()
    finalMatrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for feature in js['features']:
            postcode = feature['properties']['postalCode']
            if postcode == zipCodesList[i]:
                polygon = shape(feature['geometry'])
                with open(boroughname+'.csv') as f:
                    f.next()
                    for line in f:
                        point = Point(float(longitude[counter]), float(latitude[counter]))
                        if polygon.contains(point):
                            cateog = activity_category_classification(categ_name[counter])
                            index = functionalRegions.index(cateog)
                            finalMatrix[i][index] = finalMatrix[i][index] + 1
                        counter += 1
                    counter = 0
    return finalMatrix

#Below function is for preprocessing the file for particular timespan
def functionalMatrixTemporal(boroughname, timespan):
    counter = 0
    zipCodesList = uniqueZipCodes(boroughname)
    w = functionalRegions.__len__()
    h = zipCodesList.__len__()
    finalMatrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for feature in js['features']:
            postcode = feature['properties']['postalCode']
            if postcode == zipCodesList[i]:
                polygon = shape(feature['geometry'])
                with open(boroughname+'.csv') as f:
                    f.next()
                    for line in f:
                        point = Point(float(longitude[counter]), float(latitude[counter]))
                        if polygon.contains(point):
                            TS = one_time_slot(utc_time[counter].split()[3])
                            if (TS==timespan):
                                cateog = activity_category_classification(categ_name[counter])
                                index = functionalRegions.index(cateog)
                                finalMatrix[i][index] = finalMatrix[i][index] + 1
                        counter += 1
                    counter = 0
    return finalMatrix

def matrixNormalization(mm):
    sumOneList = [0]*mm.__len__()
    for i in range(mm.__len__()):
        for j in range(mm[i].__len__()):
            sumOneList[i] = mm[i][j] + sumOneList[i]
        for j in range(mm[i].__len__()):
            if not sumOneList[i] == 0:
                mm[i][j] = float(mm[i][j])/float(sumOneList[i])
    return mm

def writeMatrixCSV(Matrix, fileName):
    with open(fileName, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(Matrix)

'''
#mm = functionalMatrix('Manhattan')
mm = functionalMatrixTemporal('Manhattan',11)
normalizedMatrix = matrixNormalization(mm)
writeMatrixCSV(normalizedMatrix,"output_22PM_23PM.csv")
'''


for i in range(timeInterval):
    mm = functionalMatrixTemporal('Manhattan',i)
    normalizedMatrix = matrixNormalization(mm)
    writeMatrixCSV(normalizedMatrix,"output_"+str(i)+".csv")


#Below, it is used only for printing all zip codes with Manhattan.

zipCodesList = uniqueZipCodes('Manhattan')
print zipCodesList
