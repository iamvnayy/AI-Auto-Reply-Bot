from openai import OpenAI
client = OpenAI(
  api_key="<Your Key Here>",
)
command = '''
[20:30, 29/12/2025] Vinay: jo sunke coding ho sake?
[20:30, 29/12/2025] Rohan 2nd: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 29/12/2025] Rohan 2nd: ye
[20:30, 29/12/2025] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 29/12/2025] Vinay: This is hindi
[20:31, 29/12/2025] Vinay: send me some english songs
[20:31, 29/12/2025] Vinay: but wait
[20:31, 29/12/2025] Vinay: this song is amazing
[20:31, 29/12/2025] Vinay: so I will stick to it
[20:31, 29/12/2025] Vinay: send me some english song also
[20:31, 29/12/2025] Rohan 2nd: hold on
[20:31, 29/12/2025] Vinay: I know what you are about to send
[20:32, 29/12/2025] Vinay: 😂😂
[20:32, 29/12/2025] Rohan 2nd: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 29/12/2025] Vinay: okok
[20:33, 29/12/2025] Rohan 2nd: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Vinay who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Vinay"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)

