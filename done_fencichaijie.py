import jieba

seg_list = jieba.cut("北京野生动物园")
print ("Default Mode:",' '.join(seg_list))