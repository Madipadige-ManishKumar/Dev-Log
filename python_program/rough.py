import pyttsx3 as pt


def no(s):
    c=1
    for i in range(len(s)):
        if s[i]==" " or s[i]=="\n":
            c+=1
    print(c)


eng=pt.init()
text='''
Hello everyone, welcome to today's video where we dive into the fascinating world of Generative AI. Before we explore Generative AI, let's first understand the broader field of Artificial Intelligence. Artificial Intelligence, or AI, is a scientific discipline focused on creating computers or machines capable of intelligent behavior such as understanding language, analyzing data, making recommendations, and much more. Generative AI is a subset of AI that focuses on creating new content based on patterns learned from large amounts of data. One of the earliest examples is ELIZA, a simple chatbot created by Joseph Weizenbaum using NLP and pattern matching. Generative AI can create various forms of content including text, images, and even audio. Imagine someone who loves reading mystery novels. Over the years, they've read hundreds of books with different detectives and puzzles. When presented with a new mystery, they use their accumulated knowledge and patterns to solve it. Similarly, Generative AI learns from data patterns and applies that knowledge to generate new content or solve problems. Traditional AI focuses on specific tasks like classification and decision-making based on existing data patterns. In contrast, Generative AI is about creativity and innovation, generating new outputs based on given inputs or patterns. Generative AI is widely used today in applications like ChatGPT for conversational AI, DALL-E for generating images, and in fields such as healthcare for diagnostics, personalized medicine, finance for fraud detection, education, entertainment, and more. If you're interested in learning more about Generative AI, there are great resources available for free. For instance, you can explore courses like "Generative AI by FreeCodeCamp," which covers Generative AI and LLM in-depth over 30 hours. Another excellent option is "Generative AI for Beginners" on Coursera by Andrew Ng, a comprehensive 3-week course. That wraps up today's video on Generative AI. I hope you found this introduction insightful. Stay tuned for our next video where we'll explore another intriguing topic. Until then, take care and happy learning!
'''
no(text)
eng.save_to_file(text,"output1.wav")
eng.runAndWait()

