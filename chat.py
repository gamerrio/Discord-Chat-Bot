from pyllamacpp.model import Model

def new_text_callback(text: str):
    print(text, end="", flush=True)

model = Model(ggml_model='./gpt4all-converted.bin', n_ctx=512)
text = model.generate("what is capital of delhi ", n_predict=128, new_text_callback=new_text_callback, n_threads=8)
print(text)