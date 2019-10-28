#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 线索树，这里建立的线索是按中序遍历的顺序从一个结点指向另一个'''
class ThreadedBinaryNode:

    '''
    初始化函数
    data ：结点数值
    l_tag, r_tag ： 指针标志； 1表示线索指针（可能为空指针），0表示左子树指针 
    left, right : 左子树指针或者左线索指针，右子树指针或者右子树指针
    '''
    def __init__(self, data, l_tag=1, r_tag=1, left=None, right=None):
        self.data = data
        self.l_tag = l_tag
        self.r_tag = r_tag
        self.left = left
        self.right = right

    # 中序遍历
    def inorder_traversal(self, root):
        node = root  
        branch_tag = 1 # 该结点的指标标志，1表示子树指针，0表示线索指针
        while node is not None: 
            # 如果该结点是子树，则尽可能的找到最左的子结点
            if branch_tag == 1: 
                while node.l_tag == 0:
                    node = node.left 
            # 打印结点值
            print(node.data)
            # 下一个处理的结点 
            if node.r_tag == 1: 
                branch_tag = 0 
            else:
                branch_tag = 1
            node = node.right

    # 反转遍历 （结点从大到小）
    def reverse_traversal(self, root):
        node = root
        branch_tag = 1 # 该结点的指标标志，1表示子树指针，0表示线索指针
        while node is not None:
            # 如果该结点是子树，则尽可能的找到最右的子结点
            if branch_tag == 1:
                while node.r_tag == 0:
                    node = node.right
            #打印结点值
            print(node.data)
            #处理下一个结点
            if node.l_tag == 1:
                branch_tag = 0
            else:
                branch_tag = 1
            node = node.left



class ThreadedBinaryTree:

    def __init__(self):
        self.root = None

    # 添加结点
    def add_node(self, data):
        if self.root == None:
            self.root = ThreadedBinaryNode(data)
        else:
            self.__private_add_node(self.root, data) 
    def __private_add_node(self, node, data):
        if node.data > data:
            if node.l_tag == 1:
                # 添加到左子结点
                tmp = ThreadedBinaryNode(data) # 新添加的结点 
                tmp.left = node.left # 左指针设为父结点的左指针  
                tmp.right = node # 右指针指向父结点
                node.l_tag = 0 # 左指针为左子树指针
                node.left = tmp 

            else:
                self.__private_add_node(node.left, data)
        else:
            if node.r_tag == 1:
                # 添加到右子结点
                tmp = ThreadedBinaryNode(data) # 新添加的结点
                tmp.right = node.right # 右指针设为父结点的右指针  
                tmp.left = node # 左指针指向父结点
                node.r_tag = 0 # 右指针为右子树指针
                node.right = tmp
            else:
                self.__private_add_node(node.right, data)


'''建树 15 11 10 20 40 8 43 6 12 9'''
'''   
        15
       /  \
      11   20
     /  \  / \
    10  12    40
    /          \
   8            43
  / \
 6   9
'''        

if __name__ == '__main__':
    th_b_tree = ThreadedBinaryTree()
    print('添加结点15,11,10,20,40,8,43,6,12,9')
    th_b_tree.add_node(15) 
    th_b_tree.add_node(11)
    th_b_tree.add_node(10)
    th_b_tree.add_node(20)
    th_b_tree.add_node(40) 
    th_b_tree.add_node(8)
    th_b_tree.add_node(43)
    th_b_tree.add_node(6)
    th_b_tree.add_node(12)
    th_b_tree.add_node(9)  

    
    print("中序遍历：")
    th_b_tree.root.inorder_traversal(th_b_tree.root)  

    print("反转遍历：")
    th_b_tree.root.reverse_traversal(th_b_tree.root)  

