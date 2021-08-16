from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from .math_serv import create_app
from .math_serv import celery

app = create_app()
app.app_context().push()
