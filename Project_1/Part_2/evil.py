#!/usr/bin/python
# -*- coding: utf-8 -*-

blob = """        �����ސ�a�P޺�~�&{�#�:�
гj����'k�#�w�����\�^K�t՚� Y�њ���Ml�{:W�<p#�)��Ɗ_h��-����2>:?;�(�T�ӢR��z��S�F͊"""
from hashlib import sha256
if sha256(blob).hexdigest() == "52852f84abc5339c02ce23a5de085d4ddbdf32d4315d175f8cef4b1039ed7c43":
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
