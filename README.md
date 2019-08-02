# Deploying a Titanic Prediction Model on Heroku

This tutorial shows how to set up and deploy a prediction model on Heroku using Docker. The model is based on the famous “Titanic: Machine Learning from Disaster” from Kaggle, where the survival prediction of a passenger is estimated.


# Files you will find in this repo:



*   The train and test datasets in .csv format.
*   The create_db.py file  that will create a database with 2 tables to train ‘passengers’ and to make prediction ‘test_passengers’.
*   Pipeline of a prediction model under the folder ml_model.
*   The dockerfile that will build the container for the model.
*   The requirements.txt file that will load the necessary libraries and dependencies


# Prerequisites:



*   Python 3 installed
*   A free Heroku account
*   A postgres database on a server (if you haven’t, you can create it in the followings).
*   Postman installed


# Setting up:

In your command-line interface, run the following commands (Note that I am on Linux, your actual CLI could be different) to create a new folder, clone the repository, and install the environment:

$ touch <folder-name>

$ git clone <git-address>

$ pip install pipenv 

$ pipenv shell

Open your browser and log in to your heroku account.

Click on New button-> Create new app and name it <app-yourname>.

Open .envrc file and fill it with your database url and local port.

If you don’t have yet a database, create one in your heroku app:

Open the menu /Ressources, type “Heroku-postgres” in the Adds-on bar, and validate it.

Open the menu /Settings , click on Reveal Config Vars button, and copy the url and paste it in the .envrc file (be cautious not to include any space around the = sign)

DATABASE_URL=<postgressdatabaseurl>

PORT=<4digit>

Fill the database with the datasets values by running in your terminal:

$ python create_db.py

Build the Docker container for the application.

$ sudo docker build .

Log in to your heroku container from your command line-interface (have your heroku password in mind :-) ), tag your container with <app-yourname>, push and release it with:

$ sudo heroku login

The previous command line should open a browser so that you can login to your Heroku account. In my case, I should do the following:

$ sudo heroku login -i

$ sudo heroku container:login

Check container id and copy the container ID you have just created:

$ sudo docker images

Update tag to properly name your container:

“docker tag <image>registry.heroku.com/<app>/<process-type>”

$ sudo docker tag <imageID> registry.heroku.com/<app-yourname>/web:latest

Check that the container tag has been correctly implemented:

$ sudo docker images

Push the container on heroku repository: “docker push registry.heroku.com/<app>/<process-type>”

$ sudo docker push registry.heroku.com/<app-yourname>/web:latest

And...release application

$ sudo heroku container:release web -a <app-yourname>

Open your browser and copy-paste the following URL, updated previously with your app name:

https://<app-yourname>.herokuapp.com/train

The page should display the message:“Training completed”, meaning that the application has been correctly deployed.

Then you are done with the deployment! Let’s make your survival predictions:


# Make prediction

The application contains several GET and POST routes to check the model, show the dataset and make predictions.

From your working folder with your command line interface, install the required library and set the environment variables. Then run the app.

$ pip install -U -r requirements.txt

$ direnv allow

$ python app.py

Open Postman, create a new GET request, name it <Titanic_app_yourname> and create a folder where the requests will be saved, name it <prediction_app_yourname>.

Copy-Paste the Heroku URL in your Postman “https://<app-yourname>.herokuapp.com/” and try the following routes, and try the following routes:



*   GET ……./train

This route will display the message:“Training completed”, meaning that the model has been correctly loaded, trained and saved.



*   GET ……./data

This route will display the dataset train (or table “passengers”) as a dictionary.



*   GET ….../test

This route will display the dataset test (or table “test_passengers”) as a dictionary.



*   POST ….../predict_db

This route will make prediction on the whole test dataset (or table “test_passengers”). It will also return a new table with the data and predictions.



*   POST ….../predict

To use this route, the user could enter the data of one or several passengers and get their survival prediction. (Don’t forget to use Raw - JSON format when your make your request).

