from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature = 0.6)

def generate_Test_Cases(domain, functionality, number, type):

    prompt_template_name = PromptTemplate(
        input_variables=['number','functionality','domain', 'type'],
        template = "Generate top {number} test cases for {functionality} from {domain} industry in {type} format"
    )
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name)
    response = name_chain.run({'number': number, 'functionality': functionality, 'domain': domain, 'type': type})

    return response

if __name__ == "__main__":
    print(generate_Test_Cases("Insurance","Claim","4", "table"))
