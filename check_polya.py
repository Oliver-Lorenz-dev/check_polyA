#!/usr/bin/env python3

import sys
import re

from Bio import SeqIO
from Bio.Seq import Seq

region_count = 0
polya_count = 0
fasta_file = sys.argv[1]
genbank_file = sys.argv[2]


def read_fasta(fasta_file: str, contig_num: int) -> str:
    i = 1
    if contig_num == 1:
        with open(fasta_file) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                return record.seq
    else:
        with open(fasta_file) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                if i == contig_num:
                    return record.seq
                i += 1


def read_genbank(genbank_file: str, contig_num: int) -> list:
    i = 1
    if contig_num == 1:
        for record in SeqIO.parse(genbank_file, "genbank"):
            features = record.features
            return features
    else:
        for record in SeqIO.parse(genbank_file, "genbank"):
            if i == contig_num:
                features = record.features
                return features
            i += 1

def get_polya_count(feature, feature2) -> int:
    polya_count = 0
    match_pattern = r'A{8,}'
    start = int(feature.location.start)
    end = int(feature.location.end)
    next_start = int(feature2.location.start)
    if start >= 100:
        if feature.location.strand == 1:
            upstream_sequence = sequence[(start - 100): (start)]
        elif feature.location.strand == -1:
            upstream_sequence = str(sequence[(end): (next_start)].reverse_complement())
            print(upstream_sequence)
        polya_count = len(re.findall(match_pattern, str(upstream_sequence)))
    return polya_count


for i in range(1, (sum(1 for _ in SeqIO.parse(fasta_file, "fasta")) + 1)):
    sequence = read_fasta(fasta_file, i)
    gb_features = read_genbank(genbank_file, i)
    feature_counter = 0
    cds_features = list()
    # get cds features
    for feature in gb_features:
        if feature.type == "CDS":
            cds_features.append(feature)
    
    # check polya for cds features
    for feature in cds_features:
        if feature.location.start > 100:
            feature_counter += 1
            if feature_counter >= 2:
                # if gene on positive strand, check if previous gene end point is > 100 than this gene start point
                # only if this is the case check for polyA in 100bp upstream promoter region
                if feature.location.strand == 1:
                    start = int(feature.location.start)
                    end = int(feature.location.end)
                    prev_gene_end = cds_features[feature_counter - 1].location.end
                    if start - prev_gene_end > 100:
                        region_count += 1
                        polya_count += get_polya_count(feature, cds_features[feature_counter - 1])
                # if gene on reverse strand, check if next gene start point is > 100 than this gene start point
                # only if this is the case, rev comp then check for polyA in 100bp upstream promoter region
                else:
                    if feature_counter < (len(cds_features)-1):
                        start = int(feature.location.end)
                        end = int(feature.location.start)
                        prev_gene_start = cds_features[feature_counter + 1].location.start
                        if prev_gene_start - start > 100:
                            region_count += 1
                            print(start)
                            polya_count += get_polya_count(feature, cds_features[feature_counter + 1])


print(f"{polya_count},{region_count}")

#with open("test.fa", 'r') as f:
#    lines = f.readlines()
#        
#    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
#
#    query_sequence = 'AGTATACTTTTTTTTTTTAGTATTTCAA'
#    index  = sequence.find(query_sequence)
#
#    print(f"Match found: Start = {index}, End = {index + len(query_sequence) - 1}")