from diagrams import Cluster, Diagram

from diagrams.onprem.client import User
from diagrams.aws.compute import EC2
from diagrams.aws.network import Route53
from diagrams.aws.database import RDS

with Diagram("100 User Architecture", show=True):
    route_53 = Route53("dns")
    with Cluster("AWS"):
        route_53 >> EC2("Web Server") >> RDS("Database")
    User("User") >> route_53