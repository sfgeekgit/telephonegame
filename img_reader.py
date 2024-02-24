from openai import OpenAI
import base64
import random
client = OpenAI()

# Define your image filenames here
image1_filename = "./imgs/tele11.jpg"
image2_filename = "./imgs/tele12.jpg"




def encode_image(image_path):
    while True:
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except IOError as e:
            if e.errno != errno.EACCES:
                # Not a "file in use" error, re-raise
                raise
            # File is being written to, wait a bit and retry
            time.sleep(0.1)
  

base64_image_1 = encode_image(image1_filename)
#base64_image_2 = encode_image(image2_filename)


players = ["David Attenborough",  "Doctor Who", "Mister T", "Yoda", "Sigourney Weaver", "Stephen King", "Shakespear"]

rand_player = random.choice(players)
print(f"{rand_player=}")
##sys_prompt = f"You are {rand_player}. Narrate any pictures as if in a nature documentary. Make it short, try to reply in 20 words or less."

sys_prompt = f'''
You are {rand_player}. Please describe any image you see in your own style. 
Your description should be short, keep the facts to 5-10 words, 
then add a sentence of your own opinion or style.
'''





response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
        "role": "system",
        "content": sys_prompt,
    },      


    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Please describe this image in 10 words or less.",
        },
        {
          "type": "image_url",
          "image_url": f"data:image/jpeg;base64,{base64_image_1}",
        },
        '''        
        {
          "type": "image_url",
          "image_url": f"data:image/jpeg;base64,{base64_image_2}",
        },
        '''
      ],
    }
  ],
  max_tokens=300,
)

# print(f"{response=}")


print(response.choices[0])



