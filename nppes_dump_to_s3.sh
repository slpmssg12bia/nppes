#!/bin/bash
mkdir dump
mv *.txt dump

aws s3 sync dump/ s3://nppes2/dump-"$(date +%d-%m)"/
