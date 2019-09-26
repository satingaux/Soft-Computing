#!/usr/bin/env python
# coding: utf-8

# In[22]:


class MP:
    threshold=0
    w1=0
    w2=0
    possible_w1=[-1,1]
    possible_w2=[-1,1]
    possible_threshold=[-2,-1,1,2]
    
    def __init__(self, inputmatrix):
        self.input_matrix=inputmatrix
        
    def iterate_all(self):
        for w1 in self.possible_w1:
            self.w1=w1
            for w2 in self.possible_w2:
                self.w2=w2
                for threshold in self.possible_threshold:
                    self.threshold=threshold
                    if self.check_combination():
                        return True
        return False
    
    def check_combination(self):
        valid=True
        for (x1,x2,y) in self.input_matrix:
            if not self.compare_target(x1,x2,y):
                valid=False
        return valid
    
    def compare_target(self, x1,x2,target):
        if self.neuron_activate(x1,x2)==target:
            print("&&&&&&&&&& neuron is activated")
            print("x1={}   x2={}   target={}".format(x1,x2, target))
            print("w1={}   w2={}   threashold={}".format(self.w1,self.w2, self.threshold))
            return True
        print("&&&&&&&&&& neuron is not activated")
        print("x1={}   x2={}   target={}".format(x1,x2, target))
        print("w1={}   w2={}   threashold={}".format(self.w1,self.w2, self.threshold))
        return False
    
    def neuron_activate(self, x1,x2):
        output=self.w1*x1+self.w2*x2
        if output>=self.threshold:
            return 1
        return 0
    
    
    
    ##########################################################################################################
if __name__=="__main__":

    AND_Matrix = [
        [-1, -1, 0],
        [-1,  1, 0],
        [ 1, -1, 0],
        [ 1,  1, 1],
    ]

    OR_Matrix = [
        [-1, -1, 0],
        [-1,  1, 1],
        [ 1, -1, 1],
        [ 1,  1, 1],
    ]

    NAND_Matrix = [
        [-1, -1, 1],
        [-1,  1, 1],
        [ 1, -1, 1],
        [ 1,  1, 0],
    ]

    XOR_Matrix = [
        [-1, -1, 0],
        [-1,  1, 1],
        [ 1, -1, 1],
        [ 1,  1, 0],
    ]


    def neuron_calculate(mp):
        if mp.iterate_all():
            print("Weights are : {}, {}".format(mp.w1, mp.w2))
            print("Threshold is {}".format(mp.threshold))
        else:
            print("Not linearly separable.")
        print()

#     print("++ AND Gate ++")
#     mp_AND = MP(AND_Matrix)
#     neuron_calculate(mp_AND)

#     print("++ OR Gate ++")
#     mp_OR = MP(OR_Matrix)
#     neuron_calculate(mp_OR)

#     print("++ NAND Gate ++")
#     mp_NAND = MP(NAND_Matrix)
#     neuron_calculate(mp_NAND)

    print("++ XOR Gate ++")
    mp_XOR = MP(XOR_Matrix)
    neuron_calculate(mp_XOR)
                


# In[ ]:




