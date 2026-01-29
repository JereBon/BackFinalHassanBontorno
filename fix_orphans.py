import sys
import os
sys.path.append(os.getcwd())

from sqlalchemy import text
from config.database import SessionLocal

def fix_orphans():
    db = SessionLocal()
    try:
        print("Checking for orphaned products...")
        
        # SQL to find orphans: products with category_id that is NOT in categories
        sql_find = """
        SELECT id_key, name, category_id 
        FROM products 
        WHERE category_id IS NOT NULL 
        AND category_id NOT IN (SELECT id_key FROM categories)
        """
        
        orphans = db.execute(text(sql_find)).fetchall()
        
        if not orphans:
            print("No orphaned products found. Data looks clean.")
            return

        print(f"Found {len(orphans)} orphaned products:")
        for o in orphans:
            print(f" - Product {o.id_key} ({o.name}) points to missing category {o.category_id}")

        # Fix them
        sql_fix = """
        UPDATE products 
        SET category_id = NULL 
        WHERE category_id IS NOT NULL 
        AND category_id NOT IN (SELECT id_key FROM categories)
        """
        
        result = db.execute(text(sql_fix))
        db.commit()
        
        print(f"Fixed {result.rowcount} orphaned products. They now have category_id = NULL.")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_orphans()
