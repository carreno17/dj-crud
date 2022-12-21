build.sh


pip install -r requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell
from djangocrud.models import Categories
Categories.objects.create(name="Ninguna")
exit()
