# import os
# import time
# from cryptography.fernet import Fernet

# def model_decryption(encrypt_file, decrypt_file, key):
#     '''
#     模型文件解密
    
#     :params encrypt_file: 加密文件路径
#     :params decrypt_file: 解密文件路径
#     :paramse key: 密钥
#     '''
#     with open(encrypt_file, 'rb') as fr:
#         encrypted_data = fr.read()
    
#     decrypted_data = Fernet(key).decrypt(encrypted_data)
    
#     with open(decrypt_file, 'wb') as f:
#         f.write(decrypted_data)

# def check_timestamp(start_timestamp, valid_days=30):
#     '''
#     检查时间戳是否过期
    
#     :params start_timestamp: 开始时间戳
#     :params valid_days: 有效天数, 默认30天
#     '''
    
#     if time.time() > start_timestamp + valid_days * 24 * 60 * 60:
#         raise Exception('已过有效期, 请更新.')

# def remove_file(file):
#     if os.path.exists(file):
#         os.remove(file)
