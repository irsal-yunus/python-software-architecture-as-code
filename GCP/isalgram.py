from diagrams import Cluster, Diagram
from diagrams.gcp.security import KeyManagementService
from diagrams.gcp.compute import ComputeEngine, KubernetesEngine
from diagrams.gcp.network import FirewallRules, LoadBalancing
# from diagrams.gcp.api import Endpoints, _API
from diagrams.gcp.database import Bigtable, SQL
# from diagrams.gcp.analytics import Dataflow
# from diagrams.gcp.ml import AIPlatformDataLabelingService
from diagrams.gcp.storage import Storage, Filestore


with Diagram("K8s Cluster Developement", show="false"):
    F5 =FirewallRules("F5")
    LB1 =LoadBalancing("LB")

    with Cluster("GKE Services"):
        svc_groups = [
            KubernetesEngine("GKE_A"),
            KubernetesEngine("GKE_B"),
            KubernetesEngine("GKE_C")
            ]
    LB2 =LoadBalancing("LB")

    with Cluster("App Service Cluster"):
        handlers = [
            ComputeEngine("App Service Cluster1"),
            ComputeEngine("App Service Cluster2"),
            ComputeEngine("App Service Cluster3")
        ]
    memchaced = SQL("score board")
    store = Storage("My Cool log bucket")

    with Cluster("SQL Cluster"):
        db_master = SQL("Master")
        db_master = [SQL("Slave1"), SQL("Slave2")]

    F5 >> LB1 >> svc_groups >> LB2 >> handlers
    handlers[0] >> memchaced
    handlers[1] >> store
    handlers[2] >> db_master