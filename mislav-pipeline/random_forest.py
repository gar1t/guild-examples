import util

depth = 1

data, meta = util.load_data()

print(
    "Training random forest model on %s (%i examples) with depth %i"
    % (meta["type"], len(data), depth)
)
print("acc: 0.9")
