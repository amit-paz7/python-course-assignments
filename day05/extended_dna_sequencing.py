sequence = input("Please type in a sequence: ").upper()
valid_bases = ('A', 'C', 'T', 'G')
segments = []
current_segment = ""
for base in sequence:
    if base in valid_bases:
        current_segment += base
    else:
        if current_segment:
            segments.append(current_segment)
            current_segment = ""
if current_segment:
    segments.append(current_segment)

final_segments = []
for segment in segments:
    sub_segment = ""
    for base in segment:
        sub_segment += base
        if len(sub_segment) > 0 and (len(sub_segment) == len(segment) or segment[segment.index(base) + 1] not in valid_bases if segment.index(base) + 1 < len(segment) else True):
            final_segments.append(sub_segment)
            sub_segment = ""
    if sub_segment: # Handle any remaining bases
        final_segments.append(sub_segment)

final_segments = [seg for seg in final_segments if seg]
sorted_final_segments = sorted(final_segments, key=len, reverse=True)
print(f"Expected output: {sorted_final_segments}")
