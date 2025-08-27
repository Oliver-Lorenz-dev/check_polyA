# check_polyA
Python script which checks for polyA monomers 100bp upstream of CDS regions (AAAAAAAA)

## Description
This script checks sequences for polyA monomers 100bp upstream of CDS regions (AAAAAAAA)

The script will output a file called `polya_count.csv` which contains the polyA count for each isolate in `data.zip`

The `polya_count.csv` file follows the below format:
```csv
isolate,polya_count,promoter_region_count
4954-98,33,2255
```

The script also produces a file which contains the genbank records for each gene with a polyA monomer in the promoter region: `genes.csv`
The file format is as follows:
```csv
isolate,genbank_record
4954-98,{'gene': ['spxA2'], 'locus_tag': ['KKBGAPLG_00204'], 'inference': ['ab initio prediction:Prodigal:002006'], 'codon_start': ['1'], 'transl_table': ['11'], 'product': ['Transcriptional regulator SpxA2'], 'protein_id': ['Prokka:KKBGAPLG_00204'], 'translation': ['MIKIYTVSSCTSCKKAKTWLNAHQLSYKEQNLGKEGITREELLDILTKTDNGIASIVSSKNRYAKALGVDIEDLSVNEVLNLIMETPRILKSPILVDEKRLQVGYKEDDIRAFLPRSVRNVENAEARLRAAL']}
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
