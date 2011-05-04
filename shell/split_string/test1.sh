#!/bin/bash

STR="aaa:bbb:ccc"
IFS=:

for word in ${STR}; do
    echo ${word}
done
