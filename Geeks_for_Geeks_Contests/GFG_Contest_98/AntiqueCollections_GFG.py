from typing import List

# Geeky had developed a deep interest in
# antique items and was determined to
# acquire them all. However, as he started
# visiting different shops, he realized
# that the same antique item was being 
# sold at different prices by different
# vendors. Geeky knew that he had to be 
# smart with his purchases if he wanted 
# to save money and acquire all the 
# different types of antique items in the
# market.
# He created two arrays of size n called
# items[] and prices[]. Each item at index
# i in the items[] array had a corresponding
# price at index i in the prices[] array. 
# Can you help Geeky find his minimum budget
# to get all the different types of antique
# items from the market?

def antiqueItems(n : int, items : List[int], price : List[int]) -> int:
        dic = {}

        def add_to_dict(dic,key, value):
            if key not in dic:
                dic[key] = value
            else:
                if (dic[key] > value):
                    dic[key] = value
        for i in range(n):
            add_to_dict(dic, items[i], price[i])
        return sum(dic.values())

#Example 1:
# Input :
# n=4
# items={1,2,2,3}
# price={3,4,5,6} 

# Output : 
# 13 

# Explanation :
# item 1 is having a price : 3
# item 2 and item 3 is same so we have taken item 
# 2 to have money, hence item 2 having a price : 4 
# item 4 is having a price : 6 
# total price = 3 + 4 + 6 = 13


#Example 2:
# Input : 
# n=1
# items={2}
# price={4}

# Output : 
# 4

# Explanation :
# Only one Item 1 is having  price : 4
# total price is 4


# print(antiqueItems(n, items, price))