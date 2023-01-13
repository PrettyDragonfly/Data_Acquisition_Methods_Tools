import json

from bs4 import BeautifulSoup as bs
import urllib.request
from pytaxonomies import Taxonomy
from pytaxonomies import Predicate
from pytaxonomies import Entry
import ssl
from urllib.request import Request

ssl._create_default_https_context = ssl._create_unverified_context

req = Request(
    url="https://www.eccouncil.org/cybersecurity-exchange/computer-forensics/data-acquisition-digital-forensics/",
    headers={'User-Agent': 'Mozilla/5.0'}
)

page = urllib.request.urlopen(req, timeout=5)

soup = bs(page, "html.parser")

# SCRAP VALUES FOR DISK ACQUISITION
# ------------------------------------------------------------------------------------------------------
# Disk to image methods is an h2 title
disktoimage = soup.find_all('h2')

dtd = []
for e in disktoimage:
    e = e.text
    e = e.replace('\n', '')
    dtd.append(e)

# Others methods are h3 titles
disk_meth = soup.find_all('h3', {'class': 'elementor-heading-title elementor-size-default'})

# Add disk to image to the methods
disk_methods_expanded = [dtd[4]]

for e in disk_meth:
    e = e.text
    e = e.replace('\n', '')
    disk_methods_expanded.append(e)

# Descriptions
disk_methods_desc = []
dti_desc = soup.find_all('div', {'class': 'elementor-element elementor-element-7cc1dfe elementor-widget '
                                          'elementor-widget-text-editor'})
for e in dti_desc:
    e = e.p.text
    e = e.replace('\n', '')
    e = e.replace('\t', '')
    dti_desc = e
disk_methods_desc.append(dti_desc)

dtd_desc = soup.find_all('div', {'class': 'elementor-element elementor-element-c7b535b elementor-widget '
                                          'elementor-widget-text-editor'})
for e in dtd_desc:
    e = e.text
    e = e.replace('\n', '')
    e = e.replace('\t', '')
    dtd_desc = e
disk_methods_desc.append(dtd_desc)

logical_desc = soup.find_all('div', {'class': 'elementor-element elementor-element-c7bc4b0 elementor-widget '
                                              'elementor-widget-text-editor'})
for e in logical_desc:
    e = e.text
    e = e.replace('\n', '')
    e = e.replace('\t', '')
    logical_desc = e
disk_methods_desc.append(logical_desc)

sparse_desc = soup.find_all('div', {'class': 'elementor-element elementor-element-0ad1660 elementor-widget '
                                             'elementor-widget-text-editor'})
for e in sparse_desc:
    e = e.text
    e = e.replace('\n', '')
    e = e.replace('\t', '')
    sparse_desc = e
disk_methods_desc.append(sparse_desc)

disk_methods_name = []
for m in disk_methods_expanded:
    m = m.lower()
    m = m.strip()
    m = m.replace('-', ' ')
    m = m.replace(' ', '_')
    disk_methods_name.append(m)

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

# Declare entries
i = 0
entries = []
for m in disk_methods_name:
    temp = Entry()
    temp.value = disk_methods_name[i]
    temp.expanded = disk_methods_expanded[i]
    temp.description = disk_methods_desc[i]
    i = i+1
    entries.append(temp)

# Add entries to predicates
i = 0
for e in entries:
    disk_acquisition_predicate.entries[disk_methods_name[i]] = entries[i]
    i = i+1

# Add predicate to taxonomy
taxonomy.predicates = {
    'disk-acquisition': disk_acquisition_predicate,
}

with open("../json/taxonomy.json", 'wt', encoding='utf-8') as f:
    json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
