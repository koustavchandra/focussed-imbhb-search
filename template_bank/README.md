# O3 IMBHB template bank
Template bank for the PyCBC search on O3 24 Nov'19 C01 data and configuration file for its construction.

## Bank design

| Parameters | Values |
| ----- | ----- |
| spin range | <img src="https://latex.codecogs.com/svg.latex?\|\chi_{eff}\|&space;\leq&space;0.998" title="\|\chi_{eff}\| \leq 0.998" /> |
| Total Mass | <img src="https://latex.codecogs.com/svg.latex?100&space;M_\odot&space;\leq&space;M_T&space;\leq&space;600&space;M_\odot" title="100 M_\odot \leq M_T \leq 600 M_\odot" /> |
| Mass-Ratio | <img src="https://latex.codecogs.com/svg.latex?1&space;\leq&space;q&space;\leq&space;10" title="1 \leq q \leq 10" /> |
| f-low | <img src="https://latex.codecogs.com/svg.latex?15&space;Hz" title="15 Hz" /> |
| Minimum Match | 0.99 | 
| Minimum template duration | 70ms |
| Total number of templates | 630 |

## Building the bank

To setup the workflow, run `bash submit.sh user.name`. 
When the above command completes successfully, submit the workflow by:
```
cd output
pycbc_submit_dax --dax ${WORKFLOW_NAME}.dax --accounting-group ligo.dev.o3.cbc.bbh.pycbcoffline --no-grid
```
Wait for completion, then get the bank inside the `output` directory

<img src="Bank.png"  width="720">

See the general [PyCBC documentation](https://pycbc.org/pycbc/latest/html/tmpltbank.html) to understand the content of `tmpltbank_600.ini`.
