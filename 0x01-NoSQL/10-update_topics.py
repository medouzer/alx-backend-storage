#!/usr/bin/env python3
"""Change school topics"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """function update_topics"""
    return mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
