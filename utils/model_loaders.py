from langchain_groq import ChatGroq
from typing_extensions import Literal , Optional , Any
from pydantic import BaseModel , Field
import os
from utils.config_loaders import load_config


class ConfigLoader: 
    def __init__(self):
        print(f'Loaded config ....')
        self.config = load_config() 

    def __getitem__(self,key) : 
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider = Literal['groq'] = 'groq'
    config : Optional[ConfigLoader] = Field(default=None,exclude=True)


    def model_post_init(self,__context:Any) -> None : 
        self.config = ConfigLoader()


    class Config:
        arbitrary_types_allowed = True


    def load_llm(self):
        """
        Docstring for load_llm
        
        :param self: Description
        """
        print("LLM Loading...")
        print(f"loading model from provider: {self.model_provider}")
        if self.model_provider == "groq" : 
            print("Loading LLM from Groq .........")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm = ChatGroq(model= model_name , api_key=groq_api_key)

        return llm