# AirBnB Clone Project README

## Description
This repository contains the AirBnB clone project, an educational project to replicate the basic functionalities of AirBnB. 
The project is part of the ALX SE curriculum, focusing on object-oriented programming, file storage, and a simple command-line interface.

## Features
- A command-line console that allows data management (create, update, destroy, etc.) of various classes.
- Storage of objects in a JSON file.
- Classes include BaseModel, User, State, City, Amenity, Place, and Review.

## Installation
Clone this repository to your local machine:
git clone https://github.com/mansouriyassine/AirBnB_clone.git

## Usage
To launch the console application, navigate to the project directory and run:
./console.py

## Console Commands
- create: Creates a new instance of a class.
- show: Shows an instance of a class based on its ID.
- destroy: Deletes an instance based on the class name and ID.
- all: Shows all instances of a class or all classes if no class name is provided.
- update: Updates an instance based on the class name and ID by adding or updating an attribute.
- quit or EOF: Exits the console.

## Examples
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) all
(hbnb) update BaseModel 1234-1234-1234 email "test@example.com"
(hbnb) quit

## Testing
Unit tests for the project are defined in the tests/ directory. To run the entire test suite, execute:
python3 -m unittest discover tests

# Files and Directories
- models/: Contains classes used for this project.
- tests/: Contains all unit tests.
- console.py: Entry point for the command-line console.
- models/engine/: Storage engine, including file storage.

# Authors
Yassine Mansouri - https://github.com/mansouriyassine/
Chidubem Uchendu - https://github.com/Dubemxe
