import pymongo
import json
class DatabaseManagementSystem:
    """
    数据库的增删改查系统
    """

    def __init__(self,your_mongodb_ip=None):
        print('正在准备环境...')
        self.client = pymongo.MongoClient(your_mongodb_ip)

    def _check_all_database(self):
        print('=====您的数据库里面的所有集合=====')
        for i in self.client.list_database_names():
            print('数据库：',i)
            print('集合：')
            for j in self.client[i].list_collection_names():
                print('\t',j)
            print('\n')

    def _add_new_data(self,db,collection):
        c = self.client[db][collection]
        print(f'\t\t已进入{db}中的集合{collection}...')
        judge = True
        while judge:
            data = input('添加数据，以字典形式传入:')
            try:
                c.insert_one(data)
            except:
                print("插入数据格式不对，示例：{'age':18}")
            else:
                print('添加成功！')
                judge = False

    def _search_data(self,db,collection):
        c = self.client[db][collection]
        print(f'数据库{db}中的集合{collection}里的数据如下：')
        for i in c.find():
            print(i)

        try:
            rule = json.loads(input('输入查询条件（示例{"sex":"男"}或{"age":{"$gt":18}}）：'))
        except:
            print("插入查询格式不对")
        else:
            data = c.find(rule)
            if data:
                for i in data:
                    print(i)
            else:
                print('数据为空')
    def _delete_data(self, db, collection):

        try:
            rule = json.loads(input('输入删除数据（示例{"sex":"男"}）：'))
        except:
            print("插入删除格式不对")
        else:
            self.client[db][collection].delete_many(rule)

    def main(self):
        while True:
            print("1. 查看所有数据库")
            print("2. 添加新数据")
            print("3. 查询数据")
            print("4. 删除数据")
            print("0. 退出系统")

            choice = input('请输入编号:').strip()
            if choice == '1':
                self._check_all_database()
            elif choice == '2':
                print('*请指定添加位置*')
                db = input('数据库：')
                collection = input('集合：')
                self._add_new_data(db,collection)
            elif choice == '3':
                print('*请指定查询位置*')
                db = input('数据库：')
                collection = input('集合：')
                self._search_data(db, collection)

            elif choice == '4':
                print('*请指定位置*')
                db = input('数据库：')
                collection = input('集合：')
                self._delete_data(db, collection)
            elif choice == '0':
                break

            else:
                print('无效输入，请重新填写编号')
    def __del__(self):
        print('========已退出系统=========')


a = DatabaseManagementSystem(your_mongodb_ip='mongodb://127.0.0.1:27017/')
a.main()











