# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_names(animal_type,pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template = "I have a {animal_type} pet and i want a cool name for it .and it is {pet_color} in color .suggest me five cool names for my pet."
    )

    name_chain =  LLMChain(llm=llm, prompt = prompt_template_name, output_key = "pet_name")

    response = name_chain.invoke({'animal_type': animal_type , 'pet_color': pet_color})

    return response

if __name__ == "__main__":
    print (generate_pet_names("horse","white"))
