# Patient Progress REST API

## General info
This REST API written in Python powers the backend side of the Patient Progress app (front-end was developed using JavaScript, React Native). Patient Progress was created during a month-long CFG Hack from Home 2020 Hackathon, and it's an app that helps COVID patient families stay up-to-date on the health of their loved ones through an interactive real-time feed. 

The Patient Progress app was designed with the assumption that the medical data will be collected from existing NHS APIs and displayed on the interactive feed. As we do not have access to such data, the Patient Progress REST API mimics patient records for demonstration purposes. 

The Patient Progress REST API has no HTML interface and returns raw JSON data. That is kind of boring, but you can check out the API-powered feed in action down below 👇.

## Use
The API has two publicly available end points:
- **GET** Patients End Point `api/patients`
- **GET** Patient Detail `api/patients/<nhs_number>`

## Technologies
- Python 3
- Django and Django REST
- PostgreSQL
- Heroku (Free Tier)

## Preview
<img src="images/preview.gif" height="100%" alt="Patient Progress demo preview"/>

## Database Schema
<img src="images/db-schema.png" alt="Database schema" />
