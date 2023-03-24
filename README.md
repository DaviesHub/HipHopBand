# Hiphop Band Web App

## Contents
1. Description
2. Features
3. Installation
4. Usage
5. Package Requirements
6. Running the Application with Docker
7. Running the Application on any device with Docker Playground
8. Contributions
9. Access Tokens
10. Acknowledgement

## Description
This is a Django web application for a hiphop band with user authentication enabled. Registered users are allowed to view band information like albums, tours, and available merch. Registered users are also allowed to purchase tickets for a tour, buy merch and play album tracks via a youtube link.

## Features
. User authentication: Only registered users can access band information, buy tour tickets, buy merchandise, and play album tracks.

. Band information: Registered users can view details about the band's albums, tours, and merchandise.

. Album tracks: Registered users can play album tracks through a YouTube link.

. Merchandise: Registered users can browse and purchase band merchandise and see their purchase history.

. Tours: Registerd users can see latest band tours, dates and location.

. Tour tickets: Registered users can purchase tickets for upcoming tours and see their purchase history.

## Installation
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages by running 'pip install -r requirements.txt' on the terminal.
4. Create a database by running python manage.py migrate.
5. Create a superuser by running python manage.py createsuperuser.
6. Run the server by running 'python manage.py runserver' on the terminal.

## Usage
1. Open the web browser and go to the URL where the server is running.

![user auth](login.PNG)

2. Click on the "Register" button to create an account.

3. Login using the registered username and password. Once any user logs in successfully, the user will have access to the group's albums, tours, merch and contact (unregistered users can also see the contacts). Users can purchase tour tickets and a ticket confirmation page will be displayed for the user.

4. Browse through the site to view the band's information, purchase tour tickets, buy merchandise, and play album tracks through a YouTube link.

![ticket purchase](ticket.PNG)

## Package Requirements
Package requirements for this app can be seen on the requirements.txt file. See step 3 in installation for more.

## Running the Application with Docker
1. Clone the repository to your local machine.

2. Install Docker if you haven't already done so. You can download Docker [here](https://www.docker.com/get-started).

3. Create a docker file in the root directory

4. Open a terminal or command prompt and navigate to the root directory of the project.

5. Build the Docker image by running the following command: 'docker build -t hiphop-band'.
This will create a Docker image named hiphop-band based on the Dockerfile in the project's root directory.

6. Run the Docker container by running the following command: 'docker run -p 8000:8000 hiphop-band'
This will start the Docker container and map the container's port 8000 to your host machine's port 8000, allowing you to access the Django app in your web browser.

7. Open your web browser and go to http://localhost:8000 to view the running Django app.

## Running the Application on any device with Docker Playground

## Contributions
Contributions to the project are welcome. Please submit a pull request with your changes.

## Access Tokens
This app does not require users to authenticate with an external service that requires access tokens and secret keys.

## Acknowledgement
- Index page pic by Omran Soliman on Pexels
- Album pic by dids on Pexels
- Tour pic by Lisa Fotios on Pexels
- Merch pic by Vitalinha on Pexels
- Reachout pic by Maria Tyutina on Pexels
- Tour photos by Pixabay on Pexels