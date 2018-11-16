#Define infinity as the large enough value
#import distance.py
import numpy as np
import gmplot
import googlemaps, gmplot, webbrowser, os, json

INF=99

locations=[]
#Class to Represent the Graph
#class Graph():
    #def __init__(self, Vertex):
    #    self.v=Vertex
    #    self.graph=[[0 for column in range(Vertex)] for row in range(Vertex)]

     #Solves all pair shortest path through Floyd Warshall algorithm
'''def All_Pair_Shortest_Path(self):
        """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """
        dist=[[0 for i in range(self.v)] for j in range(self.v)]
        for i in range(self.v):
            for j in range(self.v):
                dist[i][j]=self.graph[i][j]

        dist = map(lambda i : map(lambda j : j , i) , self)
        print(dist)
        #"""Add all vertices one by one to the set of intermediate vertices """
        for k in range(self.v):
            #pick all vertices as source one by one
            for i in range(self.v):
                # Pick all vertices as destination for the
                # above picked source
                for j in range(self.v):
                    dist[i][j] = min(dist[i][j] ,
                                  dist[i][k]+ dist[k][j]
                                )
                    #if(dist[i][k]+dist[k][j] < dist[i][j]):
                        #dist[i][j] = dist[i][k] + dist[k][j]
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    #dist[i][j]= min(dist[i][j], dist[i][k]+ dist[k][j] )
        print(dist)
        #self.printSolution(dist)
        return dist'''
def floydWarshall(graph,V):
    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph))
    #print(dist)
    #print("\n\n")
    for k in range(V):
            # pick all vertices as source one by one
        for i in range(V):
                # Pick all vertices as destination for the
                # above picked source
            for j in range(V):
                if(dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                #dist[i][j] = min(dist[i][j] ,
                #              dist[i][k]+ dist[k][j]
                    #        )
    #print(dist)
    return(dist)


    #A utility function to print all pair shortest path
'''def printSolution(self,dist):
        print('Following matrices showing shortest distance between every pair of verices \n')
        for i in range(self.v):
            for j in range(self.v):
                if(dist[i][j]==INF):
                    print("%7s"%("INF"),)
                else:
                    print("%7.2f\t"%(dist[i][j]),)
            print("\n")'''
    #Function to find the Median of Graph
def Graph_Center(A,V, place):
        #sum(i)-sum of length of shortest path from i to all other vertices
        #sum=[0]*self.v
    sum=65535
    temp=0
    loc=0
    #print(A)
    for i in range(V):
            #if(V[i]==True):
                #sum[i]=0
        #print("Inside center")
        temp=0
        for j in range(V):
            temp=temp+A[i][j]
        #print(temp," ",sum)

        if(temp < sum):
            #print("Inside if")
            sum=temp
            #print("\n\n Sum:")
            #print(sum)
            center=i
            loc=i
                    #if(i !=j):
                    #    sum[i]=sum[i]+A[i][j]
        #print("Region : %d ----- sum %7.2f" %(i))

    #print("Region : %d " %(loc))
            #else:
                #sum[i]=INF
    PLACE=[0 for i in range(V)]
    f = open(place , 'r+')
    PLACE = f.readlines()
    f.close()
    location=PLACE[loc]
    print(location)
    locations.append(location)
    #plotLocation(location)
         #median=0
        #arr=[None]*self.v
        #arr=module1.lis
        #for  k in range(self.v):
        #    if(sum[k]<sum[median]):
        #        median=k
    #    print("Median of the Graph is the Region : ",median, arr[median])
    #    print("Total Sum is : ",sum[median])

#Driver Program to plot location on google map
def plotLocation():
    # GoogleMapPlotter return Map object
    # Pass the center latitude and
    # center longitude
    gmaps = googlemaps.Client(key='')
    latlng=[[0 for i in range(2)] for j in range(10)]
    for i in range(10):
        x=locations[i]
        geocode_result = gmaps.geocode(x)
        #gmap1 = gmplot.GoogleMapPlotter.from_geocode("Surathkal")
        geom = geocode_result[0]['geometry']
        loc = geom['location']
        lat = loc['lat']
        lng = loc['lng']
        latlng[i][0]=lat
        latlng[i][1]=lng

        gmap = gmplot.GoogleMapPlotter(lat, lng, 13)
        hidden_gem_lat, hidden_gem_lon = lat,lng
        gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

    a=np.array(latlng)
    mat =np.matrix(a)
    with open('LatLangFinal.txt','wb') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%.8f')
    print(latlng)
    # Draw
    #gmap.draw("my_map.html")

    filename = 'file:///'+os.getcwd()+'/' + 'plot.html'
    webbrowser.open_new_tab(filename)
    # Pass the absolute path
    #gmap1.draw( "home\map11.html" )'''

    print(locations)



def calculate (n, path, roadhealth, population, place):
    WC=[[0 for i in range(n)] for j in range(n)]
    #g=Graph(n)
    #g.graph=module1.dist
    #g.graph=[[0,2,INF,6,INF],
      #              [2,0,3,8,5],
      #              [INF,3,0,INF,7],
        #            [6,8,INF,0,9],
         #          [INF,5,7,9,0]]

    PC=[[0 for i in range(n)] for j in range(n)]
    #PC=distance.dist
    PC=np.genfromtxt(path ,dtype=int)
    #PC= distance.dist

    '''print(PC)
    a=np.array(PC)
    mat =np.matrix(a)
    with open('outfile.txt','wb') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%d')'''

    #PLACE=[0 for i in range(n)]
    #f = open('surathkal.txt', 'r+')
    #PD = f.readlines()
    #f.close()

    RH=[[0 for i in range(n)] for j in range(n)]
    RH=np.genfromtxt(roadhealth,dtype=int)
    #print(RH)
    PD=[0 for i in range(n)]
    f = open(population, 'r+')
    PD = f.readlines()
    f.close()
    #PD=np.genfromtxt('population.txt',dtype=int)
    TPP=0
    for k in range(n):
        #x = PD[i]
        #print(x)
        PD[k]=int(PD[k])
        TPP=TPP + PD[k]
    for i in range(n):
        for j in range(n):
            if(PC[i][j] <= INF and PC[i][j]!=0):
                #print(PC[i][j])
                WC[i][j]=(PC[i][j]+RH[i][j])*(TPP/(PD[i]+PD[j]))/10
            elif(PC[i][j] >= INF and PC[i][j]!=0):
                WC[i][j]=INF
            elif(PC[i][j]==0):
                WC[i][j]=0
			    #print(WC)
    #g= Graph(n)
    #g.graph = WC
    #print(WC)
    A=floydWarshall(WC,n)
    #print(A)
    #flag=int(input("Select wether there exist a warehouse in the city or not if exist then Enter Flag val as 1 otherwise as 0 :"))
    #if(flag==0):
    Graph_Center(A,n, place)
    '''else:
        v=int(input("Enter the index of the Region :"))
        V[v]=False
        Radius=20
        #Make all the Reachable region as dead if it is within the Radius
        for i in range(n):
            if(A[v][i]<=Radius):
                V[i]=False
        g.Graph_Median(A,V)'''



#Driver Program to test the above function
if(__name__=='__main__'):
    #p=module1.n
    #print('Given no of region in the city is :',p)
    #n=72
    #n=int(input("Enter no of Regions : "))
    #initially mmake all the regions as true i.e the city is applicable for establishing warehouse
    #V=[True]*n
    #length of shortest path from vertex i to j
    for k in range(10):
        if(k==0):
            calculate(5, 'pathRegion0.txt', 'roadhealth0.txt', 'population0.txt', 'Region0.txt')
        if(k==1):
            calculate(5, 'pathRegion1.txt', 'roadhealth1.txt', 'population1.txt', 'Region1.txt')
        if(k==2):
            calculate(10, 'pathRegion2.txt', 'roadhealth2.txt', 'population2.txt', 'Region2.txt')
        if(k==3):
            calculate(6, 'pathRegion3.txt', 'roadhealth3.txt', 'population3.txt', 'Region3.txt')
        if(k==4):
            calculate(8, 'pathRegion4.txt', 'roadhealth4.txt', 'population4.txt', 'Region4.txt')
        if(k==5):
            calculate(10, 'pathRegion5.txt', 'roadhealth5.txt', 'population5.txt', 'Region5.txt')
        if(k==6):
            calculate(5, 'pathRegion6.txt', 'roadhealth6.txt', 'population6.txt', 'Region6.txt')
        if(k==7):
            calculate(6, 'pathRegion7.txt', 'roadhealth7.txt', 'population7.txt', 'Region7.txt')
        if(k==8):
            calculate(7, 'pathRegion8.txt', 'roadhealth8.txt', 'population8.txt', 'Region8.txt')
        if(k==9):
            calculate(10, 'pathRegion9.txt', 'roadhealth9.txt', 'population9.txt', 'Region9.txt')

    plotLocation()
