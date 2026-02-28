from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# CRUX -- TypedDict is just for representational static type checking not for data validation


class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg", "neu"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

# before calling the invoke function we call the with_structured_output()

model = ChatOpenAI()

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" 
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
""")

print()
print("Result::::", result['summary'])






"""
TOPIC: Runtime Inheritance (OOP) vs TypedDict (Typing Only)

KEY IDEA:
- Normal classes affect runtime behavior (methods, attributes).
- TypedDict affects ONLY type checking, not runtime behavior.
"""

# -------------------------------
# 1. REAL CLASS (Runtime behavior)
# -------------------------------

class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):  # runtime inheritance
    pass


dog = Dog()

print(dog.speak())          # ✅ inherited method works
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(type(dog))            # <class '__main__.Dog'>


# ---------------------------------
# 2. TYPEDDICT (Typing-only concept)
# ---------------------------------

# from typing import TypedDict


class User(TypedDict):
    id: int
    name: str


class AdminUser(User):  # NOT runtime inheritance
    role: str


admin = {
    "id": 1,
    "name": "Jatin",
    "role": "admin"
}

print(type(admin))          # <class 'dict'>
print(admin["role"])        # ✅ works (dict access)

# ❌ DOES NOT WORK (no runtime class behavior)
# admin.role
# isinstance(admin, AdminUser)


# ---------------------------------
# 3. WHY THEY ARE DIFFERENT
# ---------------------------------

"""
Animal/Dog:
- Exists at runtime
- Can be instantiated
- Has methods
- Inheritance shares behavior

TypedDict:
- Exists only for type checkers
- Cannot be instantiated
- No methods or attributes
- "Inheritance" shares structure only
"""


# ---------------------------------
# ONE-LINE RULE (REMEMBER THIS)
# ---------------------------------

"""
Runtime class inheritance = behavior sharing
TypedDict inheritance = shape sharing
"""
