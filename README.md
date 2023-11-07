# AirBnB Clone Readme

## Description
This console program emulates basic functionality of the AirBnB website, allowing users to manage object instances via a console interpreter. The AirBnB clone project implements a backend console for managing various objects, including:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

Object data is stored using JSON serialization and an abstracted storage engine.

## Console Usage
To start the AirBnB clone console, run the following command in your terminal:

\`\`\`bash
./console.py
\`\`\`

The console supports the following commands:

- \`create <class>\`: Creates a new instance of the given class.
- \`show <class> <id>\`: Prints the object representation.
- \`all\` or \`all <class>\`: Prints all objects or objects of a specific class.
- \`destroy <class> <id>\`: Deletes an object.
- \`update <class> <id>\`: Updates the attributes of an object.

For more information on specific commands, you can type \`help\` or \`help <command>\` within the console.

Example usage:

\`\`\`bash
(hbnb) create BaseModel
01778a34-e02b-4dff-92a9-471f489d93db
(hbnb) show BaseModel 01778a34-e02b-4dff-92a9-471f489d93db
[BaseModel] (01778a34-e02b-4dff-92a9-471f489d93db) {'id': '01778a34-e02b-4dff-92a9-471f489d93db', 'created_at': datetime.datetime(2023, 2, 13, 14, 56, 12, 96959), 'updated_at': datetime.datetime(2023, 2, 13, 14, 56, 12, 96971)}
(hbnb) destroy BaseModel 01778a34-e02b-4dff-92a9-471f489d93db
(hbnb) all BaseModel
[]

## Testing
The console and classes are extensively tested using the \`unittest\` module. Tests for console functionality can be found in \`tests/test_console.py\`, and tests for each class are located in \`tests/test_<class>.py\`. To run all tests, navigate to the project root directory and execute the following command:

\`\`\`bash
python3 -m unittest discover tests
\`\`\`

This project prioritizes comprehensive testing of all its features to ensure reliability and correctness.
EOF
