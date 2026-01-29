import sys
import os
sys.path.append(os.getcwd())

from config.database import SessionLocal, init_db
from models.product import ProductModel
from models.category import CategoryModel
from schemas.product_schema import ProductSchema
from sqlalchemy import text

def reproduce():
    db = SessionLocal()
    try:
        # 1. Create a category
        cat = CategoryModel(name="Temp Category")
        db.add(cat)
        db.commit()
        db.refresh(cat)
        cat_id = cat.id_key
        print(f"Created category {cat_id}")

        # 2. Create a product with this category
        prod = ProductModel(name="Temp Product", price=10.0, stock=5, category_id=cat_id)
        db.add(prod)
        db.commit()
        db.refresh(prod)
        prod_id = prod.id_key
        print(f"Created product {prod_id}")

        # 3. Delete the category via SQL to bypass any SQLAlchemy cascade logic (simulating the state)
        # OR just delete using session if that's how user did it. 
        # User implies they used the UI, which calls API, which uses session.delete().
        # Let's see if session.delete() fails to clear category_id.
        
        db.delete(cat)
        db.commit()
        print(f"Deleted category {cat_id}")

        # 4. Fetch the product
        db.expire_all()
        fetched_prod = db.query(ProductModel).filter(ProductModel.id_key == prod_id).first()
        
        print(f"Fetched product: {fetched_prod.name}, Category ID: {fetched_prod.category_id}")
        
        # 5. Access relationship
        print(f"category relationship: {fetched_prod.category}")
        
        # 6. Validate with Pydantic
        print("Validating with Pydantic...")
        schema = ProductSchema.model_validate(fetched_prod)
        print("Validation successful!")
        print(schema)

    except Exception as e:
        print(f"CAUGHT EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        try:
            if 'prod' in locals() and prod.id_key:
                db.execute(text(f"DELETE FROM products WHERE id_key = {prod.id_key}"))
            if 'cat' in locals() and cat.id_key:
                db.execute(text(f"DELETE FROM categories WHERE id_key = {cat_id}"))
            db.commit()
        except:
            pass
        db.close()

if __name__ == "__main__":
    reproduce()
