# Project 2020
Machine Learning 
Random numerical app.
Linux
export FLASK_APP=webservice.py
python3 -m flask run
Windows
set FLASK_APP=webservice.py
python -m flask run
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image

REFERENCES:

Class Content and Tutorials:

Martin Thoma (2014) Configuration files in Python. Access online at: https://martin-thoma.com/configuration-files-in-python/
James Marshall (2012) HTTP Made Really Easy A Practical Guide to Writing Clients and Servers. Access online at: https://www.jmarshall.com/easy/http/
FLASK (2020) Tutorials. Access online at: https://flask.palletsprojects.com/en/1.1.x/
Tutorialspoint (2020) FLASK Tutorials. Access online at: tutorialspoint.com/flask/index.htm
w3schools (2020) HTML Tutorials. Access online at: https://www.w3schools.com/html/default.asp

CHALLENGES:

Time constraints with course content in line with work commitments and pandemic restrictions.
Need to practice and use the course content in more examples for future learning.
Did not get the project finished to the standard I would have liked and should have invested more time on reflection.
Need to refresh on various elements in python and machine learning to improve standards.

FILES:

Requirements in requirements.txt
Server in webservice.py
DOCKERFILE
Project File as Project 2020.ipynb
Webpages in staticpages folder
keral model in kmodel.py and keralmodel.pkl
sklearn model in skmodel.py, model.pkl and model_columns.pkl