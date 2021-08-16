import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from math_serv import create_app, db, models

app = create_app()
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run(host, port):
    app.run(host=host, port=port)

if __name__ == '__main__':
    manager.run()
