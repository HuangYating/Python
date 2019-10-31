#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from queue import*

class AVLNode:
    """ The structure to store AVL nodes.

    Attributes:
        data: The data stored in the node
        left: The left children
        right: The right children
        height: The height of the tree
        balance_factor: balance_factor = the height of the left children 
                                        - the height of the right children,
                        all posible values are 0, 1 and -1
    """
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0
        self.balance_factor = 0


    def inorder_traversal(self, root):
        if root.left_child != None :
            self.inorder_traversal(root.left_child)
        print('data:%d'%root.data, '  height:%d'%root.height, '  balance factor:%d'%root.balance_factor)
        if root.right_child != None :
            self.inorder_traversal(root.right_child)


    def breadth_first_traversal(self, root):
        queue=Queue()
        queue.push(root) 
        while queue.is_empty() == 0:
            top=queue.pop().data
            print('data:%d'%top.data, '  height:%d'%top.height, '  balance factor:%d'%top.balance_factor)
            if top.left_child != None:
                queue.push(top.left_child)
            if top.right_child != None:
                queue.push(top.right_child)



class AVLTree:

    def __init__(self, root=None):
        self.root = root

    
    def find_node(self, data):
        """Find the first node that has the data"""

        if self.root == None: # the tree is empty ,returns None
            return None
        return self.__private_find_node(self.root, data)

    def __private_find_node(self, node ,data): 
        if node.data == data: # find the node
            return node
        if node.data > data: # the target node is on the left child tree
            if node.left_child == None: # the target node doesn't exist
                return None
            self.__private_find_node(node.left_child, data)
        else: # the target node is on the right child tree
            if node.right_child == None: # the target node doesn't exist
                return None
            self.__private_find_node(node.right_child, data)




    def find_parent(self, target_node):
        """Find the parent node of the target node"""

        if self.root == None: # the root is None
            return None
        if self.root == target_node: 
            return None # the root doesn't hava the parent  
        return self.__private_find_parent(self.root, target_node)

    def __private_find_parent(self, tmp_node, target_node):  
        if tmp_node.data > target_node.data: 
            if tmp_node.left_child == None: # the target node isn't in the tree 
                return None 
            if tmp_node.left_child == target_node: # the target node is in the left tree
                return tmp_node
            return self.__private_find_parent(tmp_node.left_child, target_node)
        else: 
            if tmp_node.right_child == None: # the target node isn't in the tree 
                return None
            if tmp_node.right_child == target_node:# the target node is in the right tree
                return tmp_node 
            return self.__private_find_parent(tmp_node.right_child, target_node)



    def add_node(self, data):
        """ Add new node into the AVL tree. 
        """

        if self.root == None:
            self.root = AVLNode(data)
            self.root.height = 1
            return 
        self.__private_add_node(self.root, data)

    def __private_add_node(self, node, data):
        if node.data > data:
            if node.left_child == None:
                node.left_child = AVLNode(data)
                node.left_child.height = 1 
            else:
                self.__private_add_node(node.left_child, data)

            # calculate the height and the balance factor of the node
            self.__calculate_height_bfactor(node)

            if abs(node.balance_factor) > 1: 
                # the node tree is not balanced
                self.__rotation_operation(node)

        else:
            if node.right_child == None:
                node.right_child = AVLNode(data)
                node.right_child.height = 1
            else:
                self.__private_add_node(node.right_child, data)

            # calculate the height and the balance factor of the node
            self.__calculate_height_bfactor(node)

            if abs(node.balance_factor) > 1: 
                # the node tree is not balanced
                self.__rotation_operation(node)


    def delete_node(self, target):
        """ Delete the target node from the AVL tree.
            Rotation operations is needed if the tree is not balanced after deleting the target node.
        """

        tmp_node = target # tmp_node represents the first node that it and its ancestors needs 
                          # to update their heights and balance factors. (bottom up)

        # the target node is the root 
        if target == self.root: 
            if target != None: # the root is not None
                if target.left_child == None:
                    if target.right_child == None: 
                        # the root doesn't have children
                        # rotation is not needed
                        self.root = None
                    else:
                        # the root only has the right child
                        # rotation is not needed
                        self.root = target.right_child
                else:
                    if target.right_child == None:
                        # the root only has the left child
                        # rotation is not needed
                        self.root = target.left_child
                    else:
                        # the root has both the left and the right child

                        ''' Find the biggest node of the left child tree of the root,
                            1. if the node doesn't have right child, and replace the root with it;
                            2. if the node has the right child:
                                2.1 if the right child doesn't have a left child (it surely has no right child), 
                                    then replace the root with the right child
                                2.2 if the right child has a left child, then replace the right child with its left child
                                    and replace the root with the right child
                        '''
                        target_left_biggest = target.left_child 
                        if target_left_biggest.right_child == None:
                            # case 1
                            target_left_biggest.right_child = self.root.right_child
                            self.root = target_left_biggest

                            tmp_node = target_left_biggest.right_child
                        else:
                            # case 2
                            while target_left_biggest.right_child != None:
                                target_left_biggest = target_left_biggest.right_child

                            tmp_node = self.find_parent(target_left_biggest)

                            if target_left_biggest.left_child == None:
                                # case 2.1
                                self.root.data = target_left_biggest.data
                                tmp_node.right_child = None 
                            else:
                                # case 2.2
                                self.root.data = target_left_biggest.data
                                tmp_node.right_child = target_left_biggest.left_child
                                

                        '''Updata the heights and balance fators of "tmp_node" and its ancestors, 
                            and Rotate when a node is not balanced. 
                        '''
                        self.__calculate_height_bfactor(tmp_node) 
                        if abs(tmp_node.balance_factor) > 1: 
                            self.__rotation_operation(tmp_node)

                        parent = self.find_parent(tmp_node)
                        while parent is not None:
                            self.__calculate_height_bfactor(parent)
                            if abs(parent.balance_factor) > 1:
                                self.__rotation_operation(parent)
                            parent = self.find_parent(parent)

        else:
            # the target node is not the root 
            parent = self.find_parent(target) 
            if parent != None: # target exists
                if target.left_child == None:
                    if target.right_child == None:
                        # the target node doesn't have children 
                        if parent.left_child == target: 
                            parent.left_child = None
                        else:
                            parent.right_child = None

                        if parent.right_child == None:
                            tmp_node = parent 
                        else:
                            tmp_node = parent.right_child
                    else:
                        # the target node only has the right child, then replace the node with its right child  

                        if parent.left_child == target: 
                            parent.left_child = target.right_child
                        else:
                            parent.right_child = target.right_child

                        ''' the node "target.right_child " becomes the first node 
                            that it and its ancestors needs to update their heights and balance factors (bottom up)
                        '''
                        tmp_node = target.right_child 

                else:
                    if target.right_child == None:
                        # the target node only has the left child, then replace the node with its left child 

                        if parent.left_child == target:
                            parent.left_child = target.left_child
                        else:
                            parent.right_child = target.left_child

                        ''' the node "target.left_child " becomes the first node 
                            that it and its ancestors needs to update their heights and balance factors (bottom up)
                        '''
                        tmp_node = target.left_child 
                    else: 
                        # the target node has both the left and the right child

                        ''' Find the biggest node of the left child tree of the target node,
                            1. if the node doesn't have right child, and replace the target node with it;
                            2. if the node has the right child:
                                2.1 if the right child doesn't have a left child (it surely has no right child), 
                                    then replace the target node with the right child
                                2.2 if the right child has a left child, then replace the right child with its left child
                                    and replace the target node with the right child
                        '''
                        target_left_biggest = target.left_child 
                        if target_left_biggest.right_child == None:
                            # case 1
                            target_left_biggest.right_child = target.right_child
                            target = target_left_biggest

                            tmp_node = target_left_biggest.right_child
                        else:
                            # case 2
                            while target_left_biggest.right_child != None:
                                target_left_biggest = target_left_biggest.right_child

                            tmp_node = self.find_parent(target_left_biggest)

                            if target_left_biggest.left_child == None:
                                # case 2.1
                                target.data = target_left_biggest.data
                                tmp_node.right_child = None 
                            else:
                                # case 2.2
                                target.data = target_left_biggest.data
                                tmp_node.right_child = target_left_biggest.left_child
                                

            '''Updata the heights and balance fators of "tmp_node" and its ancestors, 
                and Rotate when a node is not balanced. 
            '''
            self.__calculate_height_bfactor(tmp_node) 
            if abs(tmp_node.balance_factor) > 1: 
                    self.__rotation_operation(tmp_node)

            parent = self.find_parent(tmp_node)  
            while parent is not None:
                self.__calculate_height_bfactor(parent)  
                if abs(parent.balance_factor) > 1: 
                    self.__rotation_operation(parent)
                parent = self.find_parent(parent) 


    def __rotation_operation(self, node):  
        """ Rotation operations of the tree when the node is not balanced"""

        if node.balance_factor == 2:
            if node.left_child is not None and node.left_child.balance_factor == 1:
                # the new node is on the left child tree of the left child of the node 
                # need one right rotation operation 

                ''' the right rotation operaton'''
                tmp = node.left_child
                if tmp.right_child is not None:
                    node.left_child = tmp.right_child
                else: 
                    node.left_child = None  
                tmp.right_child = node  

                if node == self.root: 
                    self.root = tmp 
                else:
                    parent = self.find_parent(node)
                    if parent.left_child == node: 
                        parent.left_child = tmp
                    else:  
                        parent.right_child = tmp

                '''
                Update heights and balance factors.
                besides the two rotation nodes, 
                all ancestors of "node" also have to update their heights and balance factors.
                '''
                parent = self.find_parent(node)
                node.height = node.height -2 
                node.balance_factor = 0
                parent.balance_factor = 0
                tmp_node = self.find_parent(parent)
                while tmp_node is not None:
                    self.__calculate_height_bfactor(tmp_node)
                    tmp_node = self.find_parent(tmp_node)


            elif node.left_child is not None and node.left_child.balance_factor == -1:
                # the new node is on the right child tree of the left child of the node
                # need one left rotation operation and one right rotation operation

                ''' the left rotaion operation'''
                tmp = node.left_child.right_child
                if tmp.left_child is not None:
                    node.left_child.right_child = tmp.left_child
                else:
                    node.left_child.right_child = None
                tmp.left_child = node.left_child
                node.left_child = tmp

                ''' the right rotation operaton'''
                tmp = node.left_child
                if tmp.right_child is not None:
                    node.left_child = tmp.right_child
                else: 
                    node.left_child = None  
                tmp.right_child = node  

                if node == self.root: 
                    self.root = tmp 
                else:
                    parent = self.find_parent(node)
                    if parent.left_child == node: 
                        parent.left_child = tmp
                    else:  
                        parent.right_child = tmp

                '''
                Update heights and balance factors.
                besides the three rotation nodes, 
                all ancestors of "node" also have to update their heights and balance factors.
                '''
                parent = self.find_parent(node)
                node.height -= 2 
                parent.height += 1
                parent.left_child.height -= 1
                node.balance_factor = 0
                parent.balance_factor = 0
                parent.left_child.balance_factor = 0
                tmp_node = self.find_parent(parent)
                while tmp_node is not None:
                    self.__calculate_height_bfactor(tmp_node)
                    tmp_node = self.find_parent(tmp_node)

        elif node.balance_factor == -2:
            if node.right_child is not None and node.right_child.balance_factor == 1:
                # the new node is on the left child tree of the right child of the node
                # one right rotation operation and one left rotation operation   

                ''' the right rotation operation'''
                tmp = node.right_child.left_child
                if tmp.right_child is not None:
                    node.right_child.left_child = tmp.right_child
                else:
                    node.right_child.left_child = None
                tmp.right_child = node.right_child 
                node.right_child = tmp

                ''' the left rotaion operation'''
                tmp = node.right_child
                if tmp.left_child is not None:
                    node.right_child = tmp.left_child
                else:
                    node.right_child = None
                tmp.left_child = node

                if node == self.root: 
                    self.root = tmp 
                else:
                    parent = self.find_parent(node)
                    if parent.left_child == node: 
                        parent.left_child = tmp
                    else:  
                        parent.right_child = tmp

                '''
                Update heights and balance factors.
                besides the three rotation nodes, 
                all ancestors of "node" also have to update their heights and balance factors.
                '''
                parent = self.find_parent(node)
                node.height -= 2 
                parent.height += 1
                parent.right_child.height -= 1
                node.balance_factor = 0
                parent.balance_factor = 0
                parent.right_child.balance_factor = 0
                tmp_node = self.find_parent(parent)
                while tmp_node is not None:
                    self.__calculate_height_bfactor(tmp_node)
                    tmp_node = self.find_parent(tmp_node)

            elif node.right_child is not None and node.right_child.balance_factor == -1:
                # the new node is on the right child tree of the right child of the node
                # one left rotation operation
                tmp = node.right_child 
                if tmp.left_child is not None:
                    node.right_child = tmp.left_child
                else:
                    node.right_child = None
                tmp.left_child = node 

                if node == self.root: 
                    self.root = tmp 
                else:
                    parent = self.find_parent(node)
                    if parent.left_child == node: 
                        parent.left_child = tmp
                    else:  
                        parent.right_child = tmp

                '''
                Update heights and balance factors.
                besides the two rotation nodes, 
                all ancestors of "node" also have to update their heights and balance factors.
                '''
                parent = self.find_parent(node)
                node.height = node.height -2 
                node.balance_factor = 0
                parent.balance_factor = 0
                tmp_node = self.find_parent(parent)
                while tmp_node is not None:
                    self.__calculate_height_bfactor(tmp_node)
                    tmp_node = self.find_parent(tmp_node)


    def __calculate_height_bfactor(self, node): 
        """ Calculate the height and the balance factor of the node"""
        if node.left_child == None:
            if node.right_child == None:
                # leaf node
                node.height = 1 
                node.balance_factor = 0
            else: 
                # only has the right node
                node.height = node.right_child.height + 1
                node.balance_factor = 0 - node.right_child.height
        else:
            if node.right_child == None:
                # only has the left node
                node.height = node.left_child.height + 1
                node.balance_factor = node.left_child.height
            else:
                # has both the left node and the right node
                node.height = max(node.left_child.height, node.right_child.height) + 1
                node.balance_factor = node.left_child.height - node.right_child.height

'''build the AVL tree: 30,20,35,16,22,50,14,23,34,52,21,24'''

'''   
          30
       /     \
     20      35
   /   \    /   \
  16   22  34    50
  /    / \         \
 14   21  23       52
           \
           24
'''   
if __name__ == '__main__':
    avl_tree = AVLTree()

    print('add nodes: 30,20,35,16,22,50,14,23,34,52,21,24')
    avl_tree.add_node(30)
    avl_tree.add_node(20)  
    avl_tree.add_node(35) 
    avl_tree.add_node(16)
    avl_tree.add_node(22)  
    avl_tree.add_node(50)
    avl_tree.add_node(14)
    avl_tree.add_node(23)
    avl_tree.add_node(34)
    avl_tree.add_node(52)
    avl_tree.add_node(21)
    avl_tree.add_node(24) 

    print('find the node 30:')
    tmp = avl_tree.find_node(30)
    print(tmp, tmp.data,'\n')

    print('breadth first traversal:')
    avl_tree.root.breadth_first_traversal(avl_tree.root)

    tmp = avl_tree.root.right_child.left_child
    avl_tree.delete_node(tmp)
    print('\nafter deleting the node 34:')
    print('breadth first traversal:')
    avl_tree.root.breadth_first_traversal(avl_tree.root)
    
    tmp = avl_tree.root
    avl_tree.delete_node(tmp)
    print('\nafter deleting the root node :')
    print('breadth first traversal:')
    avl_tree.root.breadth_first_traversal(avl_tree.root)
    
