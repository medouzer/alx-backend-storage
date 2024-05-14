#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def show_logs():
    """function show_logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    get_logs = nginx_collection.count_documents({"method": "GET"})
    post_logs = nginx_collection.count_documents({"method": "POST"})
    put_logs = nginx_collection.count_documents({"method": "PUT"})
    patch_logs = nginx_collection.count_documents({"method": "PATCH"})
    delete_logs = nginx_collection.count_documents({"method": "DELETE"})
    get_status_logs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(total_logs)
    print("Methods:")
    print(f"\tmethod GET: {get_logs}")
    print(f"\tmethod POST: {post_logs}")
    print(f"\tmethod PUT: {put_logs}")
    print(f"\tmethod PATCH: {patch_logs}")
    print(f"\tmethod DELETE: {delete_logs}")
    print(f"{get_status_logs} status check")

if __name__ == "__main__":
    """main"""
    show_logs()
