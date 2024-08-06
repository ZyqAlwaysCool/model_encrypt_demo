import os
import shutil
from cryptography.fernet import Fernet
from config import *

def model_encryption(pth_file, encryp_file, license):
    with open(pth_file, 'rb') as fr:
        pth_bytes = fr.read()

    key = license
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(pth_bytes)

    with open(encryp_file, 'wb') as fw:
        fw.write(encrypted_data)

def find_files(root_dir, pattern='.onnx'):
    """
    递归查找指定目录下的所有指定pattern文件。
    
    参数:
    root_dir (str): 要搜索的根目录路径。
    
    返回:
    list: 找到的目标文件完整路径列表。
    """
    onnx_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(pattern):
                full_path = os.path.join(dirpath, filename)
                onnx_files.append(full_path)
    return onnx_files

def move_file_to_folder(src_file_path, dest_folder_path):
    """
    将文件移动到指定的文件夹中。

    参数:
    src_file_path (str): 源文件的完整路径。
    dest_folder_path (str): 目标文件夹的路径。
    """
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)
    
    # 构建目标文件的完整路径
    dest_file_path = os.path.join(dest_folder_path, os.path.basename(src_file_path))
    
    # 移动文件
    shutil.move(src_file_path, dest_file_path)

if __name__ == '__main__':
    encrypt_weights = None
    if len(MODEL_ENCRYPT_SETTINGS['encrypt_model_path']) > 0:
        weights_list = MODEL_ENCRYPT_SETTINGS['encrypt_model_path']
    else:
        weights_list = find_files('.', MODEL_ENCRYPT_SETTINGS['encrypt_model_pattern'])
    
    encrypt_weights = [w+'-en' for w in weights_list]
    if encrypt_weights is None:
        raise Exception('No encrypt model found!')
    
    encrypt_key = Fernet.generate_key()
    
    assert(len(weights_list) == len(encrypt_weights))
    for i in range(len(weights_list)):
        model_encryption(weights_list[i], encrypt_weights[i], encrypt_key)
        move_file_to_folder(encrypt_weights[i], MODEL_ENCRYPT_SETTINGS['encrypt_model_save_path'])
    
    with open(MODEL_ENCRYPT_SETTINGS['encrypt_key_path'], 'wb') as f:
        f.write(encrypt_key)
    