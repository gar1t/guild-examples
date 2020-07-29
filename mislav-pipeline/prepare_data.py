import json

type = "cats"

print("Preparing %s data" % type)

# Save metadata
with open("meta.json", "w") as f:
    json.dump({"type": type}, f)

# Save examples
with open("data.csv", "w") as f:
    if type == "cats":
        f.write("cat-1\n")
        f.write("cat-2\n")
    elif type == "dogs":
        f.write("dog-1\n")
        f.write("dog-2\n")
        f.write("dog-1\n")
    else:
        assert False, type
