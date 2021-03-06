#!/usr/bin/env python
# encoding: utf-8
from cluster import *

def add_host(session_uuid, cluster_uuid, host_ip, host_name, user_name, password, ssh_port):
    content = {"name" : host_name, "username": user_name, "password":password, "sshPort":ssh_port, "clusterUuid":cluster_uuid , "managementIp":host_ip}
    rsp = api_call(session_uuid, "org.zstack.kvm.APIAddKVMHostMsg", content)
    error_if_fail(rsp)
    print "\nsuccessfully add host: %s" % host_name
    return rsp['org.zstack.header.host.APIAddHostEvent']['inventory']['uuid']

def query_host(session_uuid, conditions):
    content = {'conditions':conditions}
    rsp = api_call(session_uuid, "org.zstack.header.host.APIQueryHostMsg", content)
    error_if_fail(rsp)
    print rsp
    print "\nsuccessfully query host"
    return rsp

def update_host(session_uuid, host_uuid, host_name):
    content = {"uuid":host_uuid, "name":host_name}
    rsp = api_call(session_uuid, "org.zstack.kvm.APIUpdateKVMHostMsg", content)
    error_if_fail(rsp)
    print "\nsuccessfully update host: %s" % host_uuid

def delete_host(session_uuid, host_uuid):
    content = {"uuid" : host_uuid}
    rsp = api_call(session_uuid, "org.zstack.header.host.APIDeleteHostMsg", content)
    error_if_fail(rsp)
    print "\nsuccessfully delete host: %s" % host_uuid

if __name__ == '__main__':
    session_uuid = login()
    zone_uuid = create_zone(session_uuid, 'zone1')
    cluster_uuid = create_cluster(session_uuid, zone_uuid, 'cluster1', 'KVM')
    host_uuid = add_host(session_uuid, cluster_uuid, "127.0.0.1","test-host", "root", "linux123", "22")
    query_host(session_uuid, [])
    update_host(session_uuid, host_uuid, "host2")
    delete_host(session_uuid, host_uuid)
    delete_cluster(session_uuid, cluster_uuid)
    delete_zone(session_uuid, zone_uuid)
    logout(session_uuid)