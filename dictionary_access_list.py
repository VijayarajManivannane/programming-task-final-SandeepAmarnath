
#Storing access-list in dictionary
with open('Access_list.cfg','r') as acl:
    d={}
    a=[]


    for line in acl:
        if 'transit_access' in line:
            a.append(line)
    d['transit_access']=a



with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'global_access' in line:
            a.append(line)
    d['global_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'xcompany-lan_access' in line:
            a.append(line)
    d['xcompany-lan_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'management2_access' in line:
            a.append(line)
    d['management2_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'SomeProducts_access' in line:
            a.append(line)
    d['SomeProducts_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'fw-management_access' in line:
            a.append(line)
    d['fw-management_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'WirelessHotspot_access' in line:
            a.append(line)
    d['WirelessHotspot_access'] = a

with open('Access_list.cfg','r') as acl:

    a=[]
    for line in acl:
        if 'voicevlan_access_in' in line:
            a.append(line)
    d['voicevlan_access_in'] = a
    print(d)










