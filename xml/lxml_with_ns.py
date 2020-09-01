import xml.etree.ElementTree as et

XML_NS = {'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
root = et.parse('data/test_ns.xml')

# first variant
for person in root.findall('{http://example.com/persons}person'):
    name = person.find('{http://example.com/persons}name').text
    alias = person.find('{http://example.com/olympic}name').text
    field = person.find('{http://example.com/olympic}field').text
    # print('{}: {} -> {}'.format(name, field, alias))



# second variant
ns = {
    'persons': 'http://example.com/persons',
    'olympic': 'http://example.com/olympic'
}
for person in root.findall('persons:person', ns):
    name = person.find('persons:name', ns).text
    alias = person.find('olympic:name', ns).text
    field = person.find('olympic:field', ns).text
    print('{}: {} -> {}'.format(name, field, alias))