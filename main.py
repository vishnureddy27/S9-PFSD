class measurment:
    def recangle(self):
        x=int(input("lenght is : "))
        y = int(input("width is : "))
        rp=2*x*y
        ra=x*y
        print("primeter is : ",rp)
        print("area is : ",ra)

    def circle(self):
        r = int(input("circle : "))
        cp=3*r*r
        ca=2*3*r
        print(" perimeter circle : ",cp)
        print(" perimeter circle : ",ca)
    def triangle(self):
        a = int(input("one side : "))
        b = int(input("two side : "))
        c = int(input("third side : "))

        tp=a+b+c
        ta=0.5*b*c
        print(" perimeter triangle : ",tp)
        print(" perimeter triangle : ",ta )

obj=measurment()
obj.recangle()
obj.circle()
obj.triangle()