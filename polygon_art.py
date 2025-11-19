import turtle
import random

class ArtGenerator:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        
    # เพิ่ม self เป็นอาร์กิวเมนต์ (สำคัญ)
    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    # เพิ่ม self เป็นอาร์กิวเมนต์ (สำคัญ)
    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def art1(self):
        num_sides = random.randint(3, 5) # triangle, square, or pentagon
        size = random.randint(80, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-250, 250), random.randint(-180, 180)]
        color = self.get_new_color()
        border_size = random.randint(2, 6)
        
        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
        
        reduction_ratio = 0.618  
        
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        
        location[0] = turtle.xcor()
        location[1] = turtle.ycor()

        # adjust the size according to the reduction ratio
        size *= reduction_ratio

        # draw the second polygon embedded inside the original 
        self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        turtle.update()
        
    def art2(self):
        for _ in range(30):
            x = random.randint(-300, 300)
            y = random.randint(-250, 250)
            self.draw_polygon(5, random.randint(20, 60), random.randint(0,360),
                              [x, y], self.get_new_color(), 2)
        turtle.update()
        
    def art3(self):
        for r in range(150, 10, -10):
            turtle.penup()
            turtle.goto(0, -r)
            turtle.pendown()
            turtle.color(self.get_new_color())
            turtle.pensize(3)
            turtle.circle(r)
        turtle.update()
        
    def art4(self):
        for angle in range(0, 360, 20):
            loc = [0,0]
            self.draw_polygon(6, 120, angle, loc, self.get_new_color(), 3)
        turtle.update()
        
    def art5(self):
        size = 10
        for i in range(50):
            color = self.get_new_color()
            turtle.pencolor(color)
            turtle.pensize(3)
            turtle.forward(size)
            turtle.left(20)
            size += 5
        turtle.update()
        
    def art6(self):
        for _ in range(70):
            x = random.randint(-300, 300)
            y = random.randint(-250, 250)
            side = random.randint(20, 60)
            self.draw_polygon(4, side, 0, [x,y], self.get_new_color(), 2)
        turtle.update()
    
    def art7(self):
        for angle in range(0, 360, 10):
            turtle.penup()
            turtle.goto(0, 0)
            turtle.setheading(angle)
            turtle.pendown()
            turtle.color(self.get_new_color())
            turtle.forward(300)
        turtle.update()
        
    def art8(self, size=100, depth=6):
        if depth == 0:
            return
        turtle.pensize(2)
        turtle.pencolor(self.get_new_color())
        turtle.forward(size)
        turtle.left(25)
        self.art8(size*0.7, depth-1)
        turtle.right(50)
        self.art8(size*0.7, depth-1)
        turtle.left(25)
        turtle.backward(size)
        
    def art9(self):
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        for _ in range(300):
            turtle.pencolor(self.get_new_color())
            turtle.pensize(random.randint(1,5))
            turtle.setheading(random.randint(0,360))
            turtle.forward(random.randint(10, 40))
        turtle.update()

def main():
    art = ArtGenerator()

    # ป้องกันกรณีผู้ใช้พิมพ์ค่าไม่ใช่ตัวเลข
    try:
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
    except ValueError:
        print("Please enter a valid integer between 1 and 9.")
        return

    if choice == 1:
        art.art1()
    elif choice == 2:
        art.art2()
    elif choice == 3:
        art.art3()
    elif choice == 4:
        art.art4()
    elif choice == 5:
        art.art5()
    elif choice == 6:
        art.art6()
    elif choice == 7:
        art.art7()
    elif choice == 8:
        turtle.left(90)
        art.art8()
        turtle.update()
    elif choice == 9:
        art.art9()
    else:
        print("Invalid option!")

    turtle.done()


if __name__ == "__main__":
    main()