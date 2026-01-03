from utils.model_loaders import ModelLoader
from prompt_library.prompt import System_prompt

from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currency_conversions import CurrencyCnverterTool

from langgraph.graph import START , END , StateGraph , MessageState
from langgraph.prebuilt import ToolNode , tools_condition

class GraphBuilder ():
    def __init__(self,model_provider:str = "groq") : 
        self.tools = []
        self.weather_tools = WeatherInfoTool()
        self.place_search_tool = PlaceSearchTool()
        self.calculator_tool = CalculatorTool()
        self.currency_converter_tool = CurrencyCnverterTool()

        self.tools.extend([
            * self.weather_tools.weather_tool_list,
            * self.place_search_tool.place_search_tool_list,
            * self.currency_converter_tool.currency_converter_tool_list,
            * self.calculator_tool.calculator_tool_list])
        
        self.System_prompt = System_prompt
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)

        self.graph = None

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
        return self.build_graph()