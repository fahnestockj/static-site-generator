import os
import shutil

def build_static_file(rel_file_path):
    src_path = os.path.abspath(rel_file_path)
    abs_public_path = os.path.abspath("public")
    abs_static_path = os.path.abspath("static")
    relative_path_from_static = os.path.relpath(src_path, abs_static_path)
    dst_path = os.path.join(abs_public_path, relative_path_from_static)
    par_path = os.path.join(dst_path, os.pardir)
    
    
    os.makedirs(par_path, True)
    shutil.copy(src_path, dst_path)


def build_static_content():
    # clear out public dir
    shutil.rmtree("public")
    walk_dir("static", build_static_file)

def walk_dir(dir_relative_path: str, cb):
    for entry in os.listdir(dir_relative_path):
        if os.path.isdir(entry):
            walk_dir(entry, cb)
        else:
            cb(entry)

