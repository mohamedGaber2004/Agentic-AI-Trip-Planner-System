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
        self.tools = [
            WeatherInfoTool(),
            PlaceSearchTool(),
            CalculatorTool(),
            CurrencyCnverterTool()
        ]
        self.System_prompt = System_prompt
        self.llm_with_tools = ModelLoader().load_llm()

    def agent_function(self,state:MessageState):
        """Main Agent Function"""
        user_question = state["messages"]
        input_question = [self.System_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages":[response]}


    def build_graph(self):
        graph_builder = StateGraph(MessageState) 

        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools_condition))

        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)

        self.graph = graph_builder.compile()
        return self.graph



    def __call__(self):
        pass