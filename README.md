# Patient Progress REST API

## General Information

This Python-powered REST API fuels the backend of the Patient Progress app, born from the CFG Hack from Home 2020 Hackathon. It keeps families of COVID patients informed with an interactive real-time feed.

Designed to sync with NHS APIs for medical data, our demo API simulates patient records. While it lacks an HTML interface, it delivers raw JSON data. But hey, check out the lively API-powered feed below! 👇

## Usage
The API has two publicly available end points:
- **GET** Patients End Point `api/patients`
- **GET** Patient Detail `api/patients/<nhs_number>`

## Technologies
- Python 3
- Django and Django REST
- PostgreSQL
- Heroku (Free Tier)

## Preview
<img src="images/preview.gif" width="40%" alt="Patient Progress demo preview"/>

## Database Schema
<img src="images/db-schema.png" alt="Database schema" width="80%"/>
