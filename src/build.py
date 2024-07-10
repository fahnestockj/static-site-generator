import os
import shutil

def build_static_file(abs_file_path):
    src_path = abs_file_path
    abs_public_path = os.path.abspath("public")
    abs_static_path = os.path.abspath("static")
    relative_path_from_static = os.path.relpath(src_path, abs_static_path)
    dst_path = os.path.join(abs_public_path, relative_path_from_static)
    par_path = os.path.abspath(os.path.join(dst_path, os.pardir))
    
    os.makedirs(par_path,0o777, True)
    shutil.copy(src_path, dst_path)



def build_static_content():
    # clear out public dir
    shutil.rmtree("public")
    os.makedirs("public")
    walk_dir(os.path.abspath("static"), build_static_file)

def walk_dir(dir_abs_path: str, cb):
    for entry in os.listdir(dir_abs_path):
        entry_path = os.path.join(dir_abs_path, entry)
        if os.path.isdir(entry_path):
            walk_dir(entry_path, cb)
        else:
            cb(entry_path)

