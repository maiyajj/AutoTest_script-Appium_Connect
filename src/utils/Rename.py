import os.path

device_name = "GNAPP"
root_path = "../testcase/%s" % device_name
for parent, dirnames, filenames in os.walk(root_path):
    for filename in filenames:
        if device_name in filename:
            print(filename)
            old = os.path.join(parent, filename)
            new = os.path.join(parent, filename.replace(device_name, "GN_APP"))
            os.renames(old, new)
for parent, dirnames, filenames in os.walk(root_path):
    for dirname in dirnames:
        if device_name in dirname:
            print(dirname)
            old = os.path.join(parent, dirname)
            new = os.path.join(parent, dirname.replace(device_name, "GN_APP"))
            os.renames(old, new)
