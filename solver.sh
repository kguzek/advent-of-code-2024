#!/usr/bin/env bash
[ -z "$1" ] && echo "No day argument provided. Correct usage: 'solver.sh {DAY}', e.g. 'solver.sh 2'" && exit 1
python -m "src.puzzles.day_$1.solution"
