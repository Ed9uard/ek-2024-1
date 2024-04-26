pipenv, version 2023.12.1
pipenv --rm 
pipenv sync --dev 

docker pull testich/contactbook 

or 

docker build . -t testich/contactbook

docker run -it testich/contactbook

docker run -it testich/contactbook /bin/bash 
    ls
    python bot.py    #to run



 others support command pipenv run pip freeze > requirements.txt