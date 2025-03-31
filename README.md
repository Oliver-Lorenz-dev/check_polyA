# check_polyA
Python script which checks for polyA monomers 100bp upstream of CDS regions (AAAAAAAA)

## Description
This script checks sequences for polyA monomers 100bp upstream of CDS regions (AAAAAAAA)

The script will output a file called `results.csv` which contains the polyA count for each isolate in `data.zip`

The `results.csv` file follows the below format:
```csv
isolate,polya_count,promoter_region_count
4954-98,33,2255
```

## Setup
Clone the repository and install the dependencies:
```shell
git clone https://github.com/Oliver-Lorenz-dev/check_polyA.git
cd check_polyA
python3 -m venv venv
source venv/bin/activate
pip install bio
```

## Run the script on the dataset
```shell
./run.sh
```

## Run the python script on individual samples
```shell
./check_polya.py <filename.fasta> <filename.gbk>
```