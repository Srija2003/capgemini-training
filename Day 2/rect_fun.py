def display(data):
    print(f"the area is {data}")
    
def get_input():
    len = input("length:")
    wid = input("width:")
    return (len, wid)

def compute_area(len, wid):
    area=int(len) * int(wid)
    return area
    
def main():
    (len, wid) = get_input()
    area=compute_area(len,wid)
    display(area)
    
main()