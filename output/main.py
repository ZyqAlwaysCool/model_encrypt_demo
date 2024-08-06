from predict import *

if __name__ == '__main__':
    model_path = '/home/kemove/zyq/giit/model_encrypt/output/model_weights/yolov8n.pt-en'
    model = get_model(model_path)
    print(type(model))