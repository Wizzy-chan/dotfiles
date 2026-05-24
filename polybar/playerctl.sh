#!/usr/bin/bash

format="{{artist}} - {{title}}"

echo "Nothing Playing"
playerctl metadata -f "$format" -F | while read line; do
  if [[ "$line" ]]; then
    echo "Now Playing: $line"
  else
    echo "Nothing Playing"
  fi
done
