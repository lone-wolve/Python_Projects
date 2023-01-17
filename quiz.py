quiz = {

    "question 1":{

        "question" : "What is the capital of The Gambia",
        "answer": "Banjul"

    },

    "question 2":{

        "question" : "What is the capital of Senegal",
        "answer": "Dakar"

    },

    "Question 3":{

        "question" : "What is the capital of Nigeria",
        "answer": "Abuja"

    },

    "Question 4":{

        "question" : "What is the capital of China",
        "answer": "Beijing"

    },

    "Question 5":{

        "question" : "What is the capital of Portugal",
        "answer": "Lisbon"

    },

    "Question 6":{
    
        "question" : "What is the capital of Rwanda   ",
        "answer": "Kigali"

    },

}

score = 0
print("Welcome to Geograpy quiz\t\t ")
print("*" * 10)
for key, value in quiz.items():
    print(value["question"], " ")
    answer = input(" Answer --> ")

    if answer.lower() == value["answer"].lower():
        print("correct")
        score = score + 1
        print (f"your score is : {str(score)}\n ")

    else:

        print("your answer is wrong")
        print(f"the answer is {value['answer']}")
        print(f"your score is : {str(score)}\n")

print( f"you got {str(score)} out of 6")
print( f"you percentage is {str(int(score/6* 100))}%")
