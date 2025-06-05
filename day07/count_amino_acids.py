import sys
from collections import Counter # Useful for counting

codon_table_from_exercise = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

codon_to_amino_acid = {}
for amino_acid, codons_list in codon_table_from_exercise.items():
    for codon in codons_list:
        codon_to_amino_acid[codon.upper()] = amino_acid
print("Map built successfully.\n")

if len(sys.argv) < 2:
    print("Oops! You need to tell me which file contains the DNA sequence.")
    print("For example: python count_amino_acids.py your_dna_sequence.txt")
    print("Or: python count_amino_acids.py your_sequence.fasta")
    sys.exit() 

dna_file_path = sys.argv[1]

raw_file_content = ""
try:
    print(f"Reading DNA sequence from: {dna_file_path}")
    with open(dna_file_path, 'r') as file:
        raw_file_content = file.read()
except FileNotFoundError:
    print(f"Oh no! I couldn't find the file: {dna_file_path}")
    print("Please check if the name and path are correct.")
    sys.exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit()

print("Cleaning and preparing DNA sequence...")
dna_sequence = ""
for character in raw_file_content.upper():
    if character in "ACTG":
        dna_sequence += character

if not dna_sequence:
    print("The file didn't seem to contain any valid DNA bases (A, C, T, G).")
    sys.exit()

if len(dna_sequence) < 3:
    print(f"The DNA sequence ('{dna_sequence}') is too short to form any codons (need at least 3 bases).")
    sys.exit()

print(f"Found {len(dna_sequence)} DNA bases to analyze.\n")

amino_acid_counts = Counter() 
unrecognized_codons_count = 0
total_codons_processed = 0

end_of_full_codons = len(dna_sequence) - (len(dna_sequence) % 3)

for i in range(0, end_of_full_codons, 3):
    codon = dna_sequence[i:i+3] # Get a 3-base codon
    total_codons_processed += 1
    
    if codon in codon_to_amino_acid:
        amino_acid = codon_to_amino_acid[codon]
        amino_acid_counts[amino_acid] += 1
    else:
        print(f"Warning: Encountered an unrecognized or unexpected codon: '{codon}'")
        unrecognized_codons_count += 1

if not amino_acid_counts and unrecognized_codons_count == 0:
    print("No codons were processed or no amino acids were identified.")
else:
    print("\n--- Amino Acid Counts ---")
    
    max_name_length = 0
    if amino_acid_counts: # Check if there are any counts to process
         # Also consider "STOP" if it's in the counts
        all_counted_items = list(amino_acid_counts.keys())
        for name in all_counted_items:
            if len(name) > max_name_length:
                max_name_length = len(name)
    if max_name_length < 4: # Ensure at least a little space, e.g. for "STOP" or "Name"
        max_name_length = 4

    for name, count in sorted(amino_acid_counts.items()):
        print(f"{name:<{max_name_length}}  {count}")

    if unrecognized_codons_count > 0:
        print(f"\nAdditionally, {unrecognized_codons_count} codon(s) were unrecognized.")

leftover_bases_count = len(dna_sequence) % 3
if leftover_bases_count > 0:
    bases_str = dna_sequence[end_of_full_codons:]
    print(f"\nNote: {leftover_bases_count} base(s) ('{bases_str}') at the end of the sequence did not form a complete codon and were ignored.")

print(f"\nTotal codons considered from sequence: {total_codons_processed}")
print("Processing complete.")
