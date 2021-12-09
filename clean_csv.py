import csv

def parse_promo(entry):
    if entry:
        return str(int(entry[:4])-1)
    return ''

def parse_birth(entry : str):
    if entry:
        numbers = [int(a) for a in entry.strip().split("/")]
        return f"{numbers[1]:02d}{numbers[0]:02d}{numbers[2]}"
    return ""

def clean(s:str):
    r = s.replace("é", "e")
    r = r.replace("è", "e")
    r = r.replace("ï", "i")
    r = r.replace("ï", "i")
    r = r.replace("É", "e")
    r = r.replace("ô", "o")
    r = r.replace(" ", "-")
    r = r.replace("ç", "c")
    return r

with open("PT.csv", 'r') as f1, open("PT_clean.csv", 'w') as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)
    for row in reader:
        print(row)
        if row[0] and row[0][0]!='2':
            continue
        nom = clean(row[2].strip()).capitalize().replace(' ', '-')
        prenom = clean(row[3].strip()).capitalize().replace(' ', '-')
        promo = parse_promo(row[0])
        birth = parse_birth(row[4])
        writer.writerow([nom, prenom, promo, birth])