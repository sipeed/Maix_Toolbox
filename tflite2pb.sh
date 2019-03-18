#!/bin/bash
echo "usage: ./tflite2pb.sh xxx.tflite"
name=`echo $1 | cut -d '.' -f 1`
name=$name.pb
ncc -i tflite -o tf $1 $name
