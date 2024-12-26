#!/usr/bin/env bash
if [[ -z "$1" ]]; then
  echo "No day argument provided. Correct usage: 'solver.sh {DAY}', e.g. 'solver.sh 2'"
  exit 1
fi
day="$1"
if [[ ! "$day" =~ ^[0-9]{1,2}$ || "$day" -lt 1 || "$day" -gt 25 ]]; then
  echo "Day argument must be a number between 1 and 25."
  exit 1
fi
if [[ "$day" -lt 10 ]]; then
  day="0$day"
fi
python -m "src.puzzles.day_$day.solution"
