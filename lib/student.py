# 1. Write a method in the Student class, hello(), that print()s out the phrase :"Hey there! I'm so excited to learn stuff."

# 2. Write a method in the Student class, raise_hand(), that print()s out the phrase: "Pick me!"

class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print('Pick me!')


# 1. Write a method in the ChattyStudent class, hello(), that uses super() to inherit the behavior of the hello() method from the parent class. Then, augment that method to also print() out the very chatty phrase:
# "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
