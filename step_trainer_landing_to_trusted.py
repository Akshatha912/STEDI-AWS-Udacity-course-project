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

# Read step trainer landing data
step_trainer_landing = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_landing"
)

# (Optional) Filter for valid serial numbers
step_trainer_trusted = Filter.apply(
    frame=step_trainer_landing,
    f=lambda x: x["serialNumber"] is not None
)

# Write to trusted zone
glueContext.write_dynamic_frame.from_options(
    frame=step_trainer_trusted,
    connection_type="s3",
    connection_options={"path": "s3://project-stedi-customer-landing-bucket/step_trainer/trusted/"},
    format="json"
)

job.commit()
