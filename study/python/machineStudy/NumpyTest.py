
import numpy as np


def test():
    lst = [1,2,3,4,5,6]
    print(type(lst))
    np_lst = np.array(lst)
    #print(type(np_lst))
    #np_lst = np.array(lst,dtype=float)
    #print(np_lst)
    #print(np_lst.reshape((3,-1)))#shape 将np_lst分成3行2列或者使用 np_list.reshape((3,2))
    #print(np_lst.ndim)  #数组的维度
    #print(np_lst.dtype) #元素的类型
    #print(np_lst.itemsize) #每个元素占多少内存
    #print(np_lst.size) #数组元素个数
    # arrays
    #print(np.zeros([3,5])) #用0填充3*5的数组
    #print(np.ones((3,5)))  #用1填充3*5的数组
    #print(np.full((3,5),5)) #用5填充3*5的数组
    #print(np.eye(5,5,dtype=int)) #创建5*5的数组，[0,0],[1,1],[2,2],[3,3],[4,4] 为1，其他的为0
    #print(np.random.rand(2,4))#生成随机数，2*4的数据 生成[0,1)
    #print(np.random.randint(1,10,3))#随机生成3个[1,10)的整数
    #print(np.random.randn(2,4))#生成一个正态分布2*4
    #print(np.random.choice([1,5,7]))#从1，5，7中随机取得一个数
    #print(np.random.beta(1,10,100)) #beta分布
    #index
    #a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    #print(a[-2:,1:3])
    #print(np.arange(1,11).reshape(2,-1))
    lst = np.arange(1,11).reshape(2,-1)
    #print(np.exp(lst))
    #print(np.exp2(lst))
    #print(np.sqrt(lst))
    #print(np.sin(lst))
    #print(np.log(lst))

if __name__ == '__main__':
    test()


