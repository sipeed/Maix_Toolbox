#!/usr/bin/python3
import os
import sys
import tensorflow as tf


print("usage: python3 gen_ckpt_graph.py ckpt_path ckpt_meta_path")
ckpt_path = sys.argv[1]
ckpt_meta_path = sys.argv[2]

os.system("rm -f log/*")
with tf.Session() as sess:
    saver = tf.train.import_meta_graph(ckpt_meta_path)
    saver.restore(sess, tf.train.latest_checkpoint(ckpt_path))
    writer = tf.summary.FileWriter('log/', sess.graph)
    writer.close()
    os.system('tensorboard --logdir log/')

