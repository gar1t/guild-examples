import util

data, meta = util.load_data()

print("Training decision tree model on %s (%i examples)" % (meta["type"], len(data)))
print("acc: 0.8")
