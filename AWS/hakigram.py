from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS,Lambda
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("CLustered web services", show="false"):
    dns =Route53("dns")
    lb =ELB("App load balancer")

    with Cluster("ECS Services"):
        svc_groups = [
            ECS("ServiceA"),
            ECS("ServiceB"),
            ECS("ServiceC")
            ]
    queue = SQS("SQS Service")

    with Cluster("Lambdas"):
        handlers = [
            Lambda("Lambda1"),
            Lambda("Lambda2"),
            Lambda("Lambda3")
        ]

    memchaced = ElastiCache("score board")
    store = S3("My Cool log bucket")

    with Cluster("RDS Cluster"):
        db_master = RDS("GameDB")
        db_master = [RDS("GameDBRO"), RDS("GameDBRO2")]

    dns >> lb >> svc_groups >> queue >> handlers
    handlers[0] >> memchaced
    handlers[1] >> store
    handlers[2] >> db_master