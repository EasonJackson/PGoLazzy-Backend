import s2sphere

params = {}
params["north"] = 42.27384011
params["west"] = -71.80793310
params["south"] = 42.27384011
params["east"] = -71.80793310

region = s2sphere.RegionCoverer()
p1 = s2sphere.LatLng.from_degrees(params["north"], params["west"])
p2 = s2sphere.LatLng.from_degrees(params["south"], params["east"])
cell_ids = region.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))

print(cell_ids)