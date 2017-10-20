#This code replaces all 172 ip with 192


with open('running-config.cfg','r') as run:
    with open('Task-3_New replaced file with 192.cfg','w') as new:

        for line in run:
         new.write(line.replace('172','192'))
        new.close()