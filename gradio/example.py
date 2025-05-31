import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"], # should match the number of arguments in the function
    outputs=["text"], # should match the return value of the function
)
demo.launch(server_name="127.0.0.1", server_port=7860, pwa=True)
