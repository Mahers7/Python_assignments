import os
import sys
import csv
from datetime import datetime
from Bio import Entrez

def download_ncbi_data(term, number):
    Entrez.email = "maher@salhab.com"  
    search_handle = Entrez.esearch(db="protein", term=term, retmax=number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    number_found = search_results["Count"]
    file_names = []
    
    for idx in ids:
        fetch_handle = Entrez.efetch(db="protein", id=idx, rettype="gb", retmode="text")
        data = fetch_handle.read()
        fetch_handle.close()
        
        file_name = f"{term}_{idx}.txt"
        with open(file_name, "w") as f:
            f.write(data)
        file_names.append(file_name)

    return file_names, number_found

def log_search(term, number, total):
    log_file = "search_log.csv"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.isfile(log_file):
        with open(log_file, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["date", "term", "max", "total"])

    with open(log_file, "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([current_time, term, number, total])
def main():
    if len(sys.argv) != 3:
        print("Usage: python ncbi.py TERM NUMBER")
        sys.exit(1)

    term = sys.argv[1]
    try:
        number = int(sys.argv[2])
    except ValueError:
        print("NUMBER must be an integer")
        sys.exit(1)

    file_names, total_found = download_ncbi_data(term, number)

    for file_name in file_names:
        print(file_name)

    log_search(term, number, total_found)

if __name__ == "__main__":
    main()