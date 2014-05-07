#! /usr/bin/env python

import json

import union.ossec_collector as collector


print(json.dumps(collector.collect()))
