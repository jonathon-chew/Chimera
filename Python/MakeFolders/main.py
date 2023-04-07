import os

# names = ["All Safety Ltd Ta Diggerland","AZ, Cambridge","AZ, Luton","AZ, Macclesfield","Bank of England","Benvolent","Dartford & Gravesham NHS Trust","Department for Health & Social Care","Jami UK","Johnson Matthey","Kent Community Health NHS Foundation Trust","Ladbrokes","NHSBT Sheffield - ATMP","NHSBT-Filton, Bristol - ATMP","NHSBT, Speke","Ofcom","Pall" ,"Pharma Services Patheon (Swindon) - part of Thermofisher Scientific","Regent Electrical","Syneos","Thermofisher  (Basingstoke) Oxoid Ltd","Thermofisher (Remel Europe)","Youth Employment UK"]


# path = "/Volumes/MEDWAY/Higher and Degree Apprenticeships/CHDA MAIN FOLDER/Apprentice Database (Evidence)/Contracts Audit/Chase/Combined"
# os.chdir(path)

# for i in names:
#     os.mkdir(i)
counter = 1
path = "/Users/hunteradder626/Desktop/JavaScript"
os.chdir(path)
while counter <= 30:
    try:
        os.mkdir(f"Day {counter}")
    except:
        pass
    os.chdir(path)
    counter +=1