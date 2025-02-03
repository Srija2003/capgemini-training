class Customers:
    def __init__(self,c_id,first_name,last_name,phone,email,street,city,state,zip_code):
        
        self.c_id = c_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone =phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
        
        
    def display(self):
        print(f" customer id is : {self.c_id} \n First name is : {self.first_name} \n Lasst name is : {self.last_name} \n Phone no is : {self.phone} \n Email is {self.email} \n Street is {self.street} \n City is {self.city} \n state is {self .state} \n Zip_code is {self.zip_code} ")
    
class Orders():
    def __init__(self,o_id,c_id,O_status,o_date,required_date,shipped_date,store_id,staff_id):
        self.o_id=o_id
        self.c_id=c_id
        self.o_status=O_status
        self.o_date=o_date
        self.required_date=required_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id
        
    def displa(self):
        print (f" order id:{self.o_id}\n customer_id: {self.c_id}\n order_status: {self.o_status} \n order_date:{self.o_date} \n required date:{self.required_date} \n shipped date:{self.shipped_date} \n store id:{self.store_id} \n staff id:{self.staff_id}")

class Order_items:
    def __init__(self,order_id,item_id,product_id,quantity,list_price,discount):
        self.order_id=order_id
        self.item_id=item_id
        self.product_id=product_id
        self.quantity=quantity
        self.list_price=list_price
        self.discount=discount
        
    def displ(self):
        return"\n order_id :{self.order_id}\n item_id:{self.item_id}\n product_id:{self.product_id}\n quantity :{self.quantity}\n list_price:{self.list_price}\n discount:{self.discount}"
         
        
obj = Customers(101,"srija","sri",987654321,"abc@gmail.com","Ramalayam street","hyd","Ts",500075)
obj.display()
obj1 = Orders(202,101,"Received","29-01-2025","2-2-2025","4-02-2025",44567,102030)
obj1.displa()
obj1=Order_items(100,1,2,'3 units',4500,'32%')
obj1.displ()
