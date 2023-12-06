import datetime
import webbrowser
import speech_recognition as sr
import win32com.client
import os
import openai
from config import apikey


speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatstr = ""


def chat(query):
    global chatstr
    chatstr = f"Shiv:{query}\nJarvis:"
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatstr += "f{response['choices'][0]['text']}\n"
    print(chatstr)
    say(response['choices'][0]['text'])
    return (response["choices"][0]["text"])


def ai(prompt):
    openai.api_key = os.getenv(apikey)

    text = f"Openai response for prompt:{prompt}\n**********************\n\n"
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(
        f"Openai/{''.join(prompt.split('intelligence')[1:].strip())}.txt",
        "w") as f: f.write(text)


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognising.....")
            query = r.recognize_google(audio,
                                       language="en-in")
            print(f"User said:{query}")
            return query

        except Exception as e:
            return "Some Error occurred. Sorry from Jarvis"


while 1:
    print("Listening....")
    query = takeCommand()
    say(query)

    sites = [["youtube", "https://youtube.com"],
             ["google", "https://google.com"],
             ["wikipedia", "https://wikipedia.com"],
             ["Zoro", "https://zorotv.com"],
             ["hd1", "https://hd1.to"], ]
    musics = [["Arms around you",
               "C:/A-xe-12/shiv/BRAND/XXXTENTACION & Lil Pump - Arms Around You feat. Maluma & Swae Lee [Official Music Video].mp3"],
              ["Way down we go",
               "C:/A-xe-12/shiv/BRAND/KALEO-Way-Down-We-Go-Official-Music-Video_0-7IHOXkiV8.mp3"]]
    for site in sites:
        if site[0].lower() in query.lower():
            say(f"Opening {site[0]}")
            webbrowser.open(site[1])

    if "open music".lower() in query.lower():

        for music in musics:
            if music[0].lower() in query.lower():
                os.startfile(music[1])

    elif "the time" in query.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir the time is {time}")
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    elif "Using artificial intelligence".lower() in query:
        ai(prompt=query)

    elif "Stop Listening".lower() in query.lower():
        say("Ok sir. I have stopped listening. In case you need me you know where to find me. Jarvis out")
        exit()

    elif "reset chat".lower() in query.lower():
        chatstr = ""

    # else:
    #     print("Chatting.....\n")
    #     chat(query)
