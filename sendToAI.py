from PIL import Image
def sendToAI(model,canvas,fingers):
    if fingers ==[1,1,1,1,0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve the math problem", pil_image])
        #response = model.generate_content("Write a story about a AI and magic")
        return response.text