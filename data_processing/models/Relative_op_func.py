# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:53:53 2019

@author: ynie
"""


# coding: utf-8

# In[1]:

from math import *
import datetime
import numpy as np
import calendar

def inputs_for_rel_op(date_and_time):
    """
    Takes a single datetime.datetime as input. 
    Returns two values: 1st being day of year
    and 2nd being time of day solely in seconds-24 hr clock.
    """
    # Time correction. The center of PST is -120 W, while the logitude of the PV array is about 2 degree west of PST center
    
    pst_center_longitude = -120 # minus sign indicate west longitude
    panel_longitude = -122.174199 # minus sign indicate west longitude
    correction = np.abs(60/15*(panel_longitude - pst_center_longitude))
    min_correction = int(correction) # Local time delay in minutes from the PST
    sec_correction = int((correction - min_correction)*60)  # Local time delay in seconds from the PST
    if date_and_time.minute<=min_correction:
        date_and_time= date_and_time.replace(hour = date_and_time.hour-1, minute=60+date_and_time.minute-min_correction-1, second=60-sec_correction)
    else:
        date_and_time = date_and_time.replace(minute=date_and_time.minute-min_correction-1, second=60-sec_correction)
    
    time_of_day=date_and_time.hour * 3600 + date_and_time.minute * 60 + date_and_time.second
    
    # Following piece of code calculates day of year
    months=[31,28,31,30,31,30,31,31,30,31,30,31] # days in each month
    if (date_and_time.year % 4 == 0) and (date_and_time.year % 100 != 0 or date_and_time.year % 400 ==0 ) == True:
        months[1]=29 # Modification for leap year
    day_of_year=sum(months[:date_and_time.month-1])+date_and_time.day
    
    # Fix for daylight savings (NOTE: This doesn't work for 1st hour of each day in DST period.
    
    # which day of year is the 2nd Sunday of March in that year
    dst_start_day = sum(months[:2]) + calendar.monthcalendar(date_and_time.year,date_and_time.month)[1][6] 
    # which day of year is the 1st Sunday of Nov in that year 
    dst_end_day = sum(months[:10]) + calendar.monthcalendar(date_and_time.year,date_and_time.month)[0][6]
    if day_of_year >= dst_start_day and day_of_year < dst_end_day:
        time_of_day=time_of_day-3600
    
    return day_of_year, time_of_day
    #return day_of_year, time_of_day, date_and_time

def Relative_output(times,PV_ops):
    """
    Takes 2 inputs, 1st being single datetimes (e.g., Timestamp('2017-03-02 08:00:00')) 
    and 2nd being single PV output at those date and times.
    Returns a corresponding theoretical and relative PV output. 
    """
    
    # Constants
    P0=1  # Solar energy incident on Earth's surface=1 kW/m2
    A_eff=24.9842 # Effective area covered by panels in m2
    epsilon=radians(22.5) # Elevation angle of solar panel
    zeta=radians(195) # Azimuth angle of solar panel
    latitude=radians(37.424107) # Latitudinal co-ordinate of Stanford
    
    day_of_year, time_of_day=inputs_for_rel_op(times)
    # Calculating parameters dependent on time, day and location
    alpha=2*pi*(time_of_day-43200)/86400 # Hour angle in radians
    delta=radians(23.44*sin(radians((360/365.25)*(day_of_year-80)))); # Solar declination angle
    chi=acos(sin(delta)*sin(latitude)+cos(delta)*cos(latitude)*cos(alpha))# Zenith angle of sun
    tan_xi=sin(alpha)/(sin(latitude)*cos(alpha)-cos(latitude)*tan(delta)) # tan(Azimuth angle of sun,xi)
    if alpha>0 and tan_xi>0:
        xi=pi+atan(tan_xi)
    elif alpha>0 and tan_xi<0:
        xi=2*pi+atan(tan_xi)
    elif alpha<0 and tan_xi>0:
        xi=atan(tan_xi)
    else:
        xi=pi+atan(tan_xi)
    # Calculating theoretical output
    P_theo=P0*A_eff*(cos(epsilon)*cos(chi)+sin(epsilon)*sin(chi)*cos(xi-zeta))
    # To deal with troublesome cases
    if P_theo<0.05:
        P_theo=0.05
    if PV_ops<0.05:
        PV_ops=0.05              
    Rel_PV_op=PV_ops/P_theo
    if Rel_PV_op>1.5:
        Rel_PV_op=1.5
    
    return Rel_PV_op, P_theo

def Solar_angle(times):
    latitude=radians(37.424107) # Latitudinal co-ordinate of Stanford
    day_of_year, time_of_day=inputs_for_rel_op(times)
    # Calculating parameters dependent on time, day and location
    alpha=2*pi*(time_of_day-43200)/86400 # Hour angle in radians
    delta=radians(23.44*sin(radians((360/365.25)*(day_of_year-80)))); # Solar declination angle
    chi=acos(sin(delta)*sin(latitude)+cos(delta)*cos(latitude)*cos(alpha))# Zenith angle of sun
    tan_xi=sin(alpha)/(sin(latitude)*cos(alpha)-cos(latitude)*tan(delta)) # tan(Azimuth angle of sun,xi)
    if alpha>0 and tan_xi>0:
        xi=pi+atan(tan_xi)
    elif alpha>0 and tan_xi<0:
        xi=2*pi+atan(tan_xi)
    elif alpha<0 and tan_xi>0:
        xi=atan(tan_xi)
    else:
        xi=pi+atan(tan_xi)
    
    return degrees(xi), degrees(chi)