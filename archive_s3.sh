#!/bin/bash
aws s3 sync nppesdump/ s3://viquity-database-import-us-east-1/Jobs/nppes/nppes_archive/nppesdump-"$(date +%d-%m-%y-%H-%M)"/
