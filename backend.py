import records

class DigitalDJBackend():
    def __init__(self):
        self.db=records.Database('sqlite:///test.db',connect_args={'check_same_thread': False})
        try:
            self.createtesttable()
        except Exception as e:
            print(e)
            print("table exists already")
    def createtesttable(self):
        query="create table test(user text, todo text, category text,completed text default 0)"
        self.db.query(query)
        
        # rows=self.db.query("select * from test")
        # print(rows)
    def selecttestdata(self):
        query="select * from test"
        return self.db.query(query).all(as_dict=True)
    def inserttestdata(self,user,todo,category,completed):
        print("User: {} TODO: {} Category: {} Completed {}".format(user,todo,category,completed))
        query="insert into test(user,todo,category,completed) values(:user,:todo, :category,:completed)"
        self.db.query(query,user=user,todo=todo,category=category,completed=completed)
        
        