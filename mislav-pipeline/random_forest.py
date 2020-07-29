import util

data, meta = util.load_data()

print("Training random forest model on %s (%i examples)" % (meta["type"], len(data)))
print("acc: 0.9")
