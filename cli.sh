#!/bin/sh

# Set your API key using this line first
#
# export DOMINO_API_KEY=<YOUR API KEY>
#
# before running this
curl -v -X POST \
    https://app.dominodatalab.com/v1/SparkIQLabs/helloWorld/endpoint \
    -H 'Content-Type: application/json' \
    -H 'X-Domino-Api-Key: '$DOMINO_API_KEY \
    -d '{"parameters": [ "5.1", "3.5", "1.4", "0.2"]}'

# return value should be: setosa
