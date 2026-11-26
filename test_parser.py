
from utils.resume_parser import parse_resume

file_path = "D:/edufly/AI_Resume_Screening/ManiKumar_InternshalaResume (1).pdf"

try:

    resume_text = parse_resume(file_path)

    print("\n----- EXTRACTED RESUME TEXT -----\n")

    print(resume_text)

except Exception as e:

    print("Error:", e)
