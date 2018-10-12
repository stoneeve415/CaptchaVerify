# -*- coding: utf-8 -*-
from trains2 import crack_captcha_cnn
from trains2 import MAX_CAPTCHA
from trains2 import CHAR_SET_LEN
from trains2 import vec2text
from trains2 import convert2gray
from trains2 import keep_prob
from trains2 import X
from read import get_img_and_text

import numpy as np
import tensorflow as tf

def crack_captcha(captcha_image):
	output = crack_captcha_cnn()

	saver = tf.train.Saver()
	with tf.Session() as sess:
		saver.restore(sess, tf.train.latest_checkpoint('.'))

		predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
		text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})

		text = text_list[0].tolist()
		vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN)
		i = 0
		for n in text:
				vector[i*CHAR_SET_LEN + n] = 1
				i += 1
		return vec2text(vector)


text, image = get_img_and_text(100)
image = convert2gray(image)
image = image.flatten() / 255
predict_text = crack_captcha(image)
print("正确: {}  预测: {}".format(text, predict_text))