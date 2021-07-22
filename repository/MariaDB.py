from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MariaDB:
    def __init__(self):
        engine = create_engine("mysql+pymysql://root@localhost/api?charset=utf8mb4")
        Session = sessionmaker(bind=engine)
        self.session = Session()




