import re

# File paths
data_file = "data/data.txt"
link_file = "golang/canonical.txt"

# Read data.txt and extract canonical URLs
with open(data_file, "r") as df:
    data_content = df.read()

# Regex to find all _@_CANONICAL_@_ URLs
canonical_urls = re.findall(r"_@_CANONICAL_@_:\s*(https?://[^\s]+)", data_content)

# Append canonical URLs to link.txt
with open(link_file, "a") as lf:
    for url in canonical_urls:
        lf.write(url + "\n")

print(f"Added {len(canonical_urls)} canonical URLs to {link_file}")