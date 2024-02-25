from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

print(f"{response=}")


image_url = response.data[0].url
print(f"{image_url=}")


# save the image to a file
'''
image_filename = "output.jpg"
with open(image_filename, "wb") as f:
    f.write(requests.get(image_url).content)
'''
# display the image
from PIL import Image
import requests
from io import BytesIO

#response = requests.get(image_url)
response = image_url
img = Image.open(BytesIO(response.content))
img.show()
#img.save("output.jpg")



