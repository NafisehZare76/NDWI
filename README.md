# NDWI
## NDWI (Normalized Difference Water Index)

The NDWI is a water detection index calculated using the formula:  
**NDWI = (Green - NIR) / (Green + NIR)**  

This index effectively estimates water turbidity or impurities but may produce errors in urban areas due to building shadows.  
- **Negative values**: Indicate urban areas or soil.  
- **Positive values**: Represent water bodies.  
- **Threshold**: Values greater than zero are typically considered water.  

### Implementation Details  
- **Dataset**: Sentinel-2 imagery was used.  
- **Sample Image**: The input image shows *Chitgar Lake* in Tehran, Iran (located in the `data` folder).  
- **Output**: Results are saved in the `result` folder.  
- **Test Script**: The `test` folder contains a ready-to-use script for index calculation and visualization.  

### Customization  
- The `NDWI.py` file contains the index calculation function.  
- If your band composition differs, adjust the **image band indices** in the code for accurate calculations.  

