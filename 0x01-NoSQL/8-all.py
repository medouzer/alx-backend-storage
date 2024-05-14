#!/usr/bin/env python3
"""List all documents in Python"""

import pymongo


def list_all(mongo_collection):
    """list_all"""
    return mongo_collection.find()
