#!/usr/bin/env bash
if [ $# -eq 0 ]; then
  echo "No day argument provided. Correct usage: 'solver.sh {DAY}', e.g. 'solver.sh 2'"
else
  python -m "src.puzzles.day_$1.solution"
fi
