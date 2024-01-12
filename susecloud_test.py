#!/usr/bin/env python3

import json
import logging
import os
import re
import socket
import sys
import subprocess
import requests
import rpm
import suseAzure

class MINRPM:
    def __init__(self):
        oslevel = subprocess.Popen('rpm -q --file /etc/os-release --queryformat "%{VERSION}"  ',
            shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.osversion = oslevel.stdout.read().decode('utf-8').rstrip()
        logging.critical(self.osversion)

    def min_sle_rpms(self):
        if re.match('^15', self.osversion):
            return suseAzure.min_sle15_rpms

        if re.match('^12', self.osversion):
            return suseAzure.min_sle12_rpms


def get_rmt_servers(region):
    """Get RMT servers for region in particular framework."""
    rmt_servers = []
    rmt_dict = json.loads(suseAzure.pint_data['azure'])
    for server in rmt_dict:
        if server['region'] == region:
            rmt_servers.append(server['ip'])
    return rmt_servers

def localcompare(t1, t2):
    v1, r1 = t1
    v2, r2 = t2

    return rpm.labelCompare( ("", v1, r1), ("", v2, r2) )

def rpm_info():
    rpm_info = dict()
    logging.info("executing 'rpm -qa --queryformat %s", "'%{NAME}:%{VERSION}:%{RELEASE}'")
    rpmqa = subprocess.Popen('rpm -qa --queryformat "%{NAME}:%{VERSION}:%{RELEASE}\n"',
        shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for pkg in rpmqa.stdout.read().decode('utf-8').rstrip().split('\n'):
        info = pkg.split(':')
        logging.debug("rpm is %s and info is %s", pkg, info)
        rpm_info[info[0]] = (info[1],info[2])
    return rpm_info

def rpmcheck():
    myrpms = rpm_info()
    errors = 0


    rpminfo = MINRPM()
    min_sle_rpms = rpminfo.min_sle_rpms()

    for name in min_sle_rpms.keys():
        try:
            if localcompare(myrpms[name], suseAzure.min_sle15_rpms[name]) < 0:
                errors = 1
        except KeyError:
            logging.error("%s rpm not installed in system, \
                          follow directions to install offline updates", name)
            errors = 1

        if errors:
            logging.error("%s rpm lower level than required, \
                          follow directions to install offline updates", name)
            logging.error("refer to the following links for further information:")
            logging.error("\thttps://www.suse.com/support/kb/doc/?id=000019633")
            logging.error("\t\
                          https://www.suse.com/c/suse-linux-enterprise-and-azure-hybrid-benefit/")

def check_metadata():
    '''Metadata access is required. Check metadata is accessible.
    Return instance region if successful'''
    metadata_base_url = "http://169.254.169.254"
    logging.info("Checking metadata access.")
    instance_api_version = "2019-03-11"
    instance_endpoint = metadata_base_url + \
        "/metadata/instance/compute/location?api-version=" + \
        instance_api_version + "&format=text"
    headers = {'Metadata': 'True'}
    try:
        logging.debug("checking metadata at %s", instance_endpoint)
        r = requests.get(instance_endpoint, headers=headers, timeout=5)
        if r.status_code == 200:
            logging.info("SUCCESS: connected to Azure Metadata")
    except:
        logging.error("PROBLEM: Metadata is not accessible. \
                      Fix access to metadata at 169.254.169.254.")
        logging.error("this is usually due to problems with internal firewalls or proxies")
        logging.error("access to the metadata server should not be blocked \
                      or tunneled through a proxy server")
        sys.exit(1)

    return r.text


def read_regionserverclnt():
    etc_regionserverclnt = "/etc/regionserverclnt.cfg"
    try:
        with open(etc_regionserverclnt, 'r') as regionserverclnt_file:
            content = regionserverclnt_file.readlines()
    except FileNotFoundError:
        logging.error("%s File not found. Cannot continue.", etc_regionserverclnt)
        sys.exit(1)
    return content


def check_region_servers(region):
    """Check if the instance has access to one region server over https"""
    to_cnt = se_cnt = re_cnt = 0

    logging.info("Checking regionserver access.")
    content = read_regionserverclnt()
    for entry in content:
        if re.match('^#', entry):
            next
        if "regionsrv" in entry:
            region_servers = entry.rsplit()[2]
        if "certLocation" in entry:
            cert_dir = entry.rsplit()[2]

    if not region_servers or not cert_dir:
        logging.error("regionsrv or certLocation entry \
                      not found in /etc/regionserverclnt.cfg. Cannot continue.")
        sys.exit(1)

    # check cert_dir path
    if os.path.exists(cert_dir):
        logging.info("Certificate location is %s", cert_dir)
    else:
        logging.error("%s path does not exist, \
                      please reinstall regionServiceClientConfigAzure", cert_dir)
        sys.exit(1)

    for region_server in region_servers.split(','):
        certfile = cert_dir + '/' + region_server + '.pem'
        try:
            r = requests.get('https://' + region_server +
                         '/regionInfo?regionHint=' + region, verify=certfile, timeout=5)
        except requests.exceptions.Timeout:
            logging.warning("PROBLEM: NO access to region server. \
                            Open port 443 to region server %s", region_server)
            to_cnt += 1

        except requests.exceptions.SSLError:
            logging.warning("PROBLEM: MITM proxy misconfiguration. \
                            Proxy cannot intercept certs for %s.", region_server)
            se_cnt += 1

        except requests.exceptions.RequestException:
            logging.warning("PROBLEM: Unable to establish communication with server %s, \
                            please allow SSL traffic to it", region_server)
            re_cnt += 1
        else:
            if r.status_code == 200:
                logging.info("SUCCESS: Connected to region_server %s", region_server)

    regsrv_cnt = len(region_servers)

    if to_cnt == regsrv_cnt:
        logging.error("Cannot communicate with any of the region server, \
                      you must allow at least one")
        sys.exit(1)

    if se_cnt == regsrv_cnt:
        logging.warning("PROBLEM: MITM proxy misconfiguration. Exempt at least one region server.")
        sys.exit(1)

    if re_cnt == regsrv_cnt:
        logging.warning("PROBLEM: No access to a region server.")
        logging.warning("Region Server IPs: %s", region_servers)

def check_current_rmt(rmt_servers):
    """Check if current smt server in /etc/hosts is region correct"""
    domain_name = "smt-azure.susecloud.net"
    logging.info("Checking RMT server entry is for correct region.")

    try:
        if socket.gethostbyname(domain_name) in rmt_servers:
            logging.info("RMT server entry OK.")
    except:
        logging.error("Cannot get IP of RMT server entry.")
        sys.exit(1)
    else:
        if not socket.gethostbyname(domain_name) in rmt_servers:
            logging.error("PROBLEM: RMT server entry is for wrong region, \
                          one of the following hosts needs to be added to your server")
            logging.error("Update the smt-azure.susecloud.net entry, \
                          with one of the following IP address")
            for server in rmt_servers:
                logging.error("%s        smt-azure.susecloud.net", server)
            sys.exit(1)

    ipaddr =  socket.gethostbyname(domain_name)
    logging.debug("Returning %s for smt-azure.susecloud.com", ipaddr)
    return ipaddr

def check_rmt_servers(location):
    """Check https cert"""

    rmt_servers = get_rmt_servers(location)
    rmt_server = check_current_rmt(rmt_servers)

    logging.info("Checking https access using RMT certs.")
    certfiles = [filename for filename in os.listdir(
        '/etc/pki/trust/anchors') if filename.startswith("registration_server")]

    logging.debug("certfile is %s", certfiles)

    try:
        url = 'https://smt-azure.susecloud.net/api/health/status'
        logging.debug('Using the following link to verify the RMT server %s', url)
        r = requests.get(url, verify='/etc/pki/trust/anchors/'+certfiles[0], timeout=5)
        if r.status_code == 200:
            logging.info("SUCCESS: Connected to smt-azure.susecloud.net")
    except requests.exceptions.SSLError:
        logging.error("PROBLEM: MITM proxy misconfiguration. \
                      Proxy cannot intercept RMT certs. Exempt %s.", rmt_server)
        sys.exit(1)
    except requests.exceptions.Timeout:
        logging.error("PROBLEM: NO access to RMT server. \
                      Open port 443 to RMT server %s", rmt_server)
        sys.exit(1)


    except Exception as ex:
        template = "An exception of type {0} occurred."
        message = template.format(type(ex).__name__, ex.args)
        logging.error("%s stopping.", message)
        sys.exit(1)


def main():
    ''' Main execution, it should always land here if executed from a unix shell '''
    logging.basicConfig(level=logging.INFO)
    rpmcheck()
    location = check_metadata()
    check_region_servers(location)
    check_rmt_servers(location)
    # if we're at this point, everything is good.
    logging.info("The script did not detect any issues with the server")

if __name__ == "__main__":
    main()
