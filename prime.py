#!/usr/bin/python

#This script will evaluate if a given number is prme or not

num=7

if (num>1):
	for i in range (2,num):
		if (num%i)==0:
			print(num,"is not a prime number")
			break
	else:
		print(num," is a prime number")
else:
	print(num," is not a prime number")

