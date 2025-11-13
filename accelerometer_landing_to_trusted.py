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

# Load landing accelerometer data
accelerometer_landing = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_landing"
)

# Load trusted customer data
customer_trusted = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_trusted"
)

# Join accelerometer readings to only include customers with consent
joined_data = Join.apply(
    frame1=accelerometer_landing,
    frame2=customer_trusted,
    keys1=["user"],  # "user" in accelerometer matches "email" in customer
    keys2=["email"]
)

# Keep only accelerometer columns
accelerometer_trusted = joined_data.select_fields(["user", "timestamp", "x", "y", "z"])

# Write trusted data
glueContext.write_dynamic_frame.from_options(
    frame=accelerometer_trusted,
    connection_type="s3",
    connection_options={"path": "s3://project-stedi-customer-landing-bucket/accelerometer/trusted/"},
    format="json"
)

job.commit()
