#!/bin/bash
#$ -v LD_LIBRARY_PATH=/mnt/storage/home/egg/Tools/locarna/lib
#$ -l mem_free=4G
#$ -pe para 5
#$ -v PATH=/mnt/storage/home/egg/Tools/bin:/mnt/storage/home/egg/Tools/clustalo/bin:/mnt/storage/home/egg/Tools/ViennaRNA/bin:/mnt/storage/home/egg/Tools/locarna/bin:/mnt/storage/home/egg/Tools/infernal/bin:/mnt/storage/home/egg/.cabal/bin:/usr/bin/:/bin/:$PATH
RNAlien -i /mnt/storage/tmp/rnalien/cm18693/input.fa -c 5  -d cm18693 -o /mnt/storage/tmp/rnalien/ > /mnt/storage/tmp/rnalien/cm18693/Log
Ids2Tree -l 6 -f json -i /mnt/storage/data/rnalien/ -o /mnt/storage/tmp/rnalien/cm18693/ -r /mnt/storage/tmp/rnalien/cm18693/result.csv
cp /mnt/storage/tmp/rnalien/cm18693/result.cm  /mnt/storage/tmp/cmcws/upload/cm18693 
if [ -e /mnt/storage/tmp/rnalien/cm18693/evaluation/result.clustal.selected ]; then
(cd /mnt/storage/tmp/rnalien/cm18693/evaluation/ && RNAalifold --color result.clustal.selected )
fi
gs -sDEVICE=jpeg -dJPEGQ=100 -dNOPAUSE -dBATCH -dSAFER -r300 -sOutputFile=/mnt/storage/tmp/rnalien/cm18693/alirna.jpg /mnt/storage/tmp/rnalien/cm18693/evaluation/alirna.ps
zip -9 -r /mnt/storage/tmp/rnalien/cm18693/result.zip /mnt/storage/tmp/rnalien/cm18693/
date -r /mnt/storage/tmp/rnalien/cm18693/0 > /mnt/storage/tmp/rnalien/cm18693/starttime 
date -r /mnt/storage/tmp/rnalien/cm18693/result.zip > /mnt/storage/tmp/rnalien/cm18693/endtime 
