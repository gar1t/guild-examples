import json
import os


def load_data(dir="."):
    meta = _load_meta(dir)
    _save_run_attrs(meta, dir)
    data = _load_data(dir)
    return data, meta


def _load_meta(dir):
    return json.load(open(os.path.join(dir, "meta.json")))


def _save_run_attrs(meta, dir):
    attrs_dir = _ensure_attrs_dir(dir)
    for meta_name, val in meta.items():
        attr_name = "data_%s" % meta_name
        with open(os.path.join(attrs_dir, attr_name), "w") as f:
            json.dump(val, f)


def _ensure_attrs_dir(dir):
    attrs_dir = os.path.join(dir, ".guild", "attrs")
    if not os.path.exists(attrs_dir):
        attrs_dir = os.path.join(dir, "attrs")
        os.makesirs(attrs_dir)
    return attrs_dir


def _load_data(dir):
    return open(os.path.join(dir, "data.csv")).readlines()
