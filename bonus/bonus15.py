import json

with open("bonus15.json",'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index,Alternative in enumerate(question["Alternatives"]):
        print(index + 1,":",Alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for question in data:
    if question["Answer"] == question["user_choice"]:
        score = score + 1
        result = "Correct Answer :"
    else:
        result = "Wrong Answer : "
    Message = f"{result} Your Answer is : {question['user_choice']}, Correct Answer is : {question['Answer']}"
    print(Message)
length = len(data)

print(f"Score is {score} / {length} ")
