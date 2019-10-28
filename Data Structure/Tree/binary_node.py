#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
from queue import*

class BinaryNode(object):

    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    #深度优先遍历（前序、中序、后序遍历）
    #前序遍历
    def preorder_traversal(self, root):
        print(root.data)
        if root.left_child != None:
            self.preorder_traversal(root.left_child)
        if root.right_child != None :
            self.preorder_traversal(root.right_child)

    #中序遍历
    def inorder_traversal(self, root):
        if root.left_child != None :
            self.inorder_traversal(root.left_child)
        print(root.data)
        if root.right_child != None :
            self.inorder_traversal(root.right_child)

    #后序遍历
    def postorder_traversal(self, root):
        if root.left_child != None :
            self.postorder_traversal(root.left_child)
        if root.right_child != None :
            self.postorder_traversal(root.right_child)
        print(root.data)

    #广度优先遍历
    def breadth_first_traversal(self, root):
        queue=Queue()
        queue.push(root)
        #处理队列，直到其变空
        while queue.is_empty() == 0:
            top=queue.pop().data
            print(top.data)
            if top.left_child != None:
                queue.push(top.left_child)
            if top.right_child != None:
                queue.push(top.right_child)
