import json
from pytaxonomies import Taxonomy
from pytaxonomies import Predicate
from pytaxonomies import Entry

tools = open("../ressources/tools.md", 'r')

lines = tools.readlines()
tools.close()

tools_categories = []

# STORE MEMORY TOOLS
# ------------------------------------------------------------------------------------------------------
memory_tools = []
memory_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Memory Forensics"):
            ok = True
    else:
        if line.__contains__("###"):
            break
        else :
            temp = line
            temp = temp.replace('- [','')
            temp = temp.replace(']','')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                memory_tools.append(t[0])
                memory_tools_desc.append(temp[1])

tools_categories.append("Memory_forensics")

# STORE NETWORK TOOLS
network_tools = []
network_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Network Forensics"):
            ok = True
    else:
        if line.__contains__("###"):
            break
        else :
            temp = line
            temp = temp.replace('- [','')
            temp = temp.replace(']','')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                network_tools.append(t[0])
                network_tools_desc.append(temp[1])
tools_categories.append("Network_forensics")

# STORE DISK IMAGE HANDLING TOOLS
disk_tools = []
disk_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Disk image handling"):
            ok = True
    else:
        if line.__contains__("###"):
            break
        else :
            temp = line
            temp = temp.replace('- [','')
            temp = temp.replace(']','')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                disk_tools.append(t[0])
                disk_tools_desc.append(temp[1])
tools_categories.append("Disk_Image_Handling")

# STORE ACQUISITION TOOLS
acquisition_tools = []
acquisition_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Acquisition"):
            ok = True
    else:
        if line.__contains__("###"):
            break
        else :
            temp = line
            temp = temp.replace('- [','')
            temp = temp.replace(']','')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                acquisition_tools.append(t[0])
                acquisition_tools_desc.append(temp[1])
tools_categories.append("Acquisition")

# ------------------------------------------------------------------------------------------------------

# STORE DATA IN JSON
# ------------------------------------------------------------------------------------------------------
taxonomy = Taxonomy()

taxonomy.name = "data-acquisition-tools"
taxonomy.description = "This taxonomy aims to classify data acquisition tools."
taxonomy.version = 1
taxonomy.expanded = "Data acquisition tools"

# Declare predicates
predicates = []
disk_acquisition_predicate = Predicate()
disk_acquisition_predicate.predicate = 'disk_acquisition'
disk_acquisition_predicate.expanded = 'Disk acquisition'
disk_acquisition_predicate.description = 'Methods used when acquiring data from disk'
predicates.append(disk_acquisition_predicate)

memory_acquisition_predicate = Predicate()
memory_acquisition_predicate.predicate = 'memory_acquisition_predicate'
memory_acquisition_predicate.expanded = 'Memory acquisition'
memory_acquisition_predicate.description = 'Methods used when acquiring data from memory'
predicates.append(memory_acquisition_predicate)

network_acquisition_predicate = Predicate()
network_acquisition_predicate.predicate = 'network_acquisition_predicate'
network_acquisition_predicate.expanded = 'Network acquisition'
memory_acquisition_predicate.description = 'Methods used when acquiring data from network'
predicates.append(memory_acquisition_predicate)

# ------------------------------------------------------------------------------------------------------
# Declare entries for Disk Image/Acquisition
disk_entries = []
i = 0
for t in disk_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = disk_tools_desc[i]
    i = i+1
    disk_entries.append(temp)

i = 0
acquisition_entries = []
for t in acquisition_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = acquisition_tools_desc[i]
    i = i+1
    acquisition_entries.append(temp)

# Declare entries for Memory Forensics
memory_entries = []
i = 0
for t in memory_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = memory_tools_desc[i]
    i = i+1
    memory_entries.append(temp)

# Declare entries for Network Forensics
network_entries = []
i = 0
for t in network_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = network_tools_desc[i]
    i = i+1
    network_entries.append(temp)

# ------------------------------------------------------------------------------------------------------
# Add entries to predicates
i = 0
for e in disk_entries:
    disk_acquisition_predicate.entries[disk_tools[i].replace(' ', '_')] = disk_entries[i]
    i = i+1

i = 0
for e in acquisition_entries:
    disk_acquisition_predicate.entries[acquisition_tools[i].replace(' ', '_')] = acquisition_entries[i]
    i = i+1

i = 0
for e in memory_entries:
    memory_acquisition_predicate.entries[memory_tools[i].replace(' ', '_')] = memory_entries[i]
    i = i+1

i = 0
for e in network_entries:
    network_acquisition_predicate.entries[network_tools[i].replace(' ', '_')] = network_entries[i]
    i = i+1

# Add predicates to taxonomy
taxonomy.predicates = {
    'disk-acquisition': disk_acquisition_predicate,
    'memory-acquisition': memory_acquisition_predicate,
    'network-acquisition': network_acquisition_predicate
}

# ------------------------------------------------------------------------------------------------------

with open("../json/data-acquisition-tools.json", 'wt', encoding='utf-8') as f:
    json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
