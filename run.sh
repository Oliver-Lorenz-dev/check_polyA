#!/bin/bash

unzip -qq data.zip

echo "isolate,polya_count,promoter_region_count" > results.csv

for f in data/*.fna
do
  stem=$(echo $f | awk -F "/" '{ print $NF }' | awk -F ".fna" '{ print $1 }')
  python check_polya.py $f data/${stem}.gbk | while read line; do sed "s|^|${stem},|g"; done >> results.csv
done

tail -n +2 results.csv | awk -F, '($2 ~ /^[0-9]+$/ && $3 ~ /^[0-9]+$/) {print >> "polya_count.csv"; next} {print >> "genes.csv"}'

sed -i '1s/^/isolate,polya_count,promoter_region_count\n/' polya_count.csv

grep ",{" genes.csv > tmp
mv tmp genes.csv

sed -i '1s/^/isolate,genbank_record\n/' genes.csv

rm -r data
