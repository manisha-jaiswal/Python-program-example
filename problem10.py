# Task
# Given a string with a lot of indian phone numbers starting from +91
import re
str = "Hello mere dosto mere pas kuch no. " \
      "hain +919425635125, +912534587965 aur batau kya +913265254789, +914587496584 aur +914257865 last wala nahi ana chahiye"

patt = re.compile(r'\b91\d{10}')
matches = patt.finditer(str)
for match in matches:
    print(match)