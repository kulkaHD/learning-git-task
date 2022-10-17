import csv


import csv

dcs = []

with open('clean_stations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['station'], row['latitude'], row['longitude'], row['elevation'], row['name'], row['country'], row['state'])
        dcs.append(dict(row))

print(dcs)

# conn.execute(ins, [
#     {'station' : 'USC00519397', 'latitude' : 21.2716, 'longitude' : -157.8168, 'elevation' : 3.0, 'name' : 'WAIKIKI 717.2', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00513117', 'latitude' : 21.4234, 'longitude' : -157.8015, 'elevation' : 14.6, 'name' : 'KANEOHE 838.1', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00514830', 'latitude' : 21.5213, 'longitude' : -157.8374, 'elevation' : 7.0, 'name' : 'KUALOA RANCH HEADQUARTERS 886.9', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00518838', 'latitude' : 21.4992, 'longitude' : -158.0111, 'elevation' : 306.6, 'name' : 'UPPER WAHIAWA 874.3', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00519523', 'latitude' : 21.3356, 'longitude' : -157.7114, 'elevation' : 19.5, 'name' : 'WAIMANALO EXPERIMENTAL FARM', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00519281', 'latitude' : 21.4517, 'longitude' : -157.8489, 'elevation' : 32.9, 'name' : 'WAIHEE 837.5', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00511918', 'latitude' : 21.3152, 'longitude' : -157.9992, 'elevation' : 0.9, 'name' : 'HONOLULU OBSERVATORY 702.2', 'country' : 'US', 'state' : 'HI'},
#     {'station' : 'USC00516128', 'latitude' : 21.3331, 'longitude' : -157.8025, 'elevation' : 152.4, 'name' : 'MANOA LYON ARBO 785.2', 'country' : 'US', 'state' : 'HI'}
#     ])