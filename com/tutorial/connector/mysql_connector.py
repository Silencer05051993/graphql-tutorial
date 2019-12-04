from sqlalchemy import create_engine


class MySQLConnector:
    @staticmethod
    def connection():
        engine = create_engine('mysql+pymysql://root:@localhost:3306/graphql_tutorial?charset=utf8', echo=False,
                               pool_pre_ping=True,
                               pool_size=10,
                               pool_recycle=3600)
        return engine.connect()


if __name__ == '__main__':
    MySQLConnector.connection()
