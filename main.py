import eel

eel.init('genai-app')  # Thư mục chứa HTML/JS

@eel.expose
def say_hello(name):
    print(f"Hello from Python, {name}!")

eel.start('index.html', size=(600, 400))