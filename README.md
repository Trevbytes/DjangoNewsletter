# A Simple Newsletter Signup Form

This signup form was created to demonstate my abilites in Django by building a simple form allowing users to register and unregister to a newsletter. An admin should and can be able to download a list of the registerd users from the Django admin page.

### GitHub

[My GitHub Repository](https://github.com/Trevbytes/DjangoNewsletter)

After navigating to my repo you can download the project to a .zip file or open it in the online IDE Gitpod.

For more infomation on how to clone or download the repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Local Deployment

**To run this project locally**

- To run the project locally the following must be installed:
  - An IDE, such as [VS Code](https://code.visualstudio.com/)
  - [PIP](https://pip.pypa.io/en/stable/installing/), python requirements installer.
  - [Python3](https://www.python.org/downloads/), chosen coding language of the app.


- After, download a .ZIP file of my repository ([Master Branch](https://github.com/Trevbytes/DjangoNewsletter)) and unzip this file.

- Open this folder in your IDE

- All requirements from requirements.txt must be installed. Use the following command:
        
        pip install -r requirements.txt (VS terminal code)
        -or-
        pip3 install -r requirements.txt (Gitpod)

- In your terminal, navigate to the folder 'djangonewsletter' using the `cd` command.

        cd djangonewsletter

- Create a Django super user.

        python3 manage.py createsuperuser

- You should then be able to launch your app using the following command in your terminal:

        python3 manage.py runserver

- If your SQLite3 database is not working, confirm that there are no migrations to take care of.

        python3 manage.py makemigrations
        python3 manage.py migrate

- Access the admin page from the 'Admin' link in the deployed project or add /admin to the URL. Login with your new super user account. 

- You can run the tests associated with this simple form by entering the follwing command in your terminal:

        python3 manage.py test

*NOTE:* The secret key is visible in the settings file and should be placed in an environment variable if this code is used in production.
