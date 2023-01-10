from pytaxonomies import Taxonomies

taxonomies = Taxonomies()
print(f'Version: {taxonomies.version}')
print(f'License: {taxonomies.license}')
print(f'Description: {taxonomies.description}')
print(f'Number of taxonomies: {len(taxonomies)}')
print(f'Names: {list(taxonomies.keys())}')
