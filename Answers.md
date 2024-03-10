Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.
  Based on the given image which appears to be an entity relationship diagram (ERD), the relationship between product and product category is one-to-many. This means that a single product category can have many products, but a single product can only belong to one product category.

  Here’s a breakdown of the  relationship between the two entities:
  
  Product Category
  has attributes like:
  name
  description
  created at (timestamp)
  deleted at (timestamp)
  Product
  has attributes like:
  id
  name
  description
  SKU (Stock Keeping Unit)
  quantity
  category ID (foreign key referencing product category)
  created at (timestamp)
  modified at (timestamp)
  deleted at (timestamp)
  price
  discount ID (foreign key referencing discount table - not shown in this image)
  discount percent
  active (boolean)
  The  category ID in the product table is a foreign key that references the primary key (likely an id attribute) of the product category table. This creates the one-to-many relationship between the two tables.
  
  In simpler terms, a product category is like a shelf in a store, and the products are the items that are placed on that shelf. For example, the “Electronics” category might contain many different products, such as TVs, laptops, and smartphones. But a specific TV can only be on one shelf, like the “TVs” subcategory.

How could you ensure that each product in the "Product" table has a valid category assigned to it?
    Here are a few ways to ensure that each product in the "Product" table has a valid category assigned to it, based on the information in the ERD:

    1. Referential Integrity Constraints:
    
    Most database management systems allow you to enforce referential integrity constraints. This means the database will check to ensure that the value in the "category ID" field of the "Product" table actually exists as a primary key value in the "Product Category" table. This prevents products from being assigned non-existent category IDs.
    
    2. Data Validation on Insert/Update:
    
    During the process of adding or updating a product, you can implement data validation logic. This logic can check if the provided "category ID" exists in the "Product Category" table before allowing the product to be saved. This validation can be done on the application layer (code) or through database triggers.
    
    3. Dropdown Menu with Valid Categories:
    
    If you have a user interface for adding or updating products, you can display a dropdown menu populated with valid categories from the "Product Category" table. This prevents users from manually entering invalid category IDs.
    
    4. Default Category:
    
    As a fallback option, you can define a default category (e.g., "Uncategorized") in the "Product Category" table. During product creation, if no valid category ID is provided, the product can be assigned this default category. This ensures no product remains completely without a category.
    
    5. Regular Data Quality Checks:
    
    Even with these measures in place, it's good practice to run regular data quality checks to identify and correct any inconsistencies in the data. You can write queries to identify products with invalid category IDs and take corrective actions.
    
    These methods, used in combination, can help ensure data integrity and maintain a consistent relationship between products and their assigned categories.
