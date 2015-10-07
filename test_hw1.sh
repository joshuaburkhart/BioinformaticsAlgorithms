#!/usr/bin/env bash
#Usage: sh test_hw1.sh

clear
TMP_FILE=cur_stdout.tmp
rm -f $TMP_FILE
for f in hw1/test/Test*.py
do
    echo "######################################################" $f >> $TMP_FILE
    f=$(echo $f | cut -d'.' -f1)
    f=$(echo $f | sed "s/\//\./g")
    python -m $f >> $TMP_FILE 2>&1
    if grep -q Fail $TMP_FILE;
    then
        echo "FAILURE DETECTED"
        echo "================"
        break
    fi
    if grep -q Error $TMP_FILE;
    then
        echo "ERROR DETECTED"
        echo "=============="
        break
    fi
done
cat $TMP_FILE | sed '/^$/d'
rm -f $TMP_FILE
