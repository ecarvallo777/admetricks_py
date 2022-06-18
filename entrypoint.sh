#!/bin/bash
if [[ $1 == "bash" ]]; then
    /bin/bash
else if [[ $1 == "songs"]]; then
    python3 songs.py
else if [[ $1 == "stories"]]; then
    python3 stories.py
fi
