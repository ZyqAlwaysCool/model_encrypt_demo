## README.md
### 简介
本项目将用一个基于yolo训练的模型为例，演示ai模型私有化部署加密步骤。

> 文件说明
* setup.py: 将python文件编译为.so库
* run.sh: 执行py到.so转换
* encrypt_weights.py: 加密模型权重
* config.py: 转换相关配置文件, **需根据实际修改**
* meter_crack: 测试模型及推理文件
* output: 默认输出文件夹, 存放转换后的.so库和加密后的模型
* encrypt_key.txt: 秘钥文件, 默认由encrypt_weights.py生成, 可在config.py中修改文件名
* decrypt_utils_demo.py: 解密工具包, 拷贝到推理代码目录下进行改造

### 操作步骤
#### 1. 加密模型权重
* 基于实际修改config.py中的`encrypt_model_path`字段, 配置需要加密的模型权重路径
* 执行`python encrypt_weights.py`, 加密模型权重保存在`encrypt_model_save_path`字段配置的路径下, 并输出秘钥文件

#### 2. 推理代码改造
* 拷贝decrypt_utils.py到推理代码目录下
* 修改模型推理代码, 添加解密和有效期校验逻辑
  ```python
  # 示例代码
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
    ...
  ```
#### 3. 编译.so文件
* 在config.py中配置`py2so_list`字段, 添加需要编译为.so库的源代码文件
* 执行`bash run.sh`
* .so文件默认输出到`./output`目录下

#### 4. 测试
* 测试代码: 参考`./output/main.py`

### 参考
* [python打包.so](https://www.cnblogs.com/lidabo/p/17043275.html)
* [python文件加解密](https://blog.csdn.net/qq_44873474/article/details/133775118)
  
