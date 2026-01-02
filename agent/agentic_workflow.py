from utils.model_loaders import ModelLoader
from prompt_library.prompt import System_prompt

from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currency_conversions import CurrencyCnverterTool

from langgraph.graph import START , END , StateGraph , MessageState
from langgraph.prebuilt import ToolNode , tools_condition

class GraphBuilder ():
    def __init__(self) : 
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass