# orders_management

-Creación del entorno virtual
virtualenv venv -p 3 # or virtualenv venv --python=/usr/bin/python3
-Clonar el repositorio
git clone git@github.com:rolandoivan23/orders_management.git
cd orders_management
-Instalar dependencias
pip install requirements.txt
-Crear base de datos
python manage.py migrate
-Popular base de datos
python manage.py loaddata catalogs/fixtures/catalogs_data.json

