from ultralytics import YOLO
from decrypt_utils import *

EN_KEY = 'fCA25Wyr_vRDdhQ5Tq-8MvJt5psMfC_krl9B8YKeSiE=' # 秘钥
START_TIMESTAMP = 1722928154 # 模型开始使用时间戳

def get_model(model_path):
    # 校验时间戳
    check_timestamp(START_TIMESTAMP)
    
    # 解密模型权重
    decrypt_model_weights = model_path.replace('-en', '')
    model_decryption(model_path, decrypt_model_weights, EN_KEY)
    
    # load model
    model = YOLO(decrypt_model_weights)

    #删除解密模型文件
    remove_file(decrypt_model_weights)
    
    return model

if __name__ == '__main__':
    model_path = '/home/kemove/zyq/giit/model_encrypt/predictor/pretrained_model/yolov8n.pt'
    model = get_model(model_path)
    print(type(model))