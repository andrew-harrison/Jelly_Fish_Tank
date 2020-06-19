from Jelly import jelly

prevTime = 0
animTime = 0.0
width = 800
height = 600

def MakeJelly():

    x_pos = random(20, width - 20)
    y_pos = random(0, height / 2) + height
    # random(0.1,1.5)
    scale_val = constrain(randomGaussian() / 2 + 0.5, 0.1, 1.2)
    speed = constrain(randomGaussian() + 1, 0.5, 3)

    return jelly(120, 0, x_pos, y_pos, scale_val, speed)


def setup():
    global tank

    frameRate(30)
    size(width, height)
    textSize(20)

    names = ["bob", "fred", "harry", "trish", "Jim", "Judy",
             "Frank", "Geraldine", "Snoop", "Dingo", "Gertrude"]
    tank = {}
    for fish in names:
        tank[fish] = MakeJelly()

def draw():
    global prevTime, animTime, tank
    background(252, 236, 194)
    time = millis()
    delta = time - prevTime
    animTime += delta/2
    prevTime = time
    print(frameRate)

    for fish in tank:
        pushMatrix()

        tf = tank[fish]
        tf.phi = animTime / 1000

        if tf.dir > PI:
            tf.dir -= 2 * PI

        tf.dir = tf.dir - 0.1 * \
            (tf.dir + 3 * (noise(tf.x_pos, tf.y_pos) - 0.5))

        if tf.dir < 0:
            tf.dir += 2 * PI

        tf.DrawCroissant()

        popMatrix()

        if tf.y_pos < -2 * tf.r:
            # tank[fish] = None
            tank[fish] = MakeJelly()
            print("Hooray, " + str(fish) + " has just been born!")

    saveFrame("output/frame_####.png")
