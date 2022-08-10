# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.azure.compute import AKS
from diagrams.azure.analytics import Databricks

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> AKS("AKS") >> Databricks("Databricks")
