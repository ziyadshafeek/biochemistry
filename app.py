import gradio as gr
pip install cohere
import cohere

# Initialize the Cohere client
co = cohere.Client('mTeiGiDIpi4R7perkfRnMnCmi5jJzM8QziDVPrG8')  # Replace with your api_key

def generate_response(prompt):
    output = co.generate(model='9b2e329d-7542-4c44-8f8c-cac03a6c4f5a-ft', prompt=prompt)
    response = output.generations[0].text
    return response

iface = gr.Interface(fn=generate_response, 
                     inputs="text", 
                     outputs="text",
                     title='Cohere Text Generation',
                     description='Enter your prompt to generate text')

iface.launch(share=True)

