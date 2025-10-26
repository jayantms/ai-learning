from openai import OpenAI
client = OpenAI()

while True: 
    message = input("User - ")
    messages = []

    if message: 
        messages.append(
            {"role":"user", "content": message}, 
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages = messages
        )

        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role":"assistant", "content": reply})



#text = "Can you suggest good soft rock music albums from 1990 - 2000? " 
#completion = client.chat.completions.create(
#  model="gpt-4.1",
#  messages=[
#    {"role": "system", "content": "You are a kind helpful assistant."},
#    {"role": "user", "content": text}
#  ]
#)
#print(completion.choices[0].message)

