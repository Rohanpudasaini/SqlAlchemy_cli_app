# What is EducationHub?

Its is a simple CLI application which is the updated form of [EducationHub_postgres](https://github.com/Rohanpudasaini/EducationHub_postgres) , I have used postgres to store the user's (student in this case) data, and added SQLAlchemy as an ORM to handel database releated works. To run this please makesure you have postgres installed.
You can follow a guide online.

**Make sure you have created a `.env` file which will consist of your databse's information as below.**

1. ## .env

   ```ini
        host=host_location(generally localhost)
        database=postgres_databasename
        user=postgres_username
        password=your_password
    ```

Dont forget to change the values in the `.env` with your database's informations.

Now to run the app simply run
`pip install sqlalchemy`
and finally, do
`python3 Educationhub.py`
