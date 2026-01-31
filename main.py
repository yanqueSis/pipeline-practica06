from etl.extract import extract_catalog_orders, extract_web_orders, extract_products

catalog = extract_catalog_orders("data/Catalog_Orders.txt")
web = extract_web_orders("data/Web_orders.txt")
products = extract_products("data/Products.txt")

print(catalog.head())
print(web.head())
print(products.head())


# from etl.transform import basic_exploration

# basic_exploration(catalog, "Catalog Orders")
# basic_exploration(web, "Web Orders")
# basic_exploration(products, "Products")


# catalog = clean_catalog(catalog)
# catalog = clean_pcode(catalog)
# catalog = clean_dates(catalog)

# web = clean_catalog(web)
# web = clean_pcode(web)
# web = clean_dates(web)
