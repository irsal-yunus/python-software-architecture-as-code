from diagrams import Cluster, Diagram
from diagrams.gcp.security import KeyManagementService
from diagrams.gcp.network import DNS, FirewallRules, LoadBalancing
from diagrams.gcp.compute import GKEOnPrem , ContainerOptimizedOS , Functions
from diagrams.gcp.analytics import Dataflow
from diagrams.gcp.database import Bigtable, SQL
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.storage import Storage, Filestore

with Diagram("K8s Onpremise Developement", show="false"):
    dns =DNS("DNS")
    F5 =FirewallRules("F5")

    with Cluster("GKE Onpremise Services"):
        sec_groups = [
            GKEOnPrem("GKE_A"),
            GKEOnPrem("GKE_B"),
            GKEOnPrem("GKE_C")
        ]
        svc_groups = [
            GKEOnPrem("GKE_A"),
            GKEOnPrem("GKE_B"),
            GKEOnPrem("GKE_C")
            ]
    LB =LoadBalancing("LB")

    with Cluster("Container Service K8s"):
        handlers = [
            ContainerOptimizedOS("Nginx Service"),
            ContainerOptimizedOS("MS Service1"),
            ContainerOptimizedOS("MS Service2"),
            ContainerOptimizedOS("MS Service3"),
            ContainerOptimizedOS("MS Service4"),
            ContainerOptimizedOS("MS Service5")
        ]
    memchaced = Dataflow("score board")
    store1 = Storage("Storage log bucket")
    store2 = Monitoring("Monitoring Tools")

    with Cluster("SQL Cluster"):
        db_master = SQL("Master")
        db_master = [SQL("Slave1"), SQL("Slave2")]

    DNS >> F5 >> svc_groups >> LB >> handlers
    handlers[0] >> memchaced
    handlers[1] >> store1 >> store2
    handlers[2] >> db_master >> store2
