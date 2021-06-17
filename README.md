# RESTful_API
Flask API project for work with the database
  
## Project description  
### Structure of project 

```` 
app
    ├──  models                 - this folder contains all database models.
    │   ├── base.py             - this file contains class Model which handles all data-management operations. Actor and Movie classes will be inherited from it.
    │   ├── actor.py            - Actor entity model.
    │   ├── movie.py            - Movie entity model.
    |   └── relations.py        - association table for Actor and Movie entities. 
    │
    │
    ├── controllers             - this folder contains all commands operations handlers.
    │   ├── actor.py            - handlers for operations related to the Actor entity.
    │   ├── movie.py            - handlers for operations related to the Movie entity.
    │   └── parse_request.py    - this file contains a function which parses request data and converts it to a convenient format.
    │   
    │   
    ├── settings                - here you can store different constant values, connection parameters, etc.
    │   └── constants.py        - multiple constants storage for their convenient usage.
    │ 
    │ 
    ├── core                    - folder, which contains core application components.
    │   ├── __init__.py         - initializing our app and DB.
    │   └── routes.py           - application routes (predefined commands).
    │ 
    │ 
    ├── run.py                  - application run file.
    |
    ├── Dockerfile				      - commands used for Dockerization
    |
    └── requirements.txt		    - list of libraries used for Dockerization

````   
### In work  
API works with postgreSQL database. Database theme: movies and actors
  
Flask commands description:
  | route| method    | description| 
--- | --- | ---
  |  /api/actors           | GET       | get the list of all actors                                         | 
  |  /api/actor            | GET       | get actor by id                                                    | 
  |  /api/actor            | POST      | add new actor. Body can include: name, gender, date_of_birth       |
  |  /api/actor            | PUT       | update actor. Body can include: name, gender, date_of_birth        |
  |  /api/actor            | DELETE    | remove actor by id                                                 |
  |  /api/actor-relations  | PUT       | add relations. Body can include: id (actor), relation_id (movie)   |
  |  /api/actor-relations  | DELETE    | delete relations by id                                             |
  |  /api/movies           | GET       | list of all movies                                                 |
  |  /api/movie            | GET       | get movie by id                                                    |
  |  /api/movie            | POST      | add new movie. Body can include: name, year, genre                 |
  |  /api/movie            | PUT       | update movie. Body can include: name, year, genre                  |
  |  /api/movie            | DELETE    | remove movie by id                                                 |
  |  /api/movie-relations  | PUT       | add relations. Body can include: id (movie), relation_id (actor)   |
  |  /api/movie-relations  | DELETE    | delete relations by id                                             |
   
If someting is wrong with request, response status code will be 400 and it will call messege about error. If all is correct, response status code will be 200.

Example:  
![image](https://user-images.githubusercontent.com/77074682/122412729-7c246e00-cf8e-11eb-9fcb-7627016c5fdf.png '/api/actors GET')
  
![image](https://user-images.githubusercontent.com/77074682/122412939-ac6c0c80-cf8e-11eb-8017-80a27a805ab7.png '/api/actor POST')
  
![image](https://user-images.githubusercontent.com/77074682/122413309-f05f1180-cf8e-11eb-9cfa-631e12d02f4a.png '/api/actor PUT')
  
![image](https://user-images.githubusercontent.com/77074682/122413432-08cf2c00-cf8f-11eb-8862-683c96161b16.png '/api/actor DELETE')
  
![image](https://user-images.githubusercontent.com/77074682/122413498-15ec1b00-cf8f-11eb-939b-2c3fc95d16e1.png '/api/actors GET')
