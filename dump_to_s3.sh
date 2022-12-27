#!/bin/bash
mkdir nppesdump
mv *.csv  *.pdf nppesdump
aws s3 sync nppesdump/ s3://viquity-database-import-us-east-1/Jobs/nppes/nppesdump/
