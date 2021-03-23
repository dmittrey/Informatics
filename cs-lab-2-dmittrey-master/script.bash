#!/bin/bash
b=$2
a=$1
f=$(($a + $b)) 
c=$(($a - $b)) 
d=$(($a * $b)) 
if [[ $(($a * $b)) -lt 0 ]] 
then 
minus=-1
else
minus=1
fi
if [[ $a -lt 0 ]]
then 
a=$(($a * -1))
fi
if [[ $b -lt 0 ]]
then 
b=$(($b * -1))
fi
    e=$(($a / $b))
       if [[ $(($b * $a)) -ne 0 ]]
       then 
           e=$(($a / $b))
           ost1=$(($a % $b))
           m=0
           if [[ $ost1 -ne 0 ]]
           then
           while [[ $(($m / 10)) -eq 0 ]]
           do
              ost1=$(($ost1 * 10))
              m=$(($m * 10 + $ost1 / $b))
              ost1=$(($ost1 % $b))
           done
           else 
           m="00"
           fi
           if [[ $minus -lt 0 ]]
           then
           echo "$f $c $d -$e.$m"
           else 
           echo "$f $c $d $e.$m"
           fi
      elif [[ $b -eq 0 ]]
      then 
          echo "$f $c $d #"
      else
          echo "$f $c $d 0.00"
fi

