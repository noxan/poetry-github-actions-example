from dateutil.parser import parse

now = parse("Sat Oct 11 17:13:46 UTC 2003")
print(f"The date is {now.date()}.")
