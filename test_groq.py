from services.groq_service import ask_groq

answer = ask_groq(
    "Pakistan is facing water shortage. Give 3 water saving suggestions."
)

print(answer)