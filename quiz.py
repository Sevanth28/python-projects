quiz={
    "What is the present year ?":"2025",
    "What colour is the sun rays ?":"White",
    "Which is the smallest planet ?":"Mercury",
    "Which galaxy do we leave in ?":"Milkyway galaxy",
    "Which is the first man-made thing to cross the solar-system ?":"Voyger 1"
}
s=0
for i,q in quiz.items():
    print(f"{i}")
    ans=input("Answer :")
    if(ans.strip().capitalize()==q):
        print(f"Correct")
        s+=1
    else:
        print(f"Wrong answer the correct answer is {q}")
print(f"The final score is {s}")