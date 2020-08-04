# Patient Progress REST API 🚑

This REST API powers the backend side of the Patient Progress application which frontend written in JavaScript (React Native). Patient Progress was created during a month-long CFG Hack from Home 2020 Hackathon and it is an app that automates the process of updating emergency contacts of a patient via an interactive real-time feed.

Patient Progress was designed with the assumption that the medical data will be collected from existing NHS APIs and displayed on the interactive feed. However, for our hackathon demo, we made use of the Patient Progress REST API.

The Patient Progress REST API has no HTML interface and returns raw JSON data. That's kind of boring but you can check out preview of the demo down below.

# Use

There are two end points that are publicly available.

- **GET** Patients End Point `api/patients`
- **GET** Patient Detail `api/patients/<nhs_number>`

# Preview

<img src="images/preview.gif" height="100%" />

# Database Schema

![Database Schema](images/db.png)
<img src="images/db-schema.png" height="60%" />
