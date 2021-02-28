# ShopGrok Python Exercises

Python exercises for ShopGrok.

## Regex Questions

Further explanation added in comments of actual files.

### Question 2.1

`product_count_int = int(re.findall("\d+", product_count_text)[0])`

### Question 2.2

`special_sequence = re.findall("\/([^/]*?)\-", url)[0]`

### Question 2.3

`product_storage_parsed = re.findall("products_storage ?= ?(?=\[)(.*?)(?<=\])", product_storage_string_raw)[1]`
