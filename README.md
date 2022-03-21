# test_app

Python version- 3.8.10
To install python:
sudo apt install python3.8

The required packages are listed in the requirements.txt file<br>
install the packages:
pip install -r requirements.txt

to run the application:
python manage.py runserver

to run the tests:
python manage.py test data

The admin panel can be shown at-
http://127.0.0.1:8000/admin/

API fields for parent:
 ['firstName', 'lastName', 'street', 'city', 'state', 'zip']

API fields for child:
['firstName', 'lastName']

the api urls:

list of parent usernames:
http://127.0.0.1:8000/parent_username_list/

creating parent data
http://127.0.0.1:8000/parent_data_create/parentUsername
  
updating parent data
http://127.0.0.1:8000/parent_data_update/parentUsername

deleting parent data
http://127.0.0.1:8000/parent_data_delete/parentUsername

  
  
list of child usernames:
http://127.0.0.1:8000/child_username_list/
  
creating child data
http://127.0.0.1:8000/child_data_create/childUsername>
  
updating child data
http://127.0.0.1:8000/child_data_update/childUsername

deleting child data
http://127.0.0.1:8000/child_data_delete/childUsername
