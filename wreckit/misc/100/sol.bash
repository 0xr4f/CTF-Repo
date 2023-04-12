#!/bin/bash

for ((direct=1000; direct>=1; direct--))
do
        read -r side < direction.txt
        unzip -o "$direct$side_password.zip"
done
