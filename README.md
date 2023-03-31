# Library System Simulation 

Library system simulation using relational databases made for AGH University classes. t is written in Python and uses SQLAlchemy as the Object Relational Mapper (ORM) for database management. The Projects uses [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset) from kaggle.com

The system allows users to issue books, return them, and also has a login system for students and teachers.


## Author

- [Kacper Bojanowski](https://www.github.com/kcbojanowski)
- [Mateusz Potaśnik](https://www.github.com/PotasnikM)



## Features
- Issue books
- Return books
- Login system for students and teachers
- Monitor the flow of books in the admin panel


## Installation

1. Clone this repository:
```bash
 git clone https://github.com/kcbojanowski/Database_Library
 ```
2. Change directory to the project directory: 
```bash
cd library-system-simulation
```
3. Create a virtual environment and activate it:
- On Windows: 
```bash
python -m venv venv  
```
```bash
venv\Scripts\activate
```
- On macOS/Linux: 
```bash
python3 -m venv venv 
```
```bash
source venv/bin/activate
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```
5. Set up the database by running:
```bash
python csv_to_db.py
```
6. Run the application: 
```bash
python app.py
```

Once the application is running, open a web browser and navigate to 
http://localhost:5000 to access the application.


## Running Tests

To run tests, run the following command:

```bash
  python -m unittest tests/tests_multi_access.py
```
or: 
```bash
  python -m unittest tests/tests_wrong_input.py
 ```
 
 ## Licence
 This project is licensed under the MIT License. See the LICENSE file for more information.
