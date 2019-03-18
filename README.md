# Introduction
Maix Toolbox is a collections of model tool scripts.

You can use it to convert model format from one to another.

Now it support:
```
    ckpt  ->  pb  <->  tflite  ->  kmodel
     ∧     / ∧
     |    /   |
     ∨  ∨   ∨
     graph   pbtxt
```

# Directory Structure
get_nncase.sh ：  !!!Please run it to init toolbox

ckpt2pb.py 		 

gen_ckpt_graph.py： gen graph, view via tensorboard

gen_pb_graph.py  

pb2pbtxt.py  

pb2tflite.sh  

pbtxt2pb.py  

tflite2addpad.sh：  tflite2pb, add pad

tflite2kmodel.sh： tflite2kmodel, which MAIX used

tflite2pb.sh

ncc\： nncase release version

images\：  quantization dataset images

log\：   gen_pb_graph save workspace

workspace\：    put your model inside here

