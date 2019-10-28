#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from binary_node import*

'''中序遍历访问结点的顺序是有序的'''
class InorderdBinaryTree(object):
    def __init__(self):
        self.root = None

    # 添加结点（每个结点的值都大于其左子节点且小于（或等于）其右子结点的值） 
    def add_node(self, data):
        self.__private_add_node(self.root, data)

    def __private_add_node(self, node, data):
        if self.root == None:
            self.root = BinaryNode(data)
            return 
        if node.data > data:
            if node.left_child == None:
                node.left_child = BinaryNode(data)
                return
            self.__private_add_node(node.left_child, data)
        else:
            if node.right_child == None:
                node.right_child = BinaryNode(data)
                return
            self.__private_add_node(node.right_child, data) 

    '''
    # 采用非递归的方法添加结点
    def add_node(self,data):
        node = self.root
        if node == None:
            self.root = BinaryNode(data) 
            return
        while True:
            if node.data > data:
                if node.left_child == None:
                    node.left_child = BinaryNode(data) 
                    return
                node = node.left_child
            elif node.data <= data:
                if node.right_child == None:
                    node.right_child = BinaryNode(data) 
                    return
                node = node.right_child     
    '''

    
    # 查找结点（返回第一个值为data的结点） 
    def find_node(self, data):
        if self.root == None: # 树为空，返回None
            return None
        return self.__private_find_node(self.root, data)

    def __private_find_node(self, node ,data): 
        if node.data == data: # 结点值为data，返回该结点
            return node
        if node.data > data: # 结点值大于data，目标结点在左子树
            if node.left_child == None: # 目标结点不存在，返回None
                return None
            self.__private_find_node(node.left_child, data)
        else: # 结点值小于data，目标结点在右子树
            if node.right_child == None: # 目标结点不存在，返回None
                return None
            self.__private_find_node(node.right_child, data)

    '''
    # 采用非递归的方法查找结点
    def find_node(self, data):
        # 如果树根为空，返回None
        if self.root == None:
            return None
        target = self.root
        while target.data != data:
            if target.data > data:
                if target.left_child !=None:
                    target = target.left_child
                else:
                    return None
            else:
                if target.right_child != None:
                    target = target.right_child
                else:
                    return None
        return target
    '''

    # 查找父结点 
    def find_parent(self, target_node):
        if self.root == None: # 树为空 
            return None
        if self.root == target_node: 
            return None # 根结点没有父结点  
        return self.__private_find_parent(self.root, target_node)

    def __private_find_parent(self, tmp_node, target_node):  
        if tmp_node.data > target_node.data: 
            if tmp_node.left_child == None: # 目标结点不在树中  
                return None 
            if tmp_node.left_child == target_node: # 左子结点为目标结点 
                return tmp_node
            return self.__private_find_parent(tmp_node.left_child, target_node)
        else: 
            if tmp_node.right_child == None: # 目标结点不在树中 
                return None
            if tmp_node.right_child == target_node:# 右子结点为目标结点 
                return tmp_node 
            return self.__private_find_parent(tmp_node.right_child, target_node)
    
    '''
    # 采用非递归的方式查找父结点 
    def find_parent(self, target_node):
        if self.root == None:
            return None
        if self.root == target_node:
            return None
        result = self.root
        while result != None:
            if result.left_child != None:
                if result.left_child == target_node:
                    return result
            if result.right_child != None:
                if result.right_child == target_node:
                    return result
            if result.data > target_node.data:
                result = result.left_child
            else:
                result = result.right_child
    '''

    #删除结点   
    def delete_node(self, target):
        if target == self.root:
            if target != None:
                if target.left_child == None:
                    if target.right_child == None: 
                        # 根结点没有子结点
                        self.root = None
                    else:
                        # 根结点只有右子结点
                        self.root = target.right_child
                else:
                    if target.right_child == None:
                        # 根结点只有左子结点
                        self.root = target.left_child
                    else:
                        # 根结点既有左子结点也有右子结点
                        target_left_biggest = target.left_child
                        while target_left_biggest.right_child != None:
                            target_left_biggest = target_left_biggest.right_child 
                        target_left_biggest.right_child = target.right_child
                        self.root = target.left_child

        else:
            parent = self.find_parent(target) 
            if parent != None:
                if target.left_child == None:
                    if target.right_child == None:
                        # 目标结点没有子结点，也就是叶子结点，则直接删除 
                        if parent.left_child == target: 
                            parent.left_child = None
                        else:
                            parent.right_child = None
                    else:
                        # 目标结点只有右子结点，则用右子结点替代目标结点
                        if parent.left_child == target:
                            parent.left_child = target.right_child
                        else:
                            parent.right_child = target.right_child
                else:
                    if target.right_child == None:
                        # 目标结点只有左子结点，则用左子结点替代目标结点
                        if parent.left_child == target:
                            parent.left_child = target.left_child
                        else:
                            parent.right_child = target.left_child
                    else: 
                        # 目标结点既有左子结点也有右子结点,
                        # 则可以用目标结点的左子结点替代目标结点，同时将目标结点的右子树移到其左子树的最大结点的右子结点上
                        target_left_biggest = target.left_child
                        while target_left_biggest.right_child != None:
                            target_left_biggest = target_left_biggest.right_child 
                        target_left_biggest.right_child = target.right_child
                        if parent.left_child == target:
                            parent.left_child = target.left_child
                        else:
                            parent.right_child = target.left_child
 
# 返回树的结点个数
    def size(self):
        count = 0 # 用于结点计数
        #如果树根为空，返回0
        if self.root == None:
            return count
        #建立队列，利用广度优先遍历来计算结点个数
        queue = Queue()
        queue.push(self.root)
        while not queue.is_empty():
            top = queue.pop().data
            count += 1
            if top.left_child != None:
                queue.push(top.left_child)
            if top.right_child != None:
                queue.push(top.right_child)
        return count



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

    '''测试InorderdBinaryTree类'''

    bi_tree=InorderdBinaryTree()

    print('空树的结点个数：')
    print(bi_tree.size()) # 0

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

    print('插入10个结点后的结点个数：')
    print(bi_tree.size()) # 10

    print('查找值为15的结点')
    tmp = bi_tree.find_node(15)
    print(tmp, tmp.data) 

    print('查找值为100的结点（并不存在）')
    print(bi_tree.find_node(100))

    print('查找根结点左子结点的父结点，输出地址和值')  
    tmp = bi_tree.find_parent(bi_tree.root.left_child)
    print(tmp, tmp.data) 

    
    print("前序遍历：15 11 10 8 6 9 12 20 40 43") 
    bi_tree.root.preorder_traversal(bi_tree.root)

    print('删除叶节点6')
    bi_tree.delete_node(bi_tree.root.left_child.left_child.left_child.left_child)
    print("中序遍历：8 9 10 11 12 15 20 40 43 从小到大")
    bi_tree.root.inorder_traversal(bi_tree.root)
    
    print('删除结点40（只有一个子结点）') 
    bi_tree.delete_node(bi_tree.root.right_child.right_child)
    print("后序遍历：9 8 10 12 11 43 20 15")
    bi_tree.root.postorder_traversal(bi_tree.root)

    print('删除结点11（有左右子结点）') 
    bi_tree.delete_node(bi_tree.root.left_child)
    print("广度优先遍历：15 10 20 8 12 43 9")
    bi_tree.root.breadth_first_traversal(bi_tree.root)

    print('删除根结点15') 
    bi_tree.delete_node(bi_tree.root)
    print("广度优先遍历：10 8 12 9 20 43")
    bi_tree.root.breadth_first_traversal(bi_tree.root)
  
