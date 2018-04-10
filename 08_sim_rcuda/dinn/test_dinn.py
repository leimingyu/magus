#!/usr/bin/env python
import time,os,sys
import tensorflow as tf

from functools import partial

import numpy as np
import scipy.io as sio

def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)

reset_graph()



class dinn(object):
    def __init__(self, sess, n_inputs=90, n_outputs=2, n_hidden =500, 
            n_epochs = 100, batch_size=96, batch_norm_momentum = 0.9, learning_rate = 0.01):
        self.sess = sess

        self.X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
        self.y = tf.placeholder(tf.int32,   shape=(None),           name="y")

        training = tf.placeholder_with_default(False, shape=(), name='training')

        with tf.name_scope("dnn"):
            he_init = tf.contrib.layers.variance_scaling_initializer()
            
            # avoid repeating the same parameters over and over again
            my_batch_norm_layer = partial(tf.layers.batch_normalization,
                    training=training, momentum=batch_norm_momentum)
            
            my_dense_layer = partial(tf.layers.dense, kernel_initializer=he_init) # activeFunc after BN
            
            hidden1 = my_dense_layer(self.X, n_hidden, name="hidden1")
            bn1= my_batch_norm_layer(hidden1)
            bn1_act = tf.nn.elu(bn1)
            
            hidden2 = my_dense_layer(bn1_act, n_hidden, name="hidden2")
            bn2 = my_batch_norm_layer(hidden2)
            bn2_act = tf.nn.elu(bn2)
            
            hidden3 = my_dense_layer(bn2_act, n_hidden, name="hidden3")
            bn3 = my_batch_norm_layer(hidden3)
            bn3_act = tf.nn.elu(bn3)

            hidden4 = my_dense_layer(bn3_act, n_hidden, name="hidden4")
            bn4_act = tf.nn.elu(my_batch_norm_layer(hidden4))
            
            hidden5 = my_dense_layer(bn4_act, n_hidden, name="hidden5")
            bn5_act = tf.nn.elu(my_batch_norm_layer(hidden5))
            
            hidden6 = my_dense_layer(bn5_act, n_hidden, name="hidden6")
            bn6_act = tf.nn.elu(my_batch_norm_layer(hidden6))
            
            hidden7 = my_dense_layer(bn6_act, n_hidden, name="hidden7")
            bn7_act = tf.nn.elu(my_batch_norm_layer(hidden7))
            
            hidden8 = my_dense_layer(bn7_act, n_hidden, name="hidden8")
            bn8_act = tf.nn.elu(my_batch_norm_layer(hidden8))
            
            hidden9 = my_dense_layer(bn8_act, n_hidden, name="hidden9")
            bn9_act = tf.nn.elu(my_batch_norm_layer(hidden9))
            
            hidden10 = my_dense_layer(bn9_act, n_hidden, name="hidden10")
            bn10_act = tf.nn.elu(my_batch_norm_layer(hidden10))
            
            # add extra 10 layer
            hidden11 = my_dense_layer(bn10_act, n_hidden, name="hidden11")
            bn11_act = tf.nn.elu(my_batch_norm_layer(hidden11))
            
            hidden12 = my_dense_layer(bn11_act, n_hidden, name="hidden12")
            bn12_act = tf.nn.elu(my_batch_norm_layer(hidden12))
            
            hidden13 = my_dense_layer(bn12_act, n_hidden, name="hidden13")
            bn13_act = tf.nn.elu(my_batch_norm_layer(hidden13))
            
            hidden14 = my_dense_layer(bn13_act, n_hidden, name="hidden14")
            bn14_act = tf.nn.elu(my_batch_norm_layer(hidden14))
            
            hidden15 = my_dense_layer(bn14_act, n_hidden, name="hidden15")
            bn15_act = tf.nn.elu(my_batch_norm_layer(hidden15))
            
            hidden16 = my_dense_layer(bn15_act, n_hidden, name="hidden16")
            bn16_act = tf.nn.elu(my_batch_norm_layer(hidden16))
            
            hidden17 = my_dense_layer(bn16_act, n_hidden, name="hidden17")
            bn17_act = tf.nn.elu(my_batch_norm_layer(hidden17))
            
            hidden18 = my_dense_layer(bn17_act, n_hidden, name="hidden18")
            bn18_act = tf.nn.elu(my_batch_norm_layer(hidden18))
            
            hidden19 = my_dense_layer(bn18_act, n_hidden, name="hidden19")
            bn19_act = tf.nn.elu(my_batch_norm_layer(hidden19))
            
            hidden20 = my_dense_layer(bn19_act, n_hidden, name="hidden20")
            bn20_act = tf.nn.elu(my_batch_norm_layer(hidden20))
            
            
            # add extra 10 layer
            hidden21 = my_dense_layer(bn20_act, n_hidden, name="hidden21")
            bn21_act = tf.nn.elu(my_batch_norm_layer(hidden21))
            
            hidden22 = my_dense_layer(bn21_act, n_hidden, name="hidden22")
            bn22_act = tf.nn.elu(my_batch_norm_layer(hidden22))
            
            hidden23 = my_dense_layer(bn22_act, n_hidden, name="hidden23")
            bn23_act = tf.nn.elu(my_batch_norm_layer(hidden23))
            
            hidden24 = my_dense_layer(bn23_act, n_hidden, name="hidden24")
            bn24_act = tf.nn.elu(my_batch_norm_layer(hidden24))
            
            hidden25 = my_dense_layer(bn24_act, n_hidden, name="hidden25")
            bn25_act = tf.nn.elu(my_batch_norm_layer(hidden25))
            
            hidden26 = my_dense_layer(bn25_act, n_hidden, name="hidden26")
            bn26_act = tf.nn.elu(my_batch_norm_layer(hidden26))
            
            hidden27 = my_dense_layer(bn26_act, n_hidden, name="hidden27")
            bn27_act = tf.nn.elu(my_batch_norm_layer(hidden27))
            
            hidden28 = my_dense_layer(bn27_act, n_hidden, name="hidden28")
            bn28_act = tf.nn.elu(my_batch_norm_layer(hidden28))
            
            hidden29 = my_dense_layer(bn28_act, n_hidden, name="hidden29")
            bn29_act = tf.nn.elu(my_batch_norm_layer(hidden29))
            
            hidden30 = my_dense_layer(bn29_act, n_hidden, name="hidden30")
            bn30_act = tf.nn.elu(my_batch_norm_layer(hidden30))
            
            logits_before_bn = my_dense_layer(bn30_act, n_outputs, name="outputs")
            self.logits = my_batch_norm_layer(logits_before_bn)
            
        with tf.name_scope("loss"):
            xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.y, logits=self.logits)
            loss = tf.reduce_mean(xentropy, name="loss")

        with tf.name_scope("train"):
            optimizer = tf.train.GradientDescentOptimizer(learning_rate)
            training_op = optimizer.minimize(loss)
            
        with tf.name_scope("eval"):
            correct = tf.nn.in_top_k(self.logits, self.y, 1)
            accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
        
        init = tf.global_variables_initializer()
        self.sess.run(init)
        self.saver = tf.train.Saver()
        print("[*] Initialize model successfully...")

    def test(self, testX, ckpt_model="./models/dinn_final.ckpt"):
        self.saver.restore(self.sess, ckpt_model)
        logits_pred = self.sess.run([self.logits], feed_dict={self.X: testX})
        print logits_pred




#print("Run Tensorflow [GPU]\n")
#gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)
#sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
#dpModel = dinn(sess)  # init a dinn class



#
# read data
#
app2dinnfeats_dd = np.load('./app2dinnFeats_dd.npy').item()

print len(app2dinnfeats_dd)

count = 0
for key, value in app2dinnfeats_dd.iteritems():
    print key
    if count >=3:
        break
    count = count + 1


# use "rodinia_b+tree"  and  "cudasdk_reduction"

app1 = app2dinnfeats_dd["rodinia_b+tree"]
app2 = app2dinnfeats_dd["cudasdk_reduction"]
app3 = app2dinnfeats_dd["cudasdk_convolutionFFT2D"]
app4 = app2dinnfeats_dd["shoc_lev1BFS"]

#combo = np.append(app1,app2)
#print type(combo)
#print combo
#print combo.shape
#
#combo = combo.reshape((1,90)) 
#print combo.shape

test_input = None
test_input = np.append(app1,app2)
combo = np.append(app3,app4)
test_input = np.vstack((test_input, combo))

print test_input.shape


gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))



##
## use the pre-trained model
##
#X,logits,trained_model = model_init()
#
###with tf.Session() as sess:
###    trained_model.restore(sess, "./models/dinn_final.ckpt")
###    logits_pred = sess.run([logits], feed_dict={X: test_input})
###    print logits_pred
#
#trained_model.restore(sess, "./models/dinn_final.ckpt")
#logits_pred = sess.run([logits], feed_dict={X: test_input})
#print logits_pred
#


dpModel = dinn(sess)

print "test1"
dpModel.test(test_input)
print "test2"
dpModel.test(test_input)
