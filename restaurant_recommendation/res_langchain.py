import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature = 0.8)

def generate_restaurant(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for it."   
    )

    # Runnable sequence
    # chain = prompt | llm
    chain1 = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_item = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name} restaurant. Return it as a comma separated list."   
    )

    chain2 = LLMChain(llm=llm, prompt=prompt_template_item, output_key="menu_items")

    chain = SequentialChain(
        chains = [chain1, chain2],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name','menu_items'])
    
    response = chain.invoke({'cuisine':cuisine})
    return response

if __name__=="__main__":
    print(generate_restaurant("American"))