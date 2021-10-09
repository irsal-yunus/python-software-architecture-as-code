from diagrams import Cluster, Diagram
from diagrams.onprem.client import User
from diagrams.aws.compute import EC2
from diagrams.aws.network import Route53, ElasticLoadBalancing, Cloudfront
from diagrams.aws.database import Aurora, ElastiCache
from diagrams.aws.storage import S3

with Diagram("10000 User Architecture", show=True):
    with Cluster("AWS"):
        route_53 = Route53("DNS")
        cloud_front = Cloudfront("CDN")
        s3 = S3("S3 Object Storage")
        lb = ElasticLoadBalancing("LB")
        cache = ElastiCache("Redis Cache")
        aurora_db = Aurora("Aurora DB")

        with Cluster("Availablity Zone 1"):
            vm_group1 = [EC2("Web1"), EC2("Web2")]
            lb >> vm_group1 >> cache >> aurora_db
        with Cluster("Availablity Zone 2"):
            vm_group2 = [EC2("Web3"), EC2("Web4")]
            lb >> vm_group2  >> cache >> aurora_db

        route_53 >> lb
        route_53 >> cloud_front >> s3

    User("User") >> route_53