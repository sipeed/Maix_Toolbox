#!/usr/bin/python3
import tensorflow as tf
from tensorflow.python.platform import gfile
from google.protobuf import text_format
import sys



def convert_pb_to_pbtxt(filename):
    with gfile.FastGFile(filename,'rb') as f:
        graph_def = tf.GraphDef()     
        graph_def.ParseFromString(f.read())       
        tf.import_graph_def(graph_def, name='') 
        tmp=filename.split('.')
        outname=tmp[0]+".pbtxt"
        tf.train.write_graph(graph_def, './', outname, as_text=True)
        return

print("usage: python3 pb2pbtxt.py xxx.pb")
fname=sys.argv[1]
convert_pb_to_pbtxt(fname)
