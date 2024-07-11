                        # rogor davprintot age of girls

def get_age(age):
    
    return int(age[0])

# Example usage:
print(get_age("1 year old"))  #1
print(get_age("9 years old")) #9


                            # sityvebis/aoebis chanacvleba function  
def dna_to_rna(dna):
    return dna.replace('T', 'U')

# Example usage:
print(dna_to_rna("GCAT"))       #"GCAU"
print(dna_to_rna(""))           #""
print(dna_to_rna("TCGCGCT"))    #"UCGCGCU"

                            # day month year datetime 
from datetime import datetime

def is_today(date):
    today = datetime.today()
    
    
    return date.year == today.year and date.month == today.month and date.day == today.day

# Examples
print(is_today(datetime(2024, 7, 5)))  #True
print(is_today(datetime(2023, 7, 5)))  #False
print(is_today(datetime(2024, 7, 4)))  #False