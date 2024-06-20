from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Подключение к базе данных/создание базы данных
# SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
### postgres: logi, 1234: password ###
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:aydos2005@127.0.0.1/moxi_db'
# Создание движка бд
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Переменная для создания сессий
SessionLocal = sessionmaker(bind=engine)
# Создание шаблона для базы классов бд
Base = declarative_base()

# Создание сессий


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
