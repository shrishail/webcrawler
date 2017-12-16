import psycopg2

class DB(object):
    def __init__(self):
        self.conn = psycopg2.connect(host='127.0.0.1', database='tfa',
                                     user='postgres', password='Shri@291536')
        self.cursor = self.conn.cursor()

    #getsources
    def get_sources(self):
        query = "select url, category from sources"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_news(self, newsitems, category):
        for item in newsitems:
            try:
                query = "insert into news(title, description, post_link, " \
                        "category) " \
                        "values(%s, %s, %s, %s)"

                self.cursor.execute(query, (item['title'], item['description'],
                                          item['link'], category))
                self.conn.commit()
            except Exception as e:
                print(str(e))

    #def read_news_limit(self, num):
    def read_news(self):
        #query = "select * from news order where category ='top' {}".format(num)
        #query = "select * from news where category ='top'"
        query = "select * from news where category in ('top','ent')"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def filter(self,category, limit):
        query = "select * from news where category = %s order by id desc limit %s"
        self.cursor.execute(query,(category,limit))
        return self.cursor.fetchall()
    def urlaggregate(self,category, url):
        query = "insert into sources(category, url)values(%s,%s)"
        self.cursor.execute(query,(category,url))
        self.conn.commit()
        return self.cursor.fetchall()
#objectDB = DB()
#print(objectDB.read_news())

    #read news items
    #filter news items
    #insert news item
if __name__=='__main__':
    #print("1.Top stories\n","2.Filter by category and limit\n","3.Aggregate")
    print("1.Top stories\n 2.Filter by category and limit\n 3.Aggregate\n")
    choice= int(input("choose your option:"))
    if (choice == 1):
        objectDB = DB()
        for title in objectDB.read_news():
            print(title)
    if choice==2:
        category = input("enter category:")
        limit = input("enter limit:")
        objectDB = DB()
        print(objectDB.filter(category,limit))
    if choice==3:
        category = input("enter category:")
        url = input("enter url:")
        objectDB = DB()
        print(objectDB.urlaggregate(category,url))
    

        
        
    
