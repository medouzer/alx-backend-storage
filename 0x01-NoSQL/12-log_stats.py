#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def show_logs():
    """function show_logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print(total_logs)
    print("Methods:")
    get_logs = nginx_collection.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get_logs}")
    post_logs = nginx_collection.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post_logs}")
    put_logs = nginx_collection.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put_logs}")
    patch_logs = nginx_collection.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch_logs}")
    delete_logs = nginx_collection.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete_logs}")
    get_status_logs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{get_status_logs} status check")

if __name__ == "__main__":
    """main"""
    show_logs()
