import json
from pprint import pprint

#with open('active.json') as json_file:
#    data = json.load(json_file)
#    pprint('Number of locations: ', len(data['features']))
#    for f in data['features']:
#        print(f['geometry']['coordinates'])

with open('links.json') as json_file:
    data = json.load(json_file)
    link_cnt = {}
    for f in data['features']:
        for node in f['geometry']['coordinates']:
            if str(node) in link_cnt:
                link_cnt[str(node)] += 1
            else:
                link_cnt[str(node)] = 1
    for k,v in sorted(link_cnt.items(), key=lambda item: item[1]):
        print(k, v)