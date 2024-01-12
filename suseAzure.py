min_sle15_rpms = {
    'cloud-regionsrv-client'              : ('9.1.3'  , '6.37.1' ),
    'cloud-regionsrv-client-plugin-azure' : ('1.0.1'  , '6.26.4' ),
    'libxslt1'                            : ('1.1.32' , '3.3.1'  ),
    'python3-azuremetadata'               : ('5.1.5'  , '1.23.1' ),
    'python3-cssselect'                   : ('1.0.3'  , '1.18'   ),
    'python3-dnspython'                   : ('1.15.0' , '1.25'   ),
    'python3-lxml'                        : ('4.0.0'  , '2.26'   ),
    'python3-M2Crypto'                    : ('0.35.2' , '3.6.1'  ),
    'python3-zypp-plugin'                 : ('0.6.3'  , '2.18'   ),
    'regionServiceClientConfigAzure'      : ('1.0.5'  , '3.13.4' )
}

min_sle12_rpms = {
    'cloud-regionsrv-client'			:	('9.3'       , '52.44.1'),
    'cloud-regionsrv-client-plugin-azure'	:	('1.0.1'     , '52.33.1'),
    'libopenssl1_0_0'				:	('1.0.2p'    , '2.11'),
    'libpython3_4m1_0'				:	('3.4.10'    , '25.45.1'),
    'libxslt1'					:	('1.1.28'    , '6.57'),
    'python3'					:	('3.4.6'     , '24.1'),
    'python3-asn1crypto'			:	('0.24.0'    , '2.5.1'),
    'python3-azuremetadata'			:	('5.1.4'     , '1.18.1'),
    'python3-base'				:	('3.4.6'     , '24.1'),
    'python3-certifi'				:	('2018.4.16' , '3.3.1'),
    'python3-cffi'				:	('1.11.2'    , '2.19.2'),
    'python3-chardet'				:	('3.0.4'     , '5.3.2'),
    'python3-cryptography'			:	('2.1.4'     , '7.28.2'),
    'python3-cssselect'				:	('0.8'       , '3.2.1'),
    'python3-dnspython'				:	('1.12.0'    , '9.8.1'),
    'python3-idna'				:	('2.5'       , '3.10.2'),
    'python3-lxml'				:	('3.3.5'     , '3.4.1'),
    'python3-M2Crypto'				:	('0.29.0'    , '23.3.5'),
    'python3-packaging'				:	('17.1'      , '2.5.1'),
    'python3-pip'				:	('10.0.1'    , '11.6.1'),
    'python3-py'				:	('1.5.2'     , '8.8.2'),
    'python3-pyasn1'				:	('0.1.9'     , '4.6.1'),
    'python3-pycparser'				:	('2.10'      , '5.3.1'),
    'python3-pyOpenSSL'				:	('17.1.0'    , '4.23.1'),
    'python3-pyparsing'				:	('2.2.0'     , '3.3.1'),
    'python3-PySocks'				:	('1.6.8'     , '3.3.1'),
    'python3-requests'				:	('2.11.1'    , '6.25.1'),
    'python3-setuptools'			:	('18.0.1'    , '4.3.1'),
    'python3-six'				:	('1.11.0'    , '9.21.2'),
    'python3-typing'				:	('3.6.4'     , '1.3.1'),
    'python3-urllib3'				:	('1.22'      , '3.17.1'),
    'python3-zypp-plugin'			:	('0.6.3'     , '3.3.1'),
    'regionServiceClientConfigAzure'		:	('1.0.5'     , '3.12.1')
}

pint_data = {}
pint_data["azure"] = \
    """
[
    {
      "ip": "51.4.145.155",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "Germany Central",
      "type": "smt-sles"
    },
    {
      "ip": "51.4.145.156",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "Germany Central",
      "type": "smt-sles"
    },
    {
      "ip": "51.5.145.14",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "Germany Northeast",
      "type": "smt-sles"
    },
    {
      "ip": "51.5.145.15",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "Germany Northeast",
      "type": "smt-sles"
    },
    {
      "ip": "23.101.216.104",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral",
      "type": "smt"
    },
    {
      "ip": "23.101.210.206",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral",
      "type": "smt"
    },
    {
      "ip": "13.70.94.71",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral",
      "type": "smt"
    },
    {
      "ip": "23.101.235.14",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral2",
      "type": "smt"
    },
    {
      "ip": "23.101.231.234",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral2",
      "type": "smt"
    },
    {
      "ip": "13.73.107.146",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiacentral2",
      "type": "smt"
    },
    {
      "ip": "23.101.216.104",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiaeast",
      "type": "smt"
    },
    {
      "ip": "23.101.210.206",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiaeast",
      "type": "smt"
    },
    {
      "ip": "13.70.94.71",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiaeast",
      "type": "smt"
    },
    {
      "ip": "23.101.235.14",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiasoutheast",
      "type": "smt"
    },
    {
      "ip": "23.101.231.234",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiasoutheast",
      "type": "smt"
    },
    {
      "ip": "13.73.107.146",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "australiasoutheast",
      "type": "smt"
    },
    {
      "ip": "191.237.255.212",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsouth",
      "type": "smt"
    },
    {
      "ip": "191.237.253.40",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsouth",
      "type": "smt"
    },
    {
      "ip": "191.235.81.180",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsouth",
      "type": "smt"
    },
    {
      "ip": "191.237.255.212",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsoutheast",
      "type": "smt"
    },
    {
      "ip": "191.237.253.40",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsoutheast",
      "type": "smt"
    },
    {
      "ip": "191.235.81.180",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "brazilsoutheast",
      "type": "smt"
    },
    {
      "ip": "40.85.225.32",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadacentral",
      "type": "smt"
    },
    {
      "ip": "40.85.225.240",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadacentral",
      "type": "smt"
    },
    {
      "ip": "52.228.41.50",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadacentral",
      "type": "smt"
    },
    {
      "ip": "40.86.231.97",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadaeast",
      "type": "smt"
    },
    {
      "ip": "40.86.231.128",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadaeast",
      "type": "smt"
    },
    {
      "ip": "52.229.125.108",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "canadaeast",
      "type": "smt"
    },
    {
      "ip": "40.66.32.54",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralfrance",
      "type": "smt"
    },
    {
      "ip": "40.66.41.99",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralfrance",
      "type": "smt"
    },
    {
      "ip": "40.66.48.231",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralfrance",
      "type": "smt"
    },
    {
      "ip": "104.211.97.78",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralindia",
      "type": "smt"
    },
    {
      "ip": "104.211.98.58",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralindia",
      "type": "smt"
    },
    {
      "ip": "52.172.187.74",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralindia",
      "type": "smt"
    },
    {
      "ip": "13.86.112.4",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralus",
      "type": "smt"
    },
    {
      "ip": "52.165.88.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralus",
      "type": "smt"
    },
    {
      "ip": "13.86.104.2",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centralus",
      "type": "smt"
    },
    {
      "ip": "13.86.112.4",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centraluseuap",
      "type": "smt"
    },
    {
      "ip": "52.165.88.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centraluseuap",
      "type": "smt"
    },
    {
      "ip": "13.86.104.2",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "centraluseuap",
      "type": "smt"
    },
    {
      "ip": "23.101.14.157",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast",
      "type": "smt"
    },
    {
      "ip": "23.101.3.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast",
      "type": "smt"
    },
    {
      "ip": "13.75.123.198",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast",
      "type": "smt"
    },
    {
      "ip": "23.101.14.157",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast2",
      "type": "smt"
    },
    {
      "ip": "23.101.3.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast2",
      "type": "smt"
    },
    {
      "ip": "13.75.123.198",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinaeast2",
      "type": "smt"
    },
    {
      "ip": "23.101.14.157",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth",
      "type": "smt"
    },
    {
      "ip": "23.101.3.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth",
      "type": "smt"
    },
    {
      "ip": "13.75.123.198",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth",
      "type": "smt"
    },
    {
      "ip": "23.101.14.157",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth2",
      "type": "smt"
    },
    {
      "ip": "23.101.3.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth2",
      "type": "smt"
    },
    {
      "ip": "13.75.123.198",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "chinanorth2",
      "type": "smt"
    },
    {
      "ip": "23.101.14.157",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastasia",
      "type": "smt"
    },
    {
      "ip": "23.101.3.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastasia",
      "type": "smt"
    },
    {
      "ip": "13.75.123.198",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastasia",
      "type": "smt"
    },
    {
      "ip": "52.188.224.179",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus",
      "type": "smt"
    },
    {
      "ip": "52.188.81.163",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus",
      "type": "smt"
    },
    {
      "ip": "52.186.168.210",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus",
      "type": "smt"
    },
    {
      "ip": "52.147.176.11",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2",
      "type": "smt"
    },
    {
      "ip": "20.186.88.79",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2",
      "type": "smt"
    },
    {
      "ip": "20.186.112.116",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2",
      "type": "smt"
    },
    {
      "ip": "52.147.176.11",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2euap",
      "type": "smt"
    },
    {
      "ip": "20.186.88.79",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2euap",
      "type": "smt"
    },
    {
      "ip": "20.186.112.116",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "eastus2euap",
      "type": "smt"
    },
    {
      "ip": "40.66.32.54",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francecentral",
      "type": "smt"
    },
    {
      "ip": "40.66.41.99",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francecentral",
      "type": "smt"
    },
    {
      "ip": "40.66.48.231",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francecentral",
      "type": "smt"
    },
    {
      "ip": "51.116.98.203",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanycentral",
      "type": "smt"
    },
    {
      "ip": "51.116.98.214",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanycentral",
      "type": "smt"
    },
    {
      "ip": "51.116.96.37",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanycentral",
      "type": "smt"
    },
    {
      "ip": "51.116.98.203",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynorth",
      "type": "smt"
    },
    {
      "ip": "51.116.98.214",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynorth",
      "type": "smt"
    },
    {
      "ip": "51.116.96.37",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynorth",
      "type": "smt"
    },
    {
      "ip": "51.116.98.203",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynortheast",
      "type": "smt"
    },
    {
      "ip": "51.116.98.214",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynortheast",
      "type": "smt"
    },
    {
      "ip": "51.116.96.37",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanynortheast",
      "type": "smt"
    },
    {
      "ip": "51.116.98.203",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanywestcentral",
      "type": "smt"
    },
    {
      "ip": "51.116.98.214",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanywestcentral",
      "type": "smt"
    },
    {
      "ip": "51.116.96.37",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "germanywestcentral",
      "type": "smt"
    },
    {
      "ip": "52.185.185.83",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japaneast",
      "type": "smt"
    },
    {
      "ip": "40.81.208.103",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japaneast",
      "type": "smt"
    },
    {
      "ip": "40.81.200.4",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japaneast",
      "type": "smt"
    },
    {
      "ip": "104.46.239.62",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japanwest",
      "type": "smt"
    },
    {
      "ip": "104.46.239.65",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japanwest",
      "type": "smt"
    },
    {
      "ip": "40.74.120.164",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "japanwest",
      "type": "smt"
    },
    {
      "ip": "52.231.39.82",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreacentral",
      "type": "smt"
    },
    {
      "ip": "52.231.39.83",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreacentral",
      "type": "smt"
    },
    {
      "ip": "52.231.34.241",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreacentral",
      "type": "smt"
    },
    {
      "ip": "52.231.201.188",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreasouth",
      "type": "smt"
    },
    {
      "ip": "52.231.201.178",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreasouth",
      "type": "smt"
    },
    {
      "ip": "52.231.202.220",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "koreasouth",
      "type": "smt"
    },
    {
      "ip": "23.101.164.199",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northcentralus",
      "type": "smt"
    },
    {
      "ip": "23.101.171.119",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northcentralus",
      "type": "smt"
    },
    {
      "ip": "23.96.231.74",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northcentralus",
      "type": "smt"
    },
    {
      "ip": "52.158.42.90",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northeurope",
      "type": "smt"
    },
    {
      "ip": "13.79.120.39",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northeurope",
      "type": "smt"
    },
    {
      "ip": "52.155.248.41",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "northeurope",
      "type": "smt"
    },
    {
      "ip": "51.120.2.195",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwayeast",
      "type": "smt"
    },
    {
      "ip": "51.120.0.31",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwayeast",
      "type": "smt"
    },
    {
      "ip": "51.120.2.159",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwayeast",
      "type": "smt"
    },
    {
      "ip": "51.120.2.195",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwaywest",
      "type": "smt"
    },
    {
      "ip": "51.120.0.31",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwaywest",
      "type": "smt"
    },
    {
      "ip": "51.120.2.159",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "norwaywest",
      "type": "smt"
    },
    {
      "ip": "102.133.128.124",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricanorth",
      "type": "smt"
    },
    {
      "ip": "102.133.128.67",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricanorth",
      "type": "smt"
    },
    {
      "ip": "102.133.129.51",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricanorth",
      "type": "smt"
    },
    {
      "ip": "102.133.128.124",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricawest",
      "type": "smt"
    },
    {
      "ip": "102.133.128.67",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricawest",
      "type": "smt"
    },
    {
      "ip": "102.133.129.51",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southafricawest",
      "type": "smt"
    },
    {
      "ip": "23.101.186.158",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralus",
      "type": "smt"
    },
    {
      "ip": "23.101.188.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralus",
      "type": "smt"
    },
    {
      "ip": "13.65.81.103",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralus",
      "type": "smt"
    },
    {
      "ip": "23.101.186.158",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralusstg",
      "type": "smt"
    },
    {
      "ip": "23.101.188.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralusstg",
      "type": "smt"
    },
    {
      "ip": "13.65.81.103",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southcentralusstg",
      "type": "smt"
    },
    {
      "ip": "52.230.96.47",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southeastasia",
      "type": "smt"
    },
    {
      "ip": "52.237.80.2",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southeastasia",
      "type": "smt"
    },
    {
      "ip": "52.139.216.51",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southeastasia",
      "type": "smt"
    },
    {
      "ip": "40.66.32.54",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francesouth",
      "type": "smt"
    },
    {
      "ip": "40.66.41.99",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francesouth",
      "type": "smt"
    },
    {
      "ip": "40.66.48.231",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "francesouth",
      "type": "smt"
    },
    {
      "ip": "104.211.227.174",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southindia",
      "type": "smt"
    },
    {
      "ip": "104.211.227.169",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southindia",
      "type": "smt"
    },
    {
      "ip": "52.172.51.125",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "southindia",
      "type": "smt"
    },
    {
      "ip": "51.107.0.120",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandnorth",
      "type": "smt"
    },
    {
      "ip": "51.107.0.121",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandnorth",
      "type": "smt"
    },
    {
      "ip": "51.107.0.122",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandnorth",
      "type": "smt"
    },
    {
      "ip": "51.107.0.120",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandwest",
      "type": "smt"
    },
    {
      "ip": "51.107.0.121",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandwest",
      "type": "smt"
    },
    {
      "ip": "51.107.0.122",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "switzerlandwest",
      "type": "smt"
    },
    {
      "ip": "20.46.144.230",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaenorth",
      "type": "smt"
    },
    {
      "ip": "20.46.144.239",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaenorth",
      "type": "smt"
    },
    {
      "ip": "20.46.146.20",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaenorth",
      "type": "smt"
    },
    {
      "ip": "20.46.144.230",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaecentral",
      "type": "smt"
    },
    {
      "ip": "20.46.144.239",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaecentral",
      "type": "smt"
    },
    {
      "ip": "20.46.146.20",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uaecentral",
      "type": "smt"
    },
    {
      "ip": "51.141.12.56",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uknorth",
      "type": "smt"
    },
    {
      "ip": "51.141.12.57",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uknorth",
      "type": "smt"
    },
    {
      "ip": "51.141.11.221",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uknorth",
      "type": "smt"
    },
    {
      "ip": "20.39.208.99",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth",
      "type": "smt"
    },
    {
      "ip": "20.39.216.18",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth",
      "type": "smt"
    },
    {
      "ip": "20.39.224.10",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth",
      "type": "smt"
    },
    {
      "ip": "20.39.208.99",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth2",
      "type": "smt"
    },
    {
      "ip": "20.39.216.18",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth2",
      "type": "smt"
    },
    {
      "ip": "20.39.224.10",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "uksouth2",
      "type": "smt"
    },
    {
      "ip": "51.141.12.56",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "ukwest",
      "type": "smt"
    },
    {
      "ip": "51.141.12.57",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "ukwest",
      "type": "smt"
    },
    {
      "ip": "51.141.11.221",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "ukwest",
      "type": "smt"
    },
    {
      "ip": "52.161.26.245",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westcentralus",
      "type": "smt"
    },
    {
      "ip": "52.161.27.73",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westcentralus",
      "type": "smt"
    },
    {
      "ip": "52.161.26.42",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westcentralus",
      "type": "smt"
    },
    {
      "ip": "104.211.161.139",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westindia",
      "type": "smt"
    },
    {
      "ip": "104.211.161.138",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westindia",
      "type": "smt"
    },
    {
      "ip": "104.211.166.161",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westindia",
      "type": "smt"
    },
    {
      "ip": "52.149.120.86",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westeurope",
      "type": "smt"
    },
    {
      "ip": "51.145.209.119",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westeurope",
      "type": "smt"
    },
    {
      "ip": "52.157.241.14",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westeurope",
      "type": "smt"
    },
    {
      "ip": "23.100.46.123",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus",
      "type": "smt"
    },
    {
      "ip": "23.101.192.253",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus",
      "type": "smt"
    },
    {
      "ip": "40.112.248.207",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus",
      "type": "smt"
    },
    {
      "ip": "40.90.192.185",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus2",
      "type": "smt"
    },
    {
      "ip": "52.148.152.22",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus2",
      "type": "smt"
    },
    {
      "ip": "52.156.104.18",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus2",
      "type": "smt"
    },
    {
      "ip": "20.38.0.87",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus3",
      "type": "smt"
    },
    {
      "ip": "20.38.1.19",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus3",
      "type": "smt"
    },
    {
      "ip": "20.38.0.31",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "westus3",
      "type": "smt"
    },
    {
      "ip": "23.101.164.199",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodcentral",
      "type": "smt"
    },
    {
      "ip": "23.101.171.119",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodcentral",
      "type": "smt"
    },
    {
      "ip": "23.96.231.74",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodcentral",
      "type": "smt"
    },
    {
      "ip": "52.188.224.179",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodeast",
      "type": "smt"
    },
    {
      "ip": "52.188.81.163",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodeast",
      "type": "smt"
    },
    {
      "ip": "52.186.168.210",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usdodeast",
      "type": "smt"
    },
    {
      "ip": "52.161.26.245",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovarizona",
      "type": "smt"
    },
    {
      "ip": "52.161.27.73",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovarizona",
      "type": "smt"
    },
    {
      "ip": "52.161.26.42",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovarizona",
      "type": "smt"
    },
    {
      "ip": "13.86.112.4",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgoviowa",
      "type": "smt"
    },
    {
      "ip": "52.165.88.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgoviowa",
      "type": "smt"
    },
    {
      "ip": "13.86.104.2",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgoviowa",
      "type": "smt"
    },
    {
      "ip": "23.101.186.158",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovtexas",
      "type": "smt"
    },
    {
      "ip": "23.101.188.13",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovtexas",
      "type": "smt"
    },
    {
      "ip": "13.65.81.103",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovtexas",
      "type": "smt"
    },
    {
      "ip": "52.147.176.11",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovvirginia",
      "type": "smt"
    },
    {
      "ip": "20.186.88.79",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovvirginia",
      "type": "smt"
    },
    {
      "ip": "20.186.112.116",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "usgovvirginia",
      "type": "smt"
    },
    {
      "ip": "51.120.2.195",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedencentral",
      "type": "smt"
    },
    {
      "ip": "51.120.0.31",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedencentral",
      "type": "smt"
    },
    {
      "ip": "51.120.2.159",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedencentral",
      "type": "smt"
    },
    {
      "ip": "51.120.2.195",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedensouth",
      "type": "smt"
    },
    {
      "ip": "51.120.0.31",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedensouth",
      "type": "smt"
    },
    {
      "ip": "51.120.2.159",
      "ipv6": "",
      "name": "smt-azure.susecloud.net",
      "region": "swedensouth",
      "type": "smt"
    }
  ]
"""
