#!/bin/bash
if [[ $1 == "bash" ]]; then
    /bin/bash
else
    python3 run.py --url $1 
fi
