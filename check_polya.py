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

def get_polya_count(feature) -> int:
    polya_count = 0
    match_pattern = r'A{8,}'
    start = int(feature.location.start)
    end = int(feature.location.end)
    if start >= 100:
        if feature.location.strand == 1:
            upstream_sequence = sequence[(start - 100): (start)]
        elif feature.location.strand == -1:
            upstream_sequence = sequence[(end): (end + 100)].reverse_complement()
        polya_count = len(re.findall(match_pattern, str(upstream_sequence)))
    return polya_count

for i in range(1, (sum(1 for _ in SeqIO.parse(fasta_file, "fasta")) + 1)):
    sequence = read_fasta(fasta_file, i)
    gb_features = read_genbank(genbank_file, i)
    for feature in gb_features:
        if feature.type == "CDS":
            polya_count += get_polya_count(feature)
            if int(feature.location.start) >=100:
                region_count += 1

print(f"{polya_count},{region_count}")
