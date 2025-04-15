# NDWI: The NDWI index is used for water detection,
# and the band numbers are based on Sentinel-2 imagery.
# The band numbers in the function can be modified according to your band combination. 
# Developed by programmer Nafiseh Zare :)

def NDWI (Image):
    NDWI=(Image[1]-Image[6])/(Image[1]+Image[6])
    return (NDWI)

