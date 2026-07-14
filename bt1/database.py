from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


DATABASE_URL = "mysql+pymysql://root:04122007@localhost:3306/b1ss17"

engine = create_engine(DATABASE_URL)

LocalSesison = sessionmaker(autoflush=False,autocommit=False,bind = engine)
Base = declarative_base()