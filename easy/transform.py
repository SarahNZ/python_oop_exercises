'''
Write a class such that the following code prints the results indicated 
by the comments:
'''

class Transform():

    def __init__(self, text):
        self._text = text

    def uppercase(self):
        return self._text.upper()
    
    @staticmethod
    def lowercase(text):
        return text.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz