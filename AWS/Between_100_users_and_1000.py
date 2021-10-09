from diagrams import Cluster, Diagram

from diagrams.onprem.client import User
from diagrams.aws.compute import EC2
from diagrams.aws.network import Route53, ElasticLoadBalancing
from diagrams.aws.database import RDS, ElastiCache

with Diagram("1000 User Architecture", show=True):
    with Cluster("AWS"):
        route_53 = Route53("dns")
        lb = ElasticLoadBalancing("lb")
        vm_group = [EC2("Web1"), EC2("Web2")]
        cache = ElastiCache("Redis Cache")
        route_53 >> lb >> vm_group >> cache >> RDS("Database")

    User("User") >> route_53