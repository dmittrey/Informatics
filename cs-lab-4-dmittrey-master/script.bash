#!/bin/bash
BPing(){
if ping -c 1 $1 1> /dev/null 2> /dev/null
then 
	echo "HOST IS UP"
else 
	echo "HOST IS DOWN"
fi	
}
for i in $@
do
BPing $i
done
