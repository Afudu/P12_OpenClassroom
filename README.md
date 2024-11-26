# OpenClassrooms - Python Developer Path

**Project 12:** Develop a Secure Back-End Architecture Using Django ORM

**Student:** Abdoul Baki Seydou

**Date:** 10/06/2024

## Abstract
This project consists of developing for Epic Events, an event management firm, 
a secure customer relationship management software (CRM), which tracks all its clients and events, 
in replacement of their outdated software which had been hacked.

The application is built with the Django REST framework & ORM (with a PostgreSQL database), 
and delivers a set of secure API endpoints using the to support CRUD (create, read, update, and delete) 
operations on the various CRM objects.

In adhering to the security requirements, authentication and authorized access are required for all operations, 
and logging is enabled for effective monitoring and troubleshooting.

Main Business Process:
The users are divided in three teams: Management, Sales and Support.
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
 - Can create new clients, contracts, and events.
 - Can manage only assigned clients, their contracts and events.

* Support:
 - Read-only for all clients, contracts, and events.
 - Can manage only assigned events.


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

   * Windows

      ```bash
     py -m pip install --upgrade pip
     ```
   * Unix/macOS/

      ```bash
     python -m pip install --upgrade pip
     ```


**6 - Install all dependencies**

  * Unix/macOS/Windows

    ```bash
    pip install -r requirements.txt
    ```
**7 - Set up the Postgres database**
The database used is a Postgres database.
Ensure PostgreSQL is installed on your system.
You can download the latest version for your system from : https://www.postgresql.org/download/

  - Open your PostgreSQL shell.
     * Windows : Open ````SQL Shell```` separately from the installation command line with the activated environment,
      and connect to the initial database set up ```postgres``` using the password set during the installation.
     * Unix/macOS: Access psql from the same terminal with the activated environment:  
        ````bash
       sudo -u postgres psql
       ````
  - In the PostgreSQL shell, execute this command to create the database named ```epic_events_db```:

      ```bash
      CREATE DATABASE epic_events_db;
      ```

  - Set the permissions on the database by running the following commands:

      ```bash
      CREATE USER epic_event_user WITH PASSWORD '123456';
      GRANT ALL PRIVILEGES ON DATABASE epic_events_db TO epic_event_user;
      ```
    * Note: the password set for the database isn't secure, it is only for testing purpose.

  - Return to the installation command line with the activated environment.
     * Windows : switch to the installation command line.
     * Unix/macOS: type ```exit```.  

**8 - Move to the project folder**

  * Unix/macOS/Windows

      ```bash
      cd epic_events
      ```
**9 - Apply Database Migrations**

  * Unix/macOS/Windows

    ```bash
      python manage.py makemigrations crm
    ```
    then 
    
    ```bash
      python manage.py migrate crm
    ```

**10 - Start the server**

  * Unix/macOS/Windows

    ```bash
    python manage.py runserver
    ```

## Testing the application
After the server has started, to access the root view of the API, navigate to:

Api Root: http://127.0.0.1:8000/crm/

For testing purpose, the users endpoint is accessible without authentication, and allows to create users.
Create a user with management role from:
* Users: http://127.0.0.1:8000/crm/users/

The Management user created will be able to log in with email and password to the Django admin site, 
with full access to all models:
* Django Admin: http://localhost:8000/admin/

The clients, contracts and events endpoints require an access token to work. 
An access token can be obtained from the login endpoint, with a valid authentication:
* Login :  http://localhost:8000/crm/login/

All required API Endpoints have been tested using [Postman](https://www.postman.com/).
The tests and their results can be viewed from this [link](https://documenter.getpostman.com/view/25994788/2sAYBUDsAN).

# PEP 8 adherence

The folder ```flake_report``` in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command: 

  * Unix/macOS/Windows

      ```bash
        flake8
       ```

The file ```setup.cfg``` in the root of the repository contains the settings used to generate the report.
