# orders_management

-Creación del entorno virtual
virtualenv venv -p 3 # or virtualenv venv --python=/usr/bin/python3
-Activar entorno virtual
	source ven/bin/activate
-Clonar el repositorio
git clone git@github.com:rolandoivan23/orders_management.git
cd orders_management
-Instalar dependencias
pip install requirements.txt
-Crear base de datos
python manage.py migrate
-Popular base de datos
El orden de las aplicaciones es importante para la integridad de los datos, en otro orden puede fallar el loaddata
python manage.py loaddata catalogs customers vendors articles

