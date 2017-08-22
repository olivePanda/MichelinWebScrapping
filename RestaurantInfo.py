# -*- coding: cp949 -*-

maker = 'bjune.jeong'

class RestaurantInfo :    
    category = ''
    title = ''
    image = ''
    grade = ''
    addr = ''
    phone = ''
    homepage = ''
    
##    def __init__(self) :

    def printInfo(self) :
        print 'category :', self.category
        print 'title :', self.title
        print 'image :', self.imgUrl
        print 'grade :', self.grade
        print 'addr :', self.addr
        print 'phone :', self.phone
        print 'homepage :', self.homepage
        print '\n'


# Test Code
if __name__ == '__main__':
    print 'Test code from here'
    print maker
    
