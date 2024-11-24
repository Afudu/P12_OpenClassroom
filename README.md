# OpenClassrooms - Python Developer Path

**Project 12:** Develop a Secure Back-End Architecture Using Django ORM

**Student:** Abdoul Baki Seydou

**Date:** 10/06/2024

## Abstract
This project consists of developing for Epic Events a secure customer relationship management software (CRM), 
which tracks all its clients and events, using Django ORM, in replacement of their outdated software.

The Django application needs to deliver a set of secure API endpoints using the Django REST 
framework & ORM (with a PostgreSQL database) to support CRUD (create, read, update, and delete) 
operations on the various CRM objects.

The application requires authentication and authorized access for all operations, with logging enabled 
for effective monitoring and troubleshooting.

Business Process:
The users are divided in three groups: Management, Sales and Support teams.
1. Sales team works to convince potential clients. 
2. Converted clients sign a contract to put on their event.
3. Once a client signs a contract, sales contact creates the event.
4. The Management team assigns a support team member to the new event.
5. The assigned member from the support team manages the event until its completion.

*Permissions:*

* Management:
  - Full access (CRUD for all models, and user management).
  - Access to the Django admin site.

* Sales:
 - Can access all clients, contracts, and events.
 - Can manage assigned clients, contracts, and events.

* Support:
 - Read-only for all clients, contracts, and events.
 - Can Edit assigned events.


### API Endpoints 

| Endpoint            | Description           | Method |
|---------------------|-----------------------|--------|
| crm/login/	         | Log in to the api     | POST   | 
  | crm/clients/        | Create a Client       | POST   |  
  | crm/clients/        | Get all Clients       | GET    |                   
  | crm/clients/{id}/   | Get a single Client   | GET    |                      
  | crm/clients/{id}/   | Update a Client       | PUT    |                   
  | crm/clients/{id}/   | Delete a Client       | DELETE |          
  | crm/contracts/      | Create a Contract     | POST   |                   
  | crm/contracts/      | Get all Contracts     | GET    |                   
  | crm/contracts/{id}/ | Get a single Contract | GET    |                   
  | crm/contracts/{id}/ | Update a Contract     | PUT    |                            
  | crm/contracts/{id}/ | Delete a Contract     | DELETE |                   
  | crm/events/         | Create an Event       | POST   |                   
  | crm/events/         | Get all Events        | GET    |                   
  | crm/events/{id}/    | Get a single Event    | GET    | 
  | crm/events/{id}/    | Update an Event       | PUT    |                   
  | crm/events/{id}/    | Delete an Event       | Delete |

## Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

## Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

   * Unix/macOS/Windows

       ```bash
       git clone https://github.com/Afudu/P12_OpenClassroom.git
       ```

**2 - Move to the folder**

   * Unix/macOS/Windows

       ```bash
       cd P12_OpenClassroom
       ```  

**3 - Create a virtual environment**

  * Unix/macOS

    ```bash
    python3 -m venv pythonenv
     ```
  * Windows

    ```bash
    py -m venv pythonenv
    ```
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS

    ```bash
    source pythonenv/bin/activate
    ```

  * Windows

    ```bash
    pythonenv\Scripts\activate
    ```

**5 - Securely upgrade pip**

   * Unix/macOS/Windows

      ```bash
     py -m pip install --upgrade pip
     ```

**6 - Install all dependencies**

  * Unix/macOS/Windows

    ```bash
    pip install -r requirements.txt
    ```
## Set up the database
The database used is a Postgres database.

**1 - Ensure PostgreSQL is installed on your system**
    You can download the latest version for your system from : https://www.postgresql.org/download/

**2 - Create the Database in PostgreSQL**

  - Open the ```PgAdmin4``` application: You should find a database named postgres, 
right-click it and then choose the ```Query Tool```.

    - Execute this command to create th database named ```epic_events_db```:

      ```bash
      CREATE DATABASE epic_events_db;
      ```

  - Set the permissions on the database by clearing the Query Tool and running the following commands:

      ```bash
      CREATE USER epic_event_user WITH PASSWORD '123456';
      GRANT ALL PRIVILEGES ON DATABASE epic_events_db TO epic_event_user;
      ```
    * Note: the password set for the database isn't secure, it is only for testing purpose..

## Running the application

**Move to the folder**

  * Unix/macOS/Windows

      ```bash
      cd epic_events
      ```
**Apply Database Migrations**

  * Unix/macOS/Windows

    ```bash
      python manage.py makemigrations
    ```
    then 
    
    ```bash
      python manage.py migrate
    ```

**Start the server**

  * Unix/macOS/Windows

    ```bash
    python manage.py runserver
    ```

## Testing the application
After the server has started, you can create users and test the API.

* Login :  http://localhost:8000/crm/login


All other endpoints require an access token to work, and can be tested using [Postman](https://www.postman.com/) 
or any other tool like cURL or Django REST framework’s localhost server.

All required API Endpoints have been tested, documented, 
and [published](https://documenter.getpostman.com/view/25994788/2sAYBUDsAN) on Postman.

# PEP 8 adherence

The folder ```flake_report``` in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command: 

  * Unix/macOS/Windows

      ```bash
        flake8
       ```

The file ```setup.cfg``` in the root of the repository contains the settings used to generate the report.
