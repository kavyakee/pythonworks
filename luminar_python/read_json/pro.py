from json import load
path="C:\\Users\\Admin\\Desktop\\luminar_python\\read_json\\data.json"
with open(path) as f:                                # with - we use with instead of close(),since we open the function we need to close here. so we use with. as f: - is used instead of f=open("path").
    records=load(f)                                  # load is the function we imported here,so load(f) is assigned to records.
print(records)
fw_names=[f.get("name") for f in records]
print(fw_names)
top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)
# length of records
print(len(records))

py_fw=[r.get("name") for r in records if r.get("language")=="python"]
py_fw=[r.get("name") for r in records if r.get("language")=="python"]