#!/usr/bin/python
#_*_ coding:utf-8 _*_

from pandas import DataFrame

def get_num_attribution(path):

    phnumbers=[]
    cities=[]
    provinces=[]

    #open file and read imformation about phone number and attribtuion
    data_file=open(path,'r')                               

    for line in data_file:

        phnumber,province,city=line.split(",")
        phnumbers.append(phnumber)    
        cities.append(city[:-1])
        provinces.append(province)

    data_file.close() 

    #put three lists in dict num_place
    num_place = {"provinces":provinces,"cities":cities,"phnumbers":phnumbers}     

    #dict num_place change into dataframe 
    frame = DataFrame(num_place)                              

    return frame

