print("파이썬")

import streamlit as st

import turtle
t = turtle. Turtle()
t.shape('turtle')
t.speed(0)
t.width(2)
lenght = 5

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for i in range(100):
    t.fd(lenght)
    t.pencolor(colors[length%7])
    t.right(45)

    lenght += 5



    





turtle.done()











#s = 41

#if s>=90:
 #    st.write('귀하의 점수는' +str(s) + '점으로 :blue[A등급]입니다')        
#elif s >=80:
  #   ('귀하의 점수는' +str(s) + '점으로 :green[B등급]입니다')        
#elif s >=60:
 #    ('귀하의 점수는' +str(s) + '점으로 :orange[C등급]입니다')        
#elif s >=50:
#     ('귀하의 점수는' +str(s) + '점으로 :black[D등급]입니다')        
#elif s >=40:
#     ('귀하의 점수는' +str(s) + '점으로 :red[F등급]입니다')        



t = turtle.Turtle()
t.shape('turtle')

# t.speed(10)


# t.left(60)
# t.fd(size)
# t.right(120)
# t.fd(60)

# t.right(30)
# t.fd(60)
# t.right(90)
# t.fd(60)
# t.right(90)
# t.fd(60)
# t.right(90)
# t.fd(60)




# turtle.bgcolor("black")
# t.speed(0)
# t.width



# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.shape("turtle")


turtle.done()






st.write("스플림릿")
st.title("streamlit image")
st.image("im.jfif")
