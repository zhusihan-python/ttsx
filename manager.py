import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
from app.model import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

if __name__ == "__main__":
    manager.run()