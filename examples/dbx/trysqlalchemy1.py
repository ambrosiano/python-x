from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("sqlite:///test.db")
connection = engine.connect()

cars = Table("Cars",MetaData(),autoload=True,autoload_with=engine)

