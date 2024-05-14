#!/usr/bin/env python3
"""Where can I learn Python?"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """function schools_by_topic"""
    return mongo_collection.find({"topic": topic})
