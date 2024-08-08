# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 02:20:04 2024

@author: Ace Stratton

Purpose: This script is designed to run the satellite through a series of
performance checks to ensure the health of all submodules 
"""
import sys
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace/Performance Check')
import OBC, time
from datetime import datetime



class TestOBC:
	
	
	def test_get_version(self):
		
		print("Getting OBC Version")
		version = OBC.getVersion()
		print(f"OBC Version: {version}")
		assert version != [99,99,99], "Version is invalid"
	
	def test_uptime_increase(self):
		
		print("Checking OBC UpTime Increase")
		up1 = OBC.getUptime()
		time.sleep(2)
		up2 = OBC.getUptime()
		result = up2-up1
		print(f"OBC Uptime Result: {result}")
		assert up2 > up1, "UpTime Did not increase"
		
	def test_obc_time(self):
		
		print("Checking OBC Time versus Computer OBC Time")
		obcTime = OBC.getTime()
		currentTime = datetime.now()
		
		OBCHr = obcTime[(0)]
		OBCMin = obcTime[(1)]
		OBCSec = obcTime[(2)]

		Hour = currentTime.hour
		Min = currentTime.minute
		Sec = currentTime.second

		checkTime = [Hour, Min, Sec]
		
		print(f"OBC Time: {OBCHr}:{OBCMin}:{OBCSec}")
		print(f"Computer RTC: {Hour}:{Min}:{Sec}")
		
		assert obcTime == checkTime, "OBC clock does not match computer RTC"
		
	def test_obc_date(self):
		
		print("Checking OBC date vs computer date")
		obcDate = OBC.getDate()
		currentDate = datetime.now()
		
		OBCDay = obcDate[(0)]
		OBCMon = obcDate[(1)]
		OBCYr = obcDate[(2)]
		
		Day = currentDate.day
		Mon = currentDate.month
		Yr = currentDate.year
		
		checkDate = [Day, Mon, Yr]
		
		print(f"OBC Date: {OBCDay}/{OBCMon}/{OBCYr}")
		print(f"Computer RTC Date: {Day}/{Mon}/{Yr}")
		
		assert obcDate == checkDate, "Date of OBC does not match computer RTC"
		
		
		


	
	