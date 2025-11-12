import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(0)

# ⚽ Parte 1 - Gramado (fundo verde)
def gramado():
    tartaruga.penup()
    tartaruga.back(200)  # metade da largura do campo
    tartaruga.left(90)
    tartaruga.back(125)  # metade da altura do campo
    tartaruga.pendown()
    tartaruga.color("green")
    
    for _ in range(2):
        tartaruga.forward(400)
        tartaruga.left(90)
        tartaruga.forward(250)
        tartaruga.left(90)

# ⚽ Parte 2 - Linhas brancas do campo
def linhas_campo():
    tartaruga.penup()
    tartaruga.forward(10)  # pequeno deslocamento para dentro
    tartaruga.left(90)
    tartaruga.forward(10)
    tartaruga.right(90)
    tartaruga.pendown()
    tartaruga.color("white")
    
    for _ in range(2):
        tartaruga.forward(380)
        tartaruga.left(90)
        tartaruga.forward(230)
        tartaruga.left(90)

# ⚽ Parte 3 - Círculo central
def circulo_central():
    tartaruga.penup()
    tartaruga.forward(190)  # metade da largura do campo
    tartaruga.left(90)
    tartaruga.forward(115)  # metade da altura do campo
    tartaruga.pendown()
    tartaruga.color("white")
    
    for _ in range(36):  # 36 lados simulando círculo
        tartaruga.forward(5)
        tartaruga.left(10)
    
    # Volta para a borda inferior
    tartaruga.right(90)
    tartaruga.back(115)
    tartaruga.right(90)
    tartaruga.back(190)
    tartaruga.left(180)

# ⚽ Parte 4 - Traves (retângulos pequenos)
def traves():
    tartaruga.penup()
    tartaruga.back(190)  # canto esquerdo
    tartaruga.left(90)
    tartaruga.forward(95)
    tartaruga.pendown()
    tartaruga.color("white")

    # Trave esquerda
    for _ in range(2):
        tartaruga.forward(40)
        tartaruga.left(90)
        tartaruga.forward(60)
        tartaruga.left(90)

    # Trave direita
    tartaruga.penup()
    tartaruga.forward(360)
    tartaruga.pendown()
    for _ in range(2):
        tartaruga.forward(40)
        tartaruga.left(90)
        tartaruga.forward(60)
        tartaruga.left(90)

# --- Chamada das partes do campo ---
gramado()
linhas_campo()
circulo_central()
traves()

turtle.done()
