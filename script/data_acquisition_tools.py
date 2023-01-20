import json
from pytaxonomies import Taxonomy
from pytaxonomies import Predicate
from pytaxonomies import Entry

tools = open("../ressources/tools.md", 'r')

lines = tools.readlines()
tools.close()

tools_categories = []

# ------------
# SCRAP DATA |
# ------------

# STORE DISTRIBUTIONS TOOLS
# ------------------------------------------------------------------------------------------------------
distributions_tools = []
distributions_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Distributions"):
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
                distributions_tools.append(t[0])
                distributions_tools_desc.append(temp[1])

tools_categories.append("Distributions")
# ------------------------------------------------------------------------------------------------------

# STORE FRAMEWORKS
# ------------------------------------------------------------------------------------------------------
frameworks = []
frameworks_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Frameworks"):
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
                frameworks.append(t[0])
                frameworks_desc.append(temp[1])

tools_categories.append("Frameworks")
# ------------------------------------------------------------------------------------------------------

# STORE LIVE FORENSICS TOOLS
# ------------------------------------------------------------------------------------------------------
live_tools = []
live_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Live Forensics"):
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
                live_tools.append(t[0])
                live_tools_desc.append(temp[1])

tools_categories.append("Live Forensics")
# ------------------------------------------------------------------------------------------------------

# STORE IOC SCANNER TOOLS
# ------------------------------------------------------------------------------------------------------
ioc_scanner_tools = []
ioc_scanner_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### IOC Scanner"):
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
                ioc_scanner_tools.append(t[0])
                ioc_scanner_tools_desc.append(temp[1])

tools_categories.append("IOC Scanner")
# ------------------------------------------------------------------------------------------------------

# STORE ACQUISITION TOOLS
# ------------------------------------------------------------------------------------------------------
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
        else:
            temp = line
            temp = temp.replace('- [', '')
            temp = temp.replace(']', '')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                acquisition_tools.append(t[0])
                acquisition_tools_desc.append(temp[1])
tools_categories.append("Acquisition")
# ------------------------------------------------------------------------------------------------------

# STORE IMAGING TOOLS
# ------------------------------------------------------------------------------------------------------
imaging_tools = []
imaging_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Imaging"):
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
                imaging_tools.append(t[0])
                imaging_tools_desc.append(temp[1])

tools_categories.append("Imaging")
# ------------------------------------------------------------------------------------------------------

# STORE CARVING TOOLS
# ------------------------------------------------------------------------------------------------------
carving_tools = []
carving_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Carving"):
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
                carving_tools.append(t[0])
                carving_tools_desc.append(temp[1])

tools_categories.append("Carving")
# ------------------------------------------------------------------------------------------------------

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
        else:
            temp = line
            temp = temp.replace('- [', '')
            temp = temp.replace(']', '')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                memory_tools.append(t[0])
                memory_tools_desc.append(temp[1])

tools_categories.append("Memory_forensics")
# ------------------------------------------------------------------------------------------------------

# STORE NETWORK TOOLS
# ------------------------------------------------------------------------------------------------------
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
        else:
            temp = line
            temp = temp.replace('- [', '')
            temp = temp.replace(']', '')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                network_tools.append(t[0])
                network_tools_desc.append(temp[1])
tools_categories.append("Network_forensics")
# ------------------------------------------------------------------------------------------------------

# STORE WINDOWS ARTIFACTS TOOLS
# ------------------------------------------------------------------------------------------------------
w_artifacts_tools = []
w_artifacts_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Windows Artifacts"):
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
                w_artifacts_tools.append(t[0])
                w_artifacts_tools_desc.append(temp[1])

tools_categories.append("Windows artifacts")
# ------------------------------------------------------------------------------------------------------

# STORE OS X FORENSICS TOOLS
# ------------------------------------------------------------------------------------------------------
osx_tools = []
osx_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### OS X Forensics"):
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
                osx_tools.append(t[0])
                osx_tools_desc.append(temp[1])

tools_categories.append("OS X Forensics")
# ------------------------------------------------------------------------------------------------------

# STORE MOBILE FORENSICS TOOLS
# ------------------------------------------------------------------------------------------------------
mobile_tools = []
mobile_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Mobile Forensics"):
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
                mobile_tools.append(t[0])
                mobile_tools_desc.append(temp[1])

tools_categories.append("Mobile Forensics")
# ------------------------------------------------------------------------------------------------------

# STORE DOCKER FORENSICS TOOLS
# ------------------------------------------------------------------------------------------------------
docker_tools = []
docker_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Docker Forensics"):
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
                docker_tools.append(t[0])
                docker_tools_desc.append(temp[1])

tools_categories.append("Docker Forensics")
# ------------------------------------------------------------------------------------------------------

# STORE INTERNET ARTIFACTS TOOLS
# ------------------------------------------------------------------------------------------------------
internet_artifacts_tools = []
internet_artifacts_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Internet Artifacts"):
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
                internet_artifacts_tools.append(t[0])
                internet_artifacts_tools_desc.append(temp[1])

tools_categories.append("Internet Artifacts")
# ------------------------------------------------------------------------------------------------------

# STORE TIMELINE ANALYSIS TOOLS
# ------------------------------------------------------------------------------------------------------
timeline_analysis_tools = []
timeline_analysis_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Timeline Analysis"):
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
                timeline_analysis_tools.append(t[0])
                timeline_analysis_tools_desc.append(temp[1])

tools_categories.append("Timeline Analysis")
# ------------------------------------------------------------------------------------------------------

# STORE DISK IMAGE HANDLING TOOLS
# ------------------------------------------------------------------------------------------------------
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
        else:
            temp = line
            temp = temp.replace('- [', '')
            temp = temp.replace(']', '')
            temp = temp.replace('\n', '')
            temp = temp.split(" - ")
            if len(temp) > 1:
                t = temp[0].split("(")
                disk_tools.append(t[0])
                disk_tools_desc.append(temp[1])
tools_categories.append("Disk_Image_Handling")
# ------------------------------------------------------------------------------------------------------

# STORE DECRYPTION TOOLS
# ------------------------------------------------------------------------------------------------------
decryption_tools = []
decryption_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Decryption"):
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
                decryption_tools.append(t[0])
                decryption_tools_desc.append(temp[1])
tools_categories.append("Decryption")
# ------------------------------------------------------------------------------------------------------

# STORE MANAGEMENT TOOLS
# ------------------------------------------------------------------------------------------------------
management_tools = []
management_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Management"):
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
                management_tools.append(t[0])
                management_tools_desc.append(temp[1])
tools_categories.append("Management")
# ------------------------------------------------------------------------------------------------------

# STORE PICTURE ANALYSIS TOOLS
# ------------------------------------------------------------------------------------------------------
picture_analysis_tools = []
picture_analysis_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Picture Analysis"):
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
                picture_analysis_tools.append(t[0])
                picture_analysis_tools_desc.append(temp[1])
tools_categories.append("Picture Analysis")
# ------------------------------------------------------------------------------------------------------

# STORE METADATA FORENSICS TOOLS
# ------------------------------------------------------------------------------------------------------
metadata_forensics_tools = []
metadata_forensics_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Metadata Forensics"):
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
                metadata_forensics_tools.append(t[0])
                metadata_forensics_tools_desc.append(temp[1])
tools_categories.append("Metadata Forensics")
# ------------------------------------------------------------------------------------------------------

# STORE STEGANOGRAPHY TOOLS
# ------------------------------------------------------------------------------------------------------
stegano_tools = []
stegano_tools_desc = []
ok = False
for line in lines:
    if not ok:
        if line.__contains__("### Steganography"):
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
                stegano_tools.append(t[0])
                stegano_tools_desc.append(temp[1])
tools_categories.append("Steganography")
# ------------------------------------------------------------------------------------------------------

# --------------------
# STORE DATA IN JSON |
# --------------------

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
network_acquisition_predicate.description = 'Methods used when acquiring data from network'
predicates.append(memory_acquisition_predicate)

# ------------------------------
distribution_predicate = Predicate()
distribution_predicate.predicate = 'distribution'
distribution_predicate.expanded = 'Distribution'
predicates.append(distribution_predicate)

frameworks_predicate = Predicate()
frameworks_predicate.predicate = 'frameworks'
frameworks_predicate.expanded = 'Frameworks'
predicates.append(frameworks_predicate)

live_predicate = Predicate()
live_predicate.predicate = 'live_forensics'
live_predicate.expanded = 'Live Forensics'
predicates.append(live_predicate)

ioc_scaner_predicate = Predicate()
ioc_scaner_predicate.predicate = 'ioc_scanner'
ioc_scaner_predicate.expanded = 'IOC Scanner'
predicates.append(ioc_scaner_predicate)

imaging_predicate = Predicate()
imaging_predicate.predicate = 'imaging'
imaging_predicate.expanded = 'Imaging'
predicates.append(imaging_predicate)

carving_predicate = Predicate()
carving_predicate.predicate = 'carving'
carving_predicate.expanded = 'Carving'
predicates.append(carving_predicate)

w_artifacts_predicate = Predicate()
w_artifacts_predicate.predicate = 'windows_artifacts'
w_artifacts_predicate.expanded = 'Windows Artifacts'
predicates.append(w_artifacts_predicate)

osx_predicate = Predicate()
osx_predicate.predicate = 'os_x_forensics'
osx_predicate.expanded = 'OS X Forensics'
predicates.append(osx_predicate)

mobile_predicate = Predicate()
mobile_predicate.predicate = 'mobile_forensics'
mobile_predicate.expanded = 'Mobile Forensics'
predicates.append(mobile_predicate)

docker_predicate = Predicate()
docker_predicate.predicate = 'docker_forensics'
docker_predicate.expanded = 'Docker Forensics'
predicates.append(docker_predicate)

internet_artifacts_predicate = Predicate()
internet_artifacts_predicate.predicate = 'internet_artifacts'
internet_artifacts_predicate.expanded = 'Internet Artifacts'
predicates.append(internet_artifacts_predicate)

timeline_analysis_predicate = Predicate()
timeline_analysis_predicate.predicate = 'timeline_analysis'
timeline_analysis_predicate.expanded = 'Timeline Analysis'
predicates.append(timeline_analysis_predicate)

decryption_predicate = Predicate()
decryption_predicate.predicate = 'decryption'
decryption_predicate.expanded = 'Decryption'
predicates.append(decryption_predicate)

management_predicate = Predicate()
management_predicate.predicate = 'management'
management_predicate.expanded = 'Management'
predicates.append(management_predicate)

picture_analysis_predicate = Predicate()
picture_analysis_predicate.predicate = 'picture_analysis'
picture_analysis_predicate.expanded = 'Picture Analysis'
predicates.append(picture_analysis_predicate)

metadata_forensics_predicate = Predicate()
metadata_forensics_predicate.predicate = 'metadata_forensics'
metadata_forensics_predicate.expanded = 'Metadata Forensics'
predicates.append(metadata_forensics_predicate)

stegano_predicate = Predicate()
stegano_predicate.predicate = 'steganography'
stegano_predicate.expanded = 'Steganography'
predicates.append(stegano_predicate)

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
    i = i + 1
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
    i = i + 1
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
    i = i + 1
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
    i = i + 1
    network_entries.append(temp)

# Declare entries for Distributions Forensics
distributions_entries = []
i = 0
for t in distributions_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = distributions_tools_desc[i]
    i = i + 1
    distributions_entries.append(temp)

# Declare entries for Frameworks
frameworks_entries = []
i = 0
for t in frameworks:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = frameworks_desc[i]
    i = i + 1
    frameworks_entries.append(temp)

# Declare entries for Live Forensics
live_entries = []
i = 0
for t in live_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = live_tools_desc[i]
    i = i + 1
    live_entries.append(temp)

# Declare entries for IOC Scanner
ioc_scanner_entries = []
i = 0
for t in ioc_scanner_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = ioc_scanner_tools_desc[i]
    i = i + 1
    ioc_scanner_entries.append(temp)

# Declare entries for Imaging
imaging_entries = []
i = 0
for t in imaging_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = imaging_tools_desc[i]
    i = i + 1
    imaging_entries.append(temp)

# Declare entries for Carving
carving_entries = []
i = 0
for t in carving_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = carving_tools_desc[i]
    i = i + 1
    carving_entries.append(temp)

# Declare entries for Windows Artifacts
w_artifacts_entries = []
i = 0
for t in w_artifacts_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = w_artifacts_tools_desc[i]
    i = i + 1
    w_artifacts_entries.append(temp)

# Declare entries for OS X Forensics
osx_entries = []
i = 0
for t in osx_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = osx_tools_desc[i]
    i = i + 1
    osx_entries.append(temp)

# Declare entries for Mobile Forensics
mobile_entries = []
i = 0
for t in mobile_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = mobile_tools_desc[i]
    i = i + 1
    mobile_entries.append(temp)

# Declare entries for Docker Forensics
docker_entries = []
i = 0
for t in docker_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = docker_tools_desc[i]
    i = i + 1
    docker_entries.append(temp)

# Declare entries for Internet Artifacts
internet_artifacts_entries = []
i = 0
for t in internet_artifacts_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = internet_artifacts_tools_desc[i]
    i = i + 1
    internet_artifacts_entries.append(temp)

# Declare entries for Timeline Analysis
timeline_analysis_entries = []
i = 0
for t in timeline_analysis_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = timeline_analysis_tools_desc[i]
    i = i + 1
    timeline_analysis_entries.append(temp)

# Declare entries for Decryption
decryption_entries = []
i = 0
for t in decryption_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = decryption_tools_desc[i]
    i = i + 1
    decryption_entries.append(temp)

# Declare entries for Management
management_entries = []
i = 0
for t in management_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = management_tools_desc[i]
    i = i + 1
    management_entries.append(temp)

# Declare entries for Picture Analysis
picture_analysis_entries = []
i = 0
for t in picture_analysis_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = picture_analysis_tools_desc[i]
    i = i + 1
    picture_analysis_entries.append(temp)

# Declare entries for MetaData Forensics
metadata_forensics_entries = []
i = 0
for t in metadata_forensics_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = metadata_forensics_tools_desc[i]
    i = i + 1
    metadata_forensics_entries.append(temp)

# Declare entries for Steganography
stegano_entries = []
i = 0
for t in stegano_tools:
    temp = Entry()
    name = t.lower()
    name = name.strip()
    name = name.replace(' ', '_')
    temp.value = name
    temp.expanded = t
    temp.description = stegano_tools_desc[i]
    i = i + 1
    stegano_entries.append(temp)

# ------------------------------------------------------------------------------------------------------
# Add entries to predicates
i = 0
for e in disk_entries:
    disk_acquisition_predicate.entries[disk_tools[i].replace(' ', '_')] = disk_entries[i]
    i = i + 1

i = 0
for e in acquisition_entries:
    disk_acquisition_predicate.entries[acquisition_tools[i].replace(' ', '_')] = acquisition_entries[i]
    i = i + 1

i = 0
for e in memory_entries:
    memory_acquisition_predicate.entries[memory_tools[i].replace(' ', '_')] = memory_entries[i]
    i = i + 1

i = 0
for e in network_entries:
    network_acquisition_predicate.entries[network_tools[i].replace(' ', '_')] = network_entries[i]
    i = i + 1

i = 0
for e in distributions_entries:
    distribution_predicate.entries[distributions_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in frameworks_entries:
    frameworks_predicate.entries[frameworks[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in live_entries:
    live_predicate.entries[live_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in ioc_scanner_entries:
    ioc_scaner_predicate.entries[ioc_scanner_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in imaging_entries:
    imaging_predicate.entries[imaging_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in carving_entries:
    carving_predicate.entries[carving_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in w_artifacts_entries:
    w_artifacts_predicate.entries[w_artifacts_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in osx_entries:
    osx_predicate.entries[osx_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in mobile_entries:
    mobile_predicate.entries[mobile_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in docker_entries:
    docker_predicate.entries[docker_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in internet_artifacts_entries:
    internet_artifacts_predicate.entries[internet_artifacts_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in timeline_analysis_entries:
    timeline_analysis_predicate.entries[timeline_analysis_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in decryption_entries:
    decryption_predicate.entries[decryption_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in management_entries:
    management_predicate.entries[management_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in picture_analysis_entries:
    picture_analysis_predicate.entries[picture_analysis_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in metadata_forensics_entries:
    metadata_forensics_predicate.entries[metadata_forensics_tools[i].replace(' ', '_')] = e
    i = i + 1

i = 0
for e in stegano_entries:
    stegano_predicate.entries[stegano_tools[i].replace(' ', '_')] = e
    i = i + 1

# Add predicates to taxonomy
taxonomy.predicates = {
    'disk-acquisition': disk_acquisition_predicate,
    'memory-acquisition': memory_acquisition_predicate,
    'network-acquisition': network_acquisition_predicate,
    'distributions': distribution_predicate,
    'framework': frameworks_predicate,
    'live-forensics': live_predicate,
    'ioc-scanner': ioc_scaner_predicate,
    'imaging': imaging_predicate,
    'carving': carving_predicate,
    'windows-artifacts': w_artifacts_predicate,
    'os-x-forensics': osx_predicate,
    'mobile-forensics': mobile_predicate,
    'docker-forensics': docker_predicate,
    'internet-artifacts': internet_artifacts_predicate,
    'timeline-analysis': timeline_analysis_predicate,
    'decryption': decryption_predicate,
    'management': management_predicate,
    'picture-analysis': picture_analysis_predicate,
    'metadata-forensics': metadata_forensics_predicate,
    'steganography': stegano_predicate
}
# ------------------------------------------------------------------------------------------------------

# ---------------------
# EXPORT DATA IN JSON |
# ---------------------

with open("../json/data-acquisition-tools.json", 'wt', encoding='utf-8') as f:
    json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
