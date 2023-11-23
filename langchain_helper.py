from  langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_interview_questions(interview_question):
   llm = openai(temperature = 0.7)

   prompt_template_name = PromptTemplate(
      
      input_variables=['interview_question'],
      template="Suggest a possible {interview_question} for data analytics."
   )

   name_chain = LLMChain(llm=llm,prompt =  prompt_template_name)
   
   response = name_chain({'interview_question':interview_question })
   return response

if __name__ == "_main_":
   print(generate_interview_questions("Tell me more about yourself"))  