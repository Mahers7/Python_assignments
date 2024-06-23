import argparse
from Bio import SeqIO

def find_longest_repeated_subsequence(sequence):
    n = len(sequence)
    longest_dup = ""
    
    for i in range(n):
        for j in range(i + 1, n):
            lcs_temp = 0
            
            while j + lcs_temp < n and sequence[i + lcs_temp] == sequence[j + lcs_temp]:
                lcs_temp += 1
            
            if lcs_temp > len(longest_dup):
                longest_dup = sequence[i:i + lcs_temp]
    
    return longest_dup

def find_longest_gc_run(sequence):
    max_length = 0
    max_seq = ""
    current_length = 0
    current_seq = ""

    for base in sequence:
        if base in "GCgc":
            current_length += 1
            current_seq += base
        else:
            if current_length > max_length:
                max_length = current_length
                max_seq = current_seq
            current_length = 0
            current_seq = ""
    
    if current_length > max_length:
        max_length = current_length
        max_seq = current_seq

    return max_seq

def load_sequence_from_file(file_path):
    sequence = ""
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            sequence += str(record.seq)
        if not sequence:
            for record in SeqIO.parse(file_path, "genbank"):
                sequence += str(record.seq)
        if not sequence:
            raise ValueError("No sequences found in the file")
    except Exception as e:
        raise ValueError(f"Error reading file {file_path}: {e}")
    return sequence

def main():
    parser = argparse.ArgumentParser(description='Sequence Analysis Tool')
    parser.add_argument('file', help='Path to the input file (FASTA or GenBank format)')
    parser.add_argument('--duplicate', action='store_true', help='Find the longest duplicate sub-sequence')
    parser.add_argument('--gc_long', action='store_true', help='Find the longest GC combination sequence')

    args = parser.parse_args()

    try:
        sequence = load_sequence_from_file(args.file)
    except ValueError as e:
        print(e)
        return

    if args.duplicate:
        longest_dup = find_longest_repeated_subsequence(sequence)
        print(f"Longest duplicate sub-sequence: {longest_dup}")

    if args.gc_long:
        longest_gc_seq = find_longest_gc_run(sequence)
        print(f"Longest GC combination sequence: {longest_gc_seq}")

if __name__ == '__main__':
    main()