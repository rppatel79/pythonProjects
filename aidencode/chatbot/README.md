#What does this project do?
A python implementation of a chatbot.  This code was minimic from a [huggingface](https://huggingface.co/microsoft/DialoGPT-large/blame/main/README.md) repo.


#Dependencies
##How do add a dependency?
>pip3 install flask</br>
>pip freeze > requirements.txt </br>
>git commit push requirements.txt`

#Run
##How to setup dependencies?
cd pythonProjects/aidencode/chatbot
source chatbot-env/bin/activate
python -m pip install -r requirements.txt

##Run the flask container
cd pythonProjects/aidencode/chatbot
source chatbot-env/bin/activate
python3 myFlaskedBot.py