import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'Explain what you see in the image?',
        'images': ['test_image.jpg']
    }]
)

print(response)
