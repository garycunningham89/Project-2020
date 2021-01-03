# Project 2020
 Machine Learning 
Random numerical app.
Linux
export FLASK_APP=rando.py
python3 -m flask run
Windows
set FLASK_APP=rando.py
python -m flask run
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image