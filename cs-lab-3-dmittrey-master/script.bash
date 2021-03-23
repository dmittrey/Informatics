#!/usr/bin/bash
export LANG=en_US.UTF8
export LC_ALL=en_US.UTF8
func() {
fil=$(($fil+1))

local tab=""
for (( i=1;i<$1;i++ ))
do
local tab="$tab\u2502\u00A0\u00A0\u0020"
done



if [ "$2" = "" ]
then
	printf "$tab$2$3"
else
	printf "\n$tab$2$3"
fi

if $(cd $3 2> /dev/null)
then
pap=$(($pap+1))

cd $3

local array=($(ls))

if [[ ${#array[@]} -ne 0 ]] 
then
	for i in ${array[@]}
		do
	local len=${#array[@]}
	local index=$(( $len-1 ))
		if [ "$i" = "${array[$index]}" ]
		then
			if [ "$2" = "└── " ]
			then
			func $(($1)) "    └── " $i
			else
			func $(($1+1)) "└── " $i
			fi
		else
			if [ "$2" = "└── " ]
			then
			func $(($1)) "    ├── " $i
			else
			func $(($1+1)) "├── " $i
			fi
		fi
		done
	cd ..
fi
fi
}
fil=0
pap=0
if $(cd $1 2> /dev/null)
then 
key=1
else 
key=0
fi


if [ "$1" = "" ]
then
func 0 "" . $fil $pap
pap=$(($pap-1))
else
func 0 "" $1 $fil $pap
fi

printf "\n\n"

if [[ key -eq 1 ]]
then
pap=$(($pap-1))

fi

if [[ $pap -eq -1 ]]
then 
$pap=0
fi

if [[ $fil -lt 0 ]]
then 
$fil=0
fi
if [[ $pap -eq 1 && $fil -eq 1 ]]
then
	echo "1 directory, 1 file"
elif [[ $pap -eq 1 ]]
then 
	echo "1 directory, $(($fil-$pap-1)) files"
elif [[ $(($fil-$pap-1)) -eq 1 ]]
then
	echo "$pap directories, 1 file"
else
echo "$pap directories, $(($fil-$pap-1)) files"
fi

