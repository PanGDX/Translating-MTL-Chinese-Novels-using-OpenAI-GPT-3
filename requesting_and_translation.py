import openai
import os

list_story = []
context = []

full_request = "Rewrite the following story in English. The story is one of"

while True:
	string = input ("Style/Characteristics of the story (adventure, comedy, etc) (type end to stop): ")
	if(string == "end"):
		break
	else:
		additional = f" {string}"
		full_request += additional
full_request+= "\nThe context/background of the story is:\n"

print("Additional information/context:")
while True:
	string = input ()
	if(string == "end"):
		break
	else:
		additional = string
		full_request += additional
		full_request += "\n"
		
full_request+="\n"
full_request+="Start rewriting from this portion:\n"

print("Story input:")
while True:
	string = input ()
	if(string == "end"):
		break
	else:
		additional = string
		full_request += additional
		full_request += "\n"


print(full_request)

openai.api_key = os.getenv("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")
openai.api_key = "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"
response = openai.Completion.create(
	model = "text-davinci-003",
	prompt = full_request,
	temperature = 0.5,
	max_tokens = 50
)

print(response)
'''
After four years, He Yiming finally became a Sect Master, activated the sect system, and received sign-in rewards!

The system summoned the souls of humans from Earth, reshaped their bodies, and made them disciples of the sect!

With that, the sect’s style of operation drastically changed!

Even though they couldn’t even kill the monsters in the novice village head, they just had to do a suicide attack to defeat it. That, and a whole lot of shenanigans as they innovate the world of cultivation!






"Hold the grass, so many people?" Ding Hao and Han Feng were stunned as soon as they entered with the Earth friends.

At the banquet scene, there were more than 3,000 people gathered at this time.

'''
