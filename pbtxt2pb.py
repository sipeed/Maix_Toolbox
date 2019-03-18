#!/usr/bin/python3
import tensorflow as tf
from tensorflow.python.platform import gfile
from google.protobuf import text_format
import sys
 
def convert_pbtxt_to_pb(filename):
    with tf.gfile.FastGFile(filename, 'r') as f:
        graph_def = tf.GraphDef()                           
        file_content = f.read()                                                                
        # Merges the human-readable string in `file_content` into `graph_def`.
        text_format.Merge(file_content, graph_def)
        tmp=filename.split('.')
        outname=tmp[0]+".pb"
        tf.train.write_graph( graph_def , './' , outname , as_text = False )

printf("usage: python3 pbtxt2pb.py xxx.pbtxt")
fname=sys.argv[1]
convert_pbtxt_to_pb(fname)
