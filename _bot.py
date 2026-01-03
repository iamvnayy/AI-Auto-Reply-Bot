import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="<Your Key Here>",
)

def last_message_from_sender(whatsapp_chat_text, sender_name="Rohan 2nd"):
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

pyautogui.click(1040, 1050)
time.sleep(1)

while True:
 pyautogui.moveTo(699,186)
 pyautogui.dragTo(1107,931,duration=1.0,button='left')
 pyautogui.hotkey('ctrl','c')
 time.sleep(2)
 
  pyautogui.click(913,795)
 
  chat_history = pyperclip.paste()
  print(chat_history)
  print(is_last_message_from_sender(chat_history))
  if is_last_message_from_sender(chat_history):
     completion = client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
          {"role": "system", "content": "You are a person named Vinay who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
          {"role": "system", "content": "Do not start like this [21:02, 12/6/2025] Rohan 2nd: "},
          {"role": "user", "content": chat_history}
      ]
   )
    response = completion.choices[0].message.content
    
    pyperclip.copy(response)
    pyautogui.click(885, 965)
    time.sleep(1)  
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')


