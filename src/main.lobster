import gui

let WIDTH = 400
let HEIGHT = 400

fatal(gl.window("Lobster WASM demo", WIDTH, HEIGHT))

check(gl.set_font_name("data/fonts/Inconsolata/Inconsolata-Regular.ttf"), "font!")

let FONT_SIZE = 30


def render_text_lines(lines: [string]):
    for(lines) line, i:
        gl.translate(float2 {0.0, float(i * FONT_SIZE)}):
            gl.text(line)


let text_lines = [
    "Press space to change ",
    "background to yellow. "
]

gl.set_font_size(FONT_SIZE)


while gl.frame():
    let space_down, _ = gl.button("space")

    gl.clear(color_black)
    gl.color(color_white)
    
    if space_down:
        gl.clear(color_yellow)
        gl.color(color_black)

        gl.text("Space held for {space_down} frames.")
    
    else:
        render_text_lines(text_lines)
    