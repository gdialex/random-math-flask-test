from random import randint, shuffle

def index_continue(score):
    x = randint(2,9)
    y = randint(2,9)
    z = x*y
    L = [z,randint(10,81),randint(10,81),randint(10,81)]
    shuffle(L)
    return (
                f'<p>{x}*{y}=?</p>'
                f'<a href=/{score + 1 * (L[0]==z)}>{L[0]}</a><br>'
                f'<a href=/{score + 1 * (L[1]==z)}>{L[1]}</a><br>'
                f'<a href=/{score + 1 * (L[2]==z)}>{L[2]}</a><br>'
                f'<a href=/{score + 1 * (L[3]==z)}>{L[3]}</a><br>'
    )

print(index_continue(10))