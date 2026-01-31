from etl.extract import extract_catalog_orders, extract_web_orders, extract_products
from etl.transform import basic_exploration, clean_catalog, clean_pcode,clean_dates,create_dim_date,create_dim_catalog,create_dim_product
from etl.load import load_to_postgres
 
#catalog = extract_catalog_orders("data/Catalog_Orders.txt")
#web = extract_web_orders("data/Web_orders.txt")
# products = extract_products("data/Products.txt")
catalog = extract_catalog_orders("data/dfl_catalogo.txt")
web = extract_web_orders("data/dfl_web.txt")
products = extract_products("data/dfl_productos.txt")

print(catalog.head())
print(web.head())
print(products.head())


basic_exploration(catalog, "Catalog Orders")
basic_exploration(web, "Web Orders")
basic_exploration(products, "Products")

catalog = clean_catalog(catalog)
catalog = clean_pcode(catalog)
catalog = clean_dates(catalog)

web = clean_catalog(web)
web = clean_pcode(web)
web = clean_dates(web)

fact = web.merge(products, on="PCODE")

dim_date = create_dim_date(fact)
dim_catalog = create_dim_catalog(fact)
dim_product = create_dim_product(fact)

# load_to_postgres(dim_date, "dim_date")
# load_to_postgres(dim_catalog, "dim_catalog")
# load_to_postgres(dim_product, "dim_product")
# load_to_postgres(fact, "fact_orders")
