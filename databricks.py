# databricks.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.azure.analytics import Databricks
from diagrams.azure.compute import AKS
from diagrams.azure.database import DataLake
from diagrams.azure.security import KeyVaults

with Diagram("Migration", show=False):
    Databricks("Databricks") >> [ DataLake("DataLake") , KeyVaults("Vault") ]
