# 模型权重加密配置
MODEL_ENCRYPT_SETTINGS = {
    # 加密模型权重文件路径, 当为空列表时, 会匹配当前目录下所有对应pattern的模型权重文件
    'encrypt_model_path': ['./predictor/pretrained_model/yolov8n.pt'],
    'encrypt_model_pattern': '.pt', # 加密模型权重文件类型, 默认为onnx
    'encrypt_key_path': './encrypt_key.txt', # 加密key
    'encrypt_model_save_path': './output/model_weights', # 加密后的模型保存路径
}

# 打包成.so库的py文件目录
PY2SO_LIST = [
    './predictor/predict.py',
    './predictor/decrypt_utils.py',
]

# 默认配置
DEFAULT_SETTINGS = {
    'save_dir': './output'
}