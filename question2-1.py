import re

product_count_text = "381 Products found"
# variable lenght of product, not fixed number of digits
# only take the first result
product_count_int = int(re.findall("\d+", product_count_text)[0])
print(product_count_int)