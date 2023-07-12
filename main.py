#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:39:59 2023

@author: yacoub
"""
from datetime import datetime, timedelta,date

from Update_WTH import *
from CHIRPS import *
from GetNassaP import *
from Dssat_WTH import *
#s1 = datetime.now()


# Définissez la classe main
class main:
    def download(self, in_file, startDate, endDate, out_dir):
        dssat_wth(in_file, startDate, endDate, out_dir)
    
    def Update(self, in_file,in_dir, out_dir):
        update_wth(in_file, in_dir, out_dir)

# Créez une instance de la classe main
m = main()

in_dir=out_dir = "/Users/yacoub/Desktop/UF/spyder/WTH_Files/temp/NasaChirps_DATA/"
out_dir2 = "/Users/yacoub/Desktop/UF/spyder/WTH_Files/temp/NasaChirps_DataUpdate/"

in_file="/Users/yacoub/Desktop/UF/spyder/WTH_Files/Input.csv"
startDate = 20220501
endDate = 20221231


# Appelez la méthode download() avec les valeurs spécifiées
m.download(in_file, startDate, endDate, out_dir)
m.Update(in_file,out_dir, out_dir2)
