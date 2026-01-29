from sqlalchemy import text
from config.database import engine

def drop_reviews():
    with engine.connect() as conn:
        print("Dropping reviews table...")
        conn.execute(text("DROP TABLE IF EXISTS reviews CASCADE"))
        conn.execute(text("COMMIT"))
        print("Table reviews dropped successfully.")

if __name__ == "__main__":
    drop_reviews()
