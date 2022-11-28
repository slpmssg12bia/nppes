#!/bin/bash
mkdir dump
mv *.txt dump

aws s3 sync dump/ s3://nnpes/dump-"$(date +%d-%m)"/