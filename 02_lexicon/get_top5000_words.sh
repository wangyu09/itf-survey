#!/bin/bash

awk '{$1="";print $0}' < text | tr [" "] ["\n"] | sort | uniq -c | sort -nr | awk '{print $2}' | tr -s '\n' | head -n 5000 > wordslist.txt