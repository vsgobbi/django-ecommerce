### @Vitor Sgobbi
"GPL license"
### Used libs and frameworks 
* django pillow Python3.7 pip3 

# First steps:
## Create virtual env for python3.7
> virtualenv -p python3.7 venv
## Activate to start development
> source /venv/bin/activate
## Check python correct version, must be greater than python3
> python --version # Python 3.7
> pip --version
## Then install requirements
> pip install -r requirements.txt
## Run django migration
> cd ecommerce/
> python manage.py migrate
## Create django administrator 
> python manage.py createsuperuser
## Run django environment
> python manage.py runserver


