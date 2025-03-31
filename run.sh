#!/bin/bash

unzip -qq data.zip

echo "isolate,polya_count,promoter_region_count" > results.csv

for f in data/*.fna
do
  stem=$(echo $f | awk -F "/" '{ print $NF }' | awk -F ".fna" '{ print $1 }')
  polya_count=$(python check_polya.py $f data/${stem}.gbk)
  echo "${stem},${polya_count}" >> results.csv
done

rm -r data