# Develop a Secure Back-End Architecture Using Django ORM

**OpenClassrooms - Python Developer Path:** Project 12

**Student:** Abdoul Baki Seydou

**Date:** 10/06/2024 

## Table of Contents
1. [Summary](#summary)
2. [CRM Workflow](#crm-workflow)
3. [Features](#features)
4. [API Endpoints](#api-endpoints)
5. [Technologies Used](#technologies-used)
6. [Project Tasks](#project-tasks)
7. [Local Development](#local-development)
   - [Prerequisites](#prerequisites)
   - [Setup on macOS/Linux](#setup-on-macoslinux)
   - [Setup on Windows](#setup-on-windows)
   - [Running the Application](#running-the-application)
   - [Linting and Testing](#linting-and-testing)
   - [Database Management](#database-management)
   - [Admin Panel](#admin-panel)

## Summary
This project consists of developing for **Epic Events**, an event management firm, 
a secure customer relationship management(CRM) software for better clients and events management, 
in replacement of their outdated software which had been hacked.

## CRM Workflow
The CRM facilitates collaboration across three user groups:
1. **Sales Team**: Engages potential clients, finalizes contracts and create events.
2. **Management Team**: Assigns support member to events and oversees operations.
3. **Support Team**: Manages event until its completion.

## Features
- **Authentication & Authorization**: Role-based secure access.
- **API Endpoints**: Secure, and support CRUD (create, read, update, and delete).
- **Logging**: Logging enabled to ensure effective monitoring and troubleshooting.

## API Endpoints 

| Endpoint            | Description           | Method | Permissions                                |
|---------------------|-----------------------|--------|--------------------------------------------|
| crm/login/	         | Log in to the api     | POST   | Management, Sales, Support                 |
  | crm/clients/        | Create a Client       | POST   | Management, Sales                          |
  | crm/clients/        | Get all Clients       | GET    | Management, Sales, Support                 |             
  | crm/clients/{id}/   | Get a single Client   | GET    | Management, Sales, Support                 |                
  | crm/clients/{id}/   | Update a Client       | PUT    | Management, Sales_contact                  |            
  | crm/clients/{id}/   | Delete a Client       | DELETE | Management, Sales_contact                  |  
  | crm/contracts/      | Create a Contract     | POST   | Management, Sales                          |          
  | crm/contracts/      | Get all Contracts     | GET    | Management, Sales, Support                 |        
  | crm/contracts/{id}/ | Get a single Contract | GET    | Management, Sales, Support                 |         
  | crm/contracts/{id}/ | Update a Contract     | PUT    | Management, Sales_contact                  |                
  | crm/contracts/{id}/ | Delete a Contract     | DELETE | Management, Sales_contact                  |    
  | crm/events/         | Create an Event       | POST   | Management, Sales                          |      
  | crm/events/         | Get all Events        | GET    | Management, Sales, Support                 |     
  | crm/events/{id}/    | Get a single Event    | GET    | Management, Sales, Support                 |
  | crm/events/{id}/    | Update an Event       | PUT    | Management, Sales_contact, Support_contact |          
  | crm/events/{id}/    | Delete an Event       | Delete | Management, Sales_contact, Support_contact |

## Technologies Used
- **Programming Language:** Python  
- **Framework:** Django REST framework 
- **Database:** PostgreSQL

## Project Tasks
1. Design Django models covering important business areas.
2. Design an Entity Relationship Diagram.
3. Create Serializers for data validation and transformation.
4. Create Views to handle API logic.
5. Define URL routes for the API.
6. Create Permissions and apply to the Views to ensure secure access.

## Local Development

### Prerequisites
- PostgreSQL installed.
- Python 3.6 or higher.

### Setup on macOS/Linux

1. **Clone the Repository**
   ```bash
   cd /path/to/put/project/in
   git clone https://github.com/Afudu/P12_OpenClassroom.git

2. **Move to the folder**
   ```bash
   cd P12_OpenClassroom

3. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
4. **Activate Environment**
   ```bash
   source venv/bin/activate 

5. **Securely upgrade pip**
   ```bash
   python -m pip install --upgrade pip 

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
7. **To deactivate Environment**
   ```bash
   deactivate

### Setup on Windows

1. Follow the steps above.

2. To activate the environment:
   ```bash
   .\venv\Scripts\Activate

### Running the application

1. **Start the server**
   ```bash
   cd epic_events; python manage.py runserver
   
2. **Access in the browser**
   To verify the site is running, navigate to:
   ```bash
   http://localhost:8000/crm/

### Database Management

1. **Open PostgreSQL shell:**
   ```bash
   sudo -u postgres psql

2. **Create the database:**
   ```sql
   CREATE DATABASE epic_events_db;
  
3. **Set the permissions:**
   ```sql
   CREATE USER epic_event_user WITH PASSWORD '123456';
   GRANT ALL PRIVILEGES ON DATABASE epic_events_db TO epic_event_user;
  
4. **Apply Database Migrations:**
   ```bash
   Apply Database Migrations; python manage.py migrate crm
  
5. **Create a Management user:**
   ```bash
   python manage.py create_management_user

### Admin Panel
1. Navigate to http://localhost:8000/admin
2. Use the management user created above to log in.

### Linting and Testing

- **Run Linting**
  ```bash
  flake8

- **Tests**

  All other endpoints require an access token to work, and can be tested using [Postman](https://www.postman.com/) or any other tool like cURL or Django REST framework’s localhost server.
  
- The tests performed and their results can be viewed from this [link](https://documenter.getpostman.com/view/25994788/2sAYBUDsAN).