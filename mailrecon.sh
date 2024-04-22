#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    echo "mailrecon [list of mail domain] [output folder]"
    exit
fi

target=$1
sav=${2}/

if [ ! -d ${sav} ]; then
  mkdir -p ${sav}
fi


echo =========== script started ===========

for i in $(cat $target);
do

	emailfinder -d ${i} | grep ${i} > ${sav}emailfinder-${i}
	python3 EmailHarvester.py -s ${sav}emailharvester-${i} -d ${i} 
	crosslinked -f '{first}{l}@${1}' -o ${sav}CLfirstl-${i} ${i}
	crosslinked -f '{f}{last}@${1}' -o ${sav}CLflast-${i} ${i}
	crosslinked -f '{first}.{last}@${1}' -o ${sav}CLfirst.last-${i} ${i}
	crosslinked -f '{first}_{last}@${1}' -o ${sav}CLfirst_last-${i} ${i}

	python3 email-format.py ${i} > ${sav}emailformat-${i}
	python3 intelxEmail.py ${i} > ${sav}intelxEmail-${i}

	cat ${sav}emailfinder-${i}  ${sav}emailharvester-${i} ${sav}CLfirstl-${i}.txt   ${sav}CLflast-${i}.txt ${sav}CLfirst.last-${i}.txt ${sav}CLfirst_last-${i}.txt ${sav}emailformat-${i} ${sav}intelxEmail-${i} | sort -u | grep ${i} > ${sav}total-${i}

done

echo =========== script done ===========


#more mail format can search in google : [target] mail format rocketreach
