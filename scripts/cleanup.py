#!/usr/bin/env python

import openstack
import requests

conn = openstack.connect(cloud='molecule')

def travis_job_status(name):
    try:
        job = name.split("-")[1]
    except:
        job = name.split("molecule")[1]

    result = requests.get("https://api.travis-ci.org/v3/job/%s" % job)
    result = result.json()

    if "error_type" in result:
        return 2
    elif result["finished_at"] != None:
        return 0
    else:
        return 1

for server in conn.compute.servers():
    server_dict = server.to_dict()
    server_name = server_dict["name"]

    if not server_name.startswith("molecule"):
        continue

    if travis_job_status(server_name) == 0:
        conn.compute.delete_server(server_dict["id"], force=True)

for keypair in conn.compute.keypairs():
    keypair_dict = keypair.to_dict()
    keypair_name = keypair_dict["name"]

    if not keypair_name.startswith("molecule"):
        continue

    if travis_job_status(keypair_name) == 0:
        conn.compute.delete_keypair(keypair)

for security_group in conn.network.security_groups():
    security_group_dict = security_group.to_dict()
    security_group_name = security_group_dict["name"]

    if not security_group_name.startswith("molecule"):
        continue

    if travis_job_status(security_group_name) == 0:
        conn.network.delete_security_group(security_group)
