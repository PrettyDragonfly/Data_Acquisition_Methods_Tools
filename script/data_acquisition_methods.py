import json
from pytaxonomies import Taxonomy
from pytaxonomies import Predicate
from pytaxonomies import Entry

# STORE DATA IN JSON
# ------------------------------------------------------------------------------------------------------
taxonomy = Taxonomy()

taxonomy.name = "data-acquisition-methods"
taxonomy.description = "This taxonomy aims to classify data acquisition methods."
taxonomy.version = 1
taxonomy.expanded = "Data acquisition methods"

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

# Declare entries
memory_dump = Entry()
memory_dump.value = "memory_dump"
memory_dump.expanded = "Memory dump"
memory_dump.description = "A memory dump is the process of taking all information content in RAM and writing it to a storage drive."

# Add entries to predicates
memory_acquisition_predicate.entries = {
    'memory-dump': memory_dump
}

# Add predicates to taxonomy
taxonomy.predicates = {
    'disk-acquisition': disk_acquisition_predicate,
    'memory-acquisition': memory_acquisition_predicate,
    'network-acquisition': network_acquisition_predicate
}

# ------------------------------------------------------------------------------------------------------

with open("../json/data-acquisition-methods.json", 'wt', encoding='utf-8') as f:
    json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
