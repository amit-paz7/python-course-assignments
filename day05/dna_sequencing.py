import sys
dna_sequence = sys.argv[1].upper()
valid_bases = ('A', 'C', 'T', 'G')
segments = []
current_segment = ""
for base in dna_sequence:
    if base in valid_bases:
        current_segment += base
    else:
        if current_segment:
            segments.append(current_segment)
            current_segment = ""
if current_segment:
    segments.append(current_segment)

print(f"Sequences containing only ACTG: {segments}")
sorted_segments = sorted(segments, key=len, reverse=True)
print(f"Sorted by length (descending): {sorted_segments}")
