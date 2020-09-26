from datetime import date

#組合的簡易作法
class Employee: #公司員工
    def __init__(self, *title):
        self.title = title
        
class Meeting: #會議
    def __init__(self, topic, tday):
        self.topic = topic
        self.today = tday
        print('開會日期：', self.today)
        print('開會地點：', self.topic)
        
class Company: #公司
    def __init__(self, Employee, Meeting):
        self.Employee = Employee
        self.Meeting = Meeting

    def show(self):
        print('參與會議人員:', self.Employee.title)

tday = date.today()#取得今天日期
#Employee物件
member = Employee('研發部主管','會計部主管','業務部主管','行銷部主管')
place = Meeting('公司總部805會議室', tday)#開會地點
obj = Company(member, place)#Company實體
obj.show()#呼叫方法
