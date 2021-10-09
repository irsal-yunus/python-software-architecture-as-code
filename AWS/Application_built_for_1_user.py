import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/graphviz-2.49.1/windows/bin/'
from diagrams import Cluster, Diagram, Edge

from diagrams.onprem.client import User
from diagrams.aws.compute import Lightsail
from diagrams.aws.network import Route53

with Diagram("Single User Architecture", show=True, direction="TB"):
    with Cluster(""):
        route_53 = Route53("dns")
        with Cluster("AWS"):
            route_53 - Edge(label="Elastic IP", color="orange",
                            forward=True) >> Lightsail("Lightsail Server")
        User("User") >> route_53