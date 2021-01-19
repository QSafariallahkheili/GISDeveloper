from sentinelsat import SentinelAPI
from shapely.geometry import MultiPolygon, Polygon
user = 'qasemsafariallahkheili' 
password = '13691369@aA' 
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

import geopandas as gpd

import folium 
nReserve = gpd.read_file('/Users/qasemsafariallahkheili/Downloads/bbox.geojson')
m = folium.Map([47.109743, 15.506172 ], zoom_start=12)
folium.GeoJson(nReserve).add_to(m)
footprint = None
for i in nReserve['geometry']:
    footprint = i

products = api.query(footprint,
                     date = ('20190601', '20190626'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0,10)
                    )
products_gdf = api.to_geodataframe(products)
products_gdf_sorted = products_gdf.sort_values(['cloudcoverpercentage'], ascending=[True])
products_gdf_sorted
api.download("727299de-199e-493c-9363-5fd3d71a9eed")