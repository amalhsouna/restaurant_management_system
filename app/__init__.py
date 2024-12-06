from dotenv import load_dotenv
import os

print("TESTING value:", os.getenv("TESTING"))

if os.getenv("TESTING", "false").lower() == "true":
    load_dotenv(".env_test")
else:
    load_dotenv()
