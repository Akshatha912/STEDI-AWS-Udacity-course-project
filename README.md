Project Introduction: STEDI Human Balance Analytics

In this project, we act as a data engineer for the STEDI team to build a data lakehouse solution for sensor data that trains a machine learning model.

What is STEDI?

STEDI (short for Step Trainer for Enhancing Dynamic Imbalance) is a conceptual company that has developed a Step Trainer device — a hardware sensor that helps users improve their physical balance.
The device:
Detects the distance of movement using motion sensors.
Works with a mobile app that collects accelerometer data (motion in X, Y, Z directions).
Together, they generate IoT data streams that reflect how a user moves and balances.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.
The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Project Summary
As a data engineer on the STEDI Step Trainer team, we'll need to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.
<img width="593" height="266" alt="image" src="https://github.com/user-attachments/assets/a11d1ef0-4aee-42f0-a9fc-761002f21dcf" />

Implementation
1) Landing Zone - get raw data to S3 bucket

customer_landing

accelerometer_landing

step_trainer_landing

2) Trusted zone - Glue tables:

customer_landing_to_trusted.py - removed customers who were not willing to share their data (share With ResearchAsoFDate)

accelerometer_landing_to_trusted.py - join accelerometer-landing and customer_trusted (on user and email as keys) to include only customers with consent

step_trainer_landing_to_trusted,py - remove serialnumber column with null values

Athena: trusted zone query results

3) Curated Zone - 

customer_trusted_to_curated.py - join accelerometer_trusted and customer_trusted (on user and email as keys) to include only required fields ("customerName", "email", "serialNumber", "birthDay", "registrationDate")

machine_learning_curated.py - join step_trainer_trusted and accelerometer_trusted (on sensorReadingTime and timeStamp as keys) which makes this data ready for analysis.
