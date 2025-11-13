import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read landing zone data
customer_landing = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_landing"
)

# Keep only customers who shared data for research
customer_trusted = Filter.apply(
    frame=customer_landing,
    f=lambda x: x["shareWithResearchAsOfDate"] is not None
)

# Write filtered data to trusted zone
glueContext.write_dynamic_frame.from_options(
    frame=customer_trusted,
    connection_type="s3",
    connection_options={"path": "s3://project-stedi-customer-landing-bucket/customer/trusted/"},
    format="json"
)

job.commit()
