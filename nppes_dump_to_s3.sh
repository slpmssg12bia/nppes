#!/bin/bash
mkdir dump
mv *.csv dump *.pdf
aws s3 sync dump/ s3://viquity-database-import-us-east-1/Jobs/nppes/dump-"$(date +%d-%m-%y-%H-%M)"/
