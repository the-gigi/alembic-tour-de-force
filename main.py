import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Bug


# db_name = 'alembic_tour_de_force.db'
# if os.path.exists(db_name):
#     os.remove(db_name)
# connection_string = 'sqlite:///' + db_name

db_url = 'aws-us-east-1-portal.17.dblayer.com:11453/compose'
password = os.environ['COMPOSE_POSTGRESS_PASSWORD']
connection_string = 'postgres://admin:{}@{}'.format(password, db_url)


engine = create_engine(connection_string)
Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Insert some bugs
bugs = (
    (10, 'no unit test'),
    (12, 'no unit test'),
    (13, 'insufficient coverage in unit test'),
    (14, 'no integration test'),
    (19, 'unit test broken'),
    (22, 'no intgeration test'),
    (24, 'insufficient coverage in integration test'),
    (25, 'no integration test'),
)

for bug_id, root_cause in bugs:
    bug = Bug(bug_tracker_url='http://bug-tracker.org/{}'.format(bug_id),
              root_cause=root_cause,
              who='Gigi')

    session.add(bug)

session.commit()

# get a query object
q = session.query

# Query all bugs

# for bug in q(Bug).all():
#     print(bug)

# Query some bugs by root cause
for bug in q(Bug).filter_by(root_cause='no integration test'):
    print(bug)
