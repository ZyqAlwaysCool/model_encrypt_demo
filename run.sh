#!bin/bash

build_dir="build" #.so生成目录
export_dir="./output" #导出目录

python setup.py $build_dir

if [ ! -d "$export_dir" ]; then
    mkdir -p "$export_dir"
fi

find "$build_dir" -type f -name "*.so" -exec mv {} "$export_dir" \;

echo "build success"