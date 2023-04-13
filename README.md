# TimeManagment

This is the code base and instructions for tracking productivity and time spent on important activities.

Required software:

* UNIX terminal (power shell for Windows)
* python

Optional software:

* Horo Timer -- Mac only (https://apps.apple.com/us/app/horo-timer-for-menu-bar/id1437226581?mt=12)
* conda (miniconda3)

## Quick Start

```
# 1. Clone repo
git clone https://github.com/dombraccia/TimeManagment
cd TimeManagement

# 2. Create conda env from yml file
conda activate managment

# 3. Run parse_time_log.py on sample data
python code/parse_time_log.py time_logs/2023-0411-0412.csv

## returns: plot saved to: plots/2023-0411-0412.png

# 4. Check output plot
open plots/2023-0411-0412.png 
``` 
