# -*- coding: utf-8 -*-
'''
@author: Infaraway
@time: 2017/3/31 0:14
@Function:
'''


class treeNode:
    def __init__(self, name_value, num_occur, parent_node):
        self.name = name_value
        self.count = num_occur
        self.node_link = None
        self.parent = parent_node
        self.children = {}

    def increase(self, num_occur):
        """
        增加节点的出现次数
        :param num_occur: 增加数量
        :return:
        """
        self.count += num_occur

    def disp(self, ind=1):
        print('  ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)

