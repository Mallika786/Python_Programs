import win32com.client

l = []
while True:
  nm=input('Enter the names:')
  if nm=='quit':
    break
  else:
    l.append(nm)
sp = win32com.client.Dispatch("SAPI.SpVoice")

for i in l:
  sp.Speak(f"Hello {i}")

