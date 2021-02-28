import re

generic_urls = ["https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img", "https://www.genericdomain.com/abc/31287bdwakj-jkl.img", "https://www.genericdomain.com/19unioawd02-jkl.img"]

for url in generic_urls:
    # capture all characters between / and -
    # exclude any / to ensure it's the last /
    special_sequence = re.findall("\/([^/]*?)\-", url)[0]
    print(special_sequence)
