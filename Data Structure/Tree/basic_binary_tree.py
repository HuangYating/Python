#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from binary_node import*


class BasicBinaryTree(object):

    def __init__(self):
        self.root = None

    #添加结点（无排序）
    def add_node(self,data):
        if self.root == None:
            self.root = BinaryNode(data)
            return
        queue = Queue()
        queue.push(self.root)
        while queue.is_empty() == 0:
            top = queue.pop().data
            if top.left_child == None:
                top.left_child = BinaryNode(data)
                return
            elif top.right_child == None:
                top.right_child = BinaryNode(data)
                return
            else:
                queue.push(top.left_child)
                queue.push(top.right_child) 

'''建树 15 11 10 20 40 8 43 6 12 9'''
'''  不排序                      排序
        15                       15
       /  \                     /  \
      11   10                  11   20
      / \  / \                /  \  / \
    20  40 8  43             10  12    40
    /\  /                    /          \
   6 12 9                   8            43
                           / \
                          6   9
'''
if __name__=='__main__':

    '''测试BasicBinaryTree类'''
    bi_tree=BasicBinaryTree() 
    print('添加结点15,11,10,20,40,8,43,6,12,9（无排序）')
    bi_tree.add_node(15)
    bi_tree.add_node(11)
    bi_tree.add_node(10)
    bi_tree.add_node(20) 
    bi_tree.add_node(40)
    bi_tree.add_node(8)
    bi_tree.add_node(43)
    bi_tree.add_node(6)
    bi_tree.add_node(12)
    bi_tree.add_node(9) 

    print("前序遍历：15 11 20 6 12 40 9 10 8 43") 
    bi_tree.root.preorder_traversal(bi_tree.root)

    print("中序遍历：6 20 12 11 9 40 15 8 10 43")
    bi_tree.root.inorder_traversal(bi_tree.root)

    print("后序遍历：6 12 20 9 40 11 8 43 10 15")
    bi_tree.root.postorder_traversal(bi_tree.root)

    print("深度优先遍历：15 11 10 20 40 8 43 6 12 9")
    bi_tree.root.breadth_first_traversal(bi_tree.root)


    
