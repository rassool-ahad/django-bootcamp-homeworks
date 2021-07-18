#!/bin/bash
echo enter your file name:
read filename
if [[ -f $filename ]]
then 
	tail -10 $filename
else
	echo file dosent exist
fi	
