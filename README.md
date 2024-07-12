# SpyneAIBackendAssignment
Solution to backend developer assignment for spyne ai

Do the following to run the backend server:
1. Run createDB.py: This will create the sqlite database testData.db with Users and Discussion table
2. Run datastructure.py: This will create python exportable classes for user and discussion
3. Run executeDB.py: This will create python exportable classes for executing database statements
4. Run restAPI.py: This is the file that contains API
5. on a python terminal, run: 'fastapi run restAPI.py', this will run the fastAPI server which will respond to the incoming requests
6. Import the postman_collection available in postman to test the APIs
7. To view the documentation for the APIs: visit 'http://localhost:8000/docs#'
