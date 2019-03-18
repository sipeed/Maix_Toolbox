#!/usr/bin/python3
import tensorflow as tf
import sys
import os

print("usage: python3 ckpt_path ckpt_meta_path output_node_names ")
ckpt_path = sys.argv[1]
ckpt_meta_path = sys.argv[2]
output_node_names = sys.argv[3]
with tf.Session() as sess:
	saver = tf.train.import_meta_graph(ckpt_meta_path)
	saver.restore(sess, tf.train.latest_checkpoint(ckpt_path))
	output_graph_def = tf.graph_util.convert_variables_to_constants(  # 模型持久化，将变量值固定
	sess=sess,
	input_graph_def=sess.graph_def,# 等于:sess.graph_def
	output_node_names=output_node_names.split(","))# 如果有多个输出节点，以逗号隔开
	with tf.gfile.GFile(ckpt_meta_path+'.pb', "wb") as f: #保存模型
		f.write(output_graph_def.SerializeToString()) #序列化输出
	print("%d ops in the final graph." % len(output_graph_def.node))


