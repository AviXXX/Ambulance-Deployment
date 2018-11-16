# Ambulance-Deployment

## Deployment of a certain no of ambulance in a city considering the population density of the places.

This application helps in deploying a certain no of ambulance in a city or any region by considering the population
density of key places and distance bewtween them. This application also considers the road health which is derived by the 
type of roads connecting the key places.

### To run this application, one can follow the steps listed below. There are few pre-requisits.

## Pre-requisits:

### python-3

### google maps api key: enable distance matrix and geolocation api

## We have ran the application for chennai city.

Step 1: Fork the repo and create a local copy. 

Step 2: Open a terminal and cd to the repository

Step 3: Run the python cluster.py command. This will form the clustering of the chennai key places data.

Step 4: Run the python distance.py command by changing the region name every time. This will create the distance matrix
        for all the sub regions.
        
Step 5: Now run the python graphcenter.py command. This will generate the markers of all the places the ambulance 
        should be deloyed.
        
## Future Work:

There is a lot of improvements required in this application which will be done with time.

For any query plz mail to: avinash.kumar369@gmail.com
