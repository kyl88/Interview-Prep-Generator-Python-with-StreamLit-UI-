from  langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_interview_questions():
   llm = openai(temperature = 0.7)

   prompt_template_name = PromptTemplate(
      
      input_variables=['interview_question'],
      template="Suggest a possible interview questions for data analytics."
   )

   name_chain = LLMChain(llm=llm,prompt =  prompt_template_name)

   return name_chain

if __name__ == "_main_":
   print(generate_interview_questions())  