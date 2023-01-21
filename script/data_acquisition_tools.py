import json
from pytaxonomies import Taxonomy
from pytaxonomies import Predicate
from pytaxonomies import Entry

tools = open("../ressources/tools.md", 'r')

lines = tools.readlines()
tools.close()

tools_categories = {}
tools_categories["Distributions"] = {}
tools_categories["Live Forensics"] = {}
tools_categories["IOC Scanner"] = {}
tools_categories["Acquisition"] = {}
tools_categories["Imaging"] = {}
tools_categories["Carving"] = {}
tools_categories["Memory Forensics"] = {}
tools_categories["Network Forensics"] = {}
tools_categories["Windows Artifacts"] = {}
tools_categories["OS X Forensics"] = {}
tools_categories["Mobile Forensics"] = {}
tools_categories["Docker Forensics"] = {}
tools_categories["Internet Artifacts"] = {}
tools_categories["Timeline Analysis"] = {}
tools_categories["Disk Image Handling"] = {}
tools_categories["Decryption"] = {}
tools_categories["Management"] = {}
tools_categories["Picture Analysis"] = {}
tools_categories["Metadata Forensics"] = {}
tools_categories["Steganography"] = {}

# ------------
# SCRAP DATA |
# ------------

for cat in tools_categories:
    ok = False
    for line in lines:
        if not ok:
            if line.__contains__("### "+cat):
                ok = True
        else:
            if line.__contains__("###"):
                break
            else:
                temp = line
                temp = temp.replace('- [', '')
                temp = temp.replace(']', '')
                temp = temp.replace('\n', '')
                temp = temp.split(" - ")
                if len(temp) > 1:
                    t = temp[0].split("(")
                    tools_categories[cat][t[0]] = temp[1]

# ------------------------
# STORE DATA IN TAXONOMY |
# ------------------------

# Declare taxonomy
taxonomy = Taxonomy()

taxonomy.name = "data-acquisition-tools"
taxonomy.description = "This taxonomy aims to classify data acquisition tools."
taxonomy.version = 1
taxonomy.expanded = "Data acquisition tools"

# Declare predicates
predicates = {}

for cat in tools_categories:
    predicates[cat] = Predicate()
    predicates[cat].expanded = cat
    predicates[cat].predicate = cat.strip().replace(" ", "_")
    if cat == "Disk Image Handling":
        predicates[cat].description = 'Methods used when acquiring data from disk'
    elif cat == "Memory Forensics":
        predicates[cat].description = 'Methods used when acquiring data from memory'
    elif cat == "Network Forensics" :
        predicates[cat].description = 'Methods used when acquiring data from network'

# Declare entries
entries_dict = {}

for cat in tools_categories:
    entries_dict[cat] = []
    for tools in tools_categories[cat]:
        temp = Entry()
        temp.expanded = tools
        name = tools
        name = name.lower()
        name = name.strip()
        name = name.replace(' ', '_')
        temp.value = name
        temp.description = tools_categories[cat][tools]
        entries_dict[cat].append(temp)

# Add entries to predicates
for cat in tools_categories:
    for entry in entries_dict[cat]:
        predicates[cat].entries[entry] = entry

# Add predicates to taxonomy
for cat in tools_categories:
    taxonomy.predicates[cat.strip().replace(' ', '_')] = predicates[cat]

# ---------------------
# EXPORT DATA IN JSON |
# ---------------------

with open("../json/data-acquisition-tools.json", 'wt', encoding='utf-8') as f:
    json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
