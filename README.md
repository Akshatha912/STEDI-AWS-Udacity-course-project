Project Introduction: STEDI Human Balance Analytics

In this project, we act as a data engineer for the STEDI team to build a data lakehouse solution for sensor data that trains a machine learning model.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.
The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Project Summary
As a data engineer on the STEDI Step Trainer team, we'll need to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.
<img width="593" height="266" alt="image" src="https://github.com/user-attachments/assets/a11d1ef0-4aee-42f0-a9fc-761002f21dcf" />

Implementation
Landing Zone

Glue tables:
customer_landing.sql
accelerometer_landing.sql

Athena: Landing Zone data query results

Trusted Zone
Glue job scripts:
customer_landing to trusted.py
accelerometer_landing to trusted.py

Athena: trusted zone query results

Curated Zone

customer_trusted to curated.py
step_trainer_trusted to curated.py
