# Thermal_calib_Generator

### Generates the Calibrated result matrices for an any LWIR uncooled microbolometer.

#### Tools required
0) Python3
1) Numpy
2) Inquirer
  > pip install inquirer
  

Create /datasets folder with following structure;
```
.
├── ...
├── datasets
|   ├──gain
|       ├──low_temp
|       ├──high_temp
|   ├──offset
|       ├──0
|       ├──4
|       ├──etc..
└── ...
```
Place all data in respective locations in the 'datasets' folder.

All offset data in individual folders; inside the '/datasets/offset/' folder.

The script generates all output matrices and the bolometer co-efficients and saves it in the 'results' directory.
Formatted output stored in 'final_results'
