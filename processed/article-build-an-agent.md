---
id: "article_c4f5262c"
title: "Build an Agent"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [agents, langchain, langgraph, tool-calling]
summary: "Language models use tool-calling to act as reasoning engines. You can build an agent with LangChain and LangGraph. The agent uses search tools and conversational memory. You can stream messages and tokens from the agent."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Language models use tool-calling to act as reasoning engines. You can build an agent with LangChain and LangGraph. The agent uses search tools and conversational memory. You can stream messages and tokens from the agent.

## Key Takeaways

- Agents use LLMs as reasoning engines to select actions.
- Tool-calling lets language models decide when to invoke external tools.
- LangGraph constructs the agent using an API.
- A checkpointer adds conversational memory to the agent.
- You can stream intermediate messages and individual tokens.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Build an Agent
---
Date:May 13, 2025
Tags: #Agents
Summary:

---
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/tutorials/agents.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/tutorials/agents.ipynb)

# Build an Agent

By themselves, language models can't take actions - they just output text. A big use case for LangChain is creating **agents**. [Agents](https://python.langchain.com/docs/concepts/agents/) are systems that use [LLMs](https://python.langchain.com/docs/concepts/chat_models/) as reasoning engines to determine which actions to take and the inputs necessary to perform the action. After executing actions, the results can be fed back into the LLM to determine whether more actions are needed, or whether it is okay to finish. This is often achieved via [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/).

In this tutorial we will build an agent that can interact with a search engine. You will be able to ask this agent questions, watch it call the search tool, and have conversations with it.

## End-to-end agent

The code snippet below represents a fully functional agent that uses an LLM to decide which tools to use. It is equipped with a generic search tool. It has conversational memory - meaning that it can be used as a multi-turn chatbot.

In the rest of the guide, we will walk through the individual components and what each part does - but if you want to just grab some code and get started, feel free to use this!

```
# Import relevant functionalityfrom langchain_anthropic import ChatAnthropicfrom langchain_community.tools.tavily_search import TavilySearchResultsfrom langchain_core.messages import HumanMessagefrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.prebuilt import create_react_agent# Create the agentmemory = MemorySaver()model = ChatAnthropic(model_name="claude-3-sonnet-20240229")search = TavilySearchResults(max_results=2)tools = [search]agent_executor = create_react_agent(model, tools, checkpointer=memory)
```

**API Reference:**[ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

```
# Use the agentconfig = {"configurable": {"thread_id": "abc123"}}for step in agent_executor.stream(    {"messages": [HumanMessage(content="hi im bob! and i live in sf")]},    config,    stream_mode="values",):    step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================hi im bob! and i live in sf==================================[1m Ai Message [0m==================================Hello Bob! Since you didn't ask a specific question, I don't need to use any tools right now. I'm an AI assistant created by Anthropic to be helpful, honest, and harmless. Feel free to ask me anything and I'll do my best to provide a useful response or look up information using my capabilities.
```

```
for step in agent_executor.stream(    {"messages": [HumanMessage(content="whats the weather where I live?")]},    config,    stream_mode="values",):    step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================whats the weather where I live?==================================[1m Ai Message [0m==================================[{'text': 'To get the current weather for your location in San Francisco, I can use the tavily_search_results_json tool:', 'type': 'text'}, {'id': 'toolu_01AKa2MErG1CU3zRiGsvpBud', 'input': {'query': 'san francisco weather'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]Tool Calls:  tavily_search_results_json (toolu_01AKa2MErG1CU3zRiGsvpBud) Call ID: toolu_01AKa2MErG1CU3zRiGsvpBud  Args:    query: san francisco weather=================================[1m Tool Message [0m=================================Name: tavily_search_results_json[{"url": "https://www.weatherapi.com/", "content": "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.775, 'lon': -122.4183, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1739994486, 'localtime': '2025-02-19 11:48'}, 'current': {'last_updated_epoch': 1739994300, 'last_updated': '2025-02-19 11:45', 'temp_c': 13.3, 'temp_f': 55.9, 'is_day': 1, 'condition': {'text': 'Light rain', 'icon': '//cdn.weatherapi.com/weather/64x64/day/296.png', 'code': 1183}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 195, 'wind_dir': 'SSW', 'pressure_mb': 1023.0, 'pressure_in': 30.2, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 87, 'cloud': 100, 'feelslike_c': 12.7, 'feelslike_f': 54.8, 'windchill_c': 9.1, 'windchill_f': 48.4, 'heatindex_c': 10.2, 'heatindex_f': 50.3, 'dewpoint_c': 9.8, 'dewpoint_f': 49.7, 'vis_km': 4.0, 'vis_miles': 2.0, 'uv': 1.4, 'gust_mph': 8.9, 'gust_kph': 14.4}}"}, {"url": "https://world-weather.info/forecast/usa/san_francisco/february-2025/", "content": "Weather in San Francisco in February 2025 (California) - Detailed Weather Forecast for a Month Weather World Weather in San Francisco Weather in San Francisco in February 2025 San Francisco Weather Forecast for February 2025, is based on previous years' statistical data. +59°+50° +59°+52° +59°+50° +61°+52° +59°+50° +61°+50° +61°+52° +63°+52° +61°+52° +61°+50° +61°+50° +61°+50° +59°+50° +59°+50° +61°+50° +61°+52° +59°+50° +59°+48° +57°+48° +59°+50° +59°+48° +59°+50° +57°+46° +61°+50° +61°+50° +59°+50° +59°+48° +59°+50° Extended weather forecast in San Francisco HourlyWeek10-Day14-Day30-DayYear Weather in large and nearby cities Weather in Washington, D.C.+41° Sacramento+55° Pleasanton+55° Redwood City+55° San Leandro+55° San Mateo+54° San Rafael+52° San Ramon+52° South San Francisco+54° Vallejo+50° Palo Alto+55° Pacifica+55° Berkeley+54° Castro Valley+55° Concord+52° Daly City+54° Noverd+52° Sign Hill+54° world's temperature today day day Temperature units"}]==================================[1m Ai Message [0m==================================The search results provide the current weather conditions and forecast for San Francisco. According to the data from WeatherAPI, the current temperature in San Francisco is around 55°F (13°C) with light rain and winds around 6 mph. The extended forecast shows temperatures ranging from the upper 40s to low 60s Fahrenheit over the next few weeks.So in summary, it's a cool, rainy day currently in San Francisco where you live, Bob. Let me know if you need any other details about the weather there!
```

## Setup

### Jupyter Notebook

This guide (and most of the other guides in the documentation) uses [Jupyter notebooks](https://jupyter.org/) and assumes the reader is as well. Jupyter notebooks are perfect interactive environments for learning how to work with LLM systems because oftentimes things can go wrong (unexpected output, API down, etc), and observing these cases is a great way to better understand building with LLMs.

This and other tutorials are perhaps most conveniently run in a Jupyter notebook. See [here](https://jupyter.org/install) for instructions on how to install.

### Installation

To install LangChain run:

```
%pip install -U langchain-community langgraph langchain-anthropic tavily-python langgraph-checkpoint-sqlite
```

For more details, see our [Installation guide](https://python.langchain.com/docs/how_to/installation/).

### LangSmith

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with [LangSmith](https://smith.langchain.com/).

After you sign up at the link above, make sure to set your environment variables to start logging traces:

```
export LANGSMITH_TRACING="true"export LANGSMITH_API_KEY="..."
```

Or, if in a notebook, you can set them with:

```
import getpassimport osos.environ["LANGSMITH_TRACING"] = "true"os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

### Tavily

We will be using [Tavily](https://python.langchain.com/docs/integrations/tools/tavily_search/) (a search engine) as a tool. In order to use it, you will need to get and set an API key:

```
export TAVILY_API_KEY="..."
```

Or, if in a notebook, you can set it with:

```
import getpassimport osos.environ["TAVILY_API_KEY"] = getpass.getpass()
```

## Define tools

We first need to create the tools we want to use. Our main tool of choice will be [Tavily](https://python.langchain.com/docs/integrations/tools/tavily_search/) - a search engine. We have a built-in tool in LangChain to easily use Tavily search engine as tool.

```
from langchain_community.tools.tavily_search import TavilySearchResultssearch = TavilySearchResults(max_results=2)search_results = search.invoke("what is the weather in SF")print(search_results)# If we want, we can create other tools.# Once we have all the tools we want, we can put them in a list that we will reference later.tools = [search]
```

**API Reference:**[TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

```
[{'url': 'https://www.weatherapi.com/', 'content': "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.775, 'lon': -122.4183, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1739993250, 'localtime': '2025-02-19 11:27'}, 'current': {'last_updated_epoch': 1739992500, 'last_updated': '2025-02-19 11:15', 'temp_c': 13.3, 'temp_f': 55.9, 'is_day': 1, 'condition': {'text': 'Light rain', 'icon': '//cdn.weatherapi.com/weather/64x64/day/296.png', 'code': 1183}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 195, 'wind_dir': 'SSW', 'pressure_mb': 1023.0, 'pressure_in': 30.2, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 87, 'cloud': 100, 'feelslike_c': 12.7, 'feelslike_f': 54.8, 'windchill_c': 9.1, 'windchill_f': 48.4, 'heatindex_c': 10.2, 'heatindex_f': 50.3, 'dewpoint_c': 9.8, 'dewpoint_f': 49.7, 'vis_km': 4.0, 'vis_miles': 2.0, 'uv': 1.4, 'gust_mph': 8.9, 'gust_kph': 14.4}}"}, {'url': 'https://weathershogun.com/weather/usa/ca/san-francisco/480/february/2025-02-19', 'content': 'San Francisco, California Weather: Wednesday, February 19, 2025. Cloudy weather, overcast skies with clouds. Day 61°. Night 43°.'}]
```

## Using Language Models

Next, let's learn how to use a language model to call tools. LangChain supports many different language models that you can use interchangably - select the one you want to use below!

Select [chat model](https://python.langchain.com/docs/integrations/chat/):

- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)
- [](https://python.langchain.com/docs/tutorials/agents/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=3f26e2efd85af88550dda5d71904d706fc230b3e#)

```
pip install -qU "langchain[openai]"
```

```
import getpassimport osif not os.environ.get("OPENAI_API_KEY"):  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("gpt-4", model_provider="openai")
```

You can call the language model by passing in a list of messages. By default, the response is a `content` string.

```
from langchain_core.messages import HumanMessageresponse = model.invoke([HumanMessage(content="hi!")])response.content
```

**API Reference:**[HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
'Hi there!'
```

We can now see what it is like to enable this model to do tool calling. In order to enable that we use `.bind_tools` to give the language model knowledge of these tools

```
model_with_tools = model.bind_tools(tools)
```

We can now call the model. Let's first call it with a normal message, and see how it responds. We can look at both the `content` field as well as the `tool_calls` field.

```
response = model_with_tools.invoke([HumanMessage(content="Hi!")])print(f"ContentString: {response.content}")print(f"ToolCalls: {response.tool_calls}")
```

```
ContentString: Hello!ToolCalls: []
```

Now, let's try calling it with some input that would expect a tool to be called.

```
response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])print(f"ContentString: {response.content}")print(f"ToolCalls: {response.tool_calls}")
```

```
ContentString: ToolCalls: [{'name': 'tavily_search_results_json', 'args': {'query': 'weather san francisco'}, 'id': 'toolu_01VTP7DUvSfgtYxsq9x4EwMp'}]
```

We can see that there's now no text content, but there is a tool call! It wants us to call the Tavily Search tool.

This isn't calling that tool yet - it's just telling us to. In order to actually call it, we'll want to create our agent.

## Create the agent

Now that we have defined the tools and the LLM, we can create the agent. We will be using [LangGraph](https://python.langchain.com/docs/concepts/architecture/#langgraph) to construct the agent. Currently, we are using a high level interface to construct the agent, but the nice thing about LangGraph is that this high-level interface is backed by a low-level, highly controllable API in case you want to modify the agent logic.

Now, we can initialize the agent with the LLM and the tools.

Note that we are passing in the `model`, not `model_with_tools`. That is because `create_react_agent` will call `.bind_tools` for us under the hood.

```
from langgraph.prebuilt import create_react_agentagent_executor = create_react_agent(model, tools)
```

**API Reference:**[create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Run the agent

We can now run the agent with a few queries! Note that for now, these are all **stateless** queries (it won't remember previous interactions). Note that the agent will return the **final** state at the end of the interaction (which includes any inputs, we will see later on how to get only the outputs).

First up, let's see how it responds when there's no need to call a tool:

```
response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})response["messages"]
```

```
[HumanMessage(content='hi!', id='a820fcc5-9b87-457a-9af0-f21768143ee3'), AIMessage(content='Hello!', response_metadata={'id': 'msg_01VbC493X1VEDyusgttiEr1z', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 264, 'output_tokens': 5}}, id='run-0e0ddae8-a85b-4bd6-947c-c36c857a4698-0', usage_metadata={'input_tokens': 264, 'output_tokens': 5, 'total_tokens': 269})]
```

In order to see exactly what is happening under the hood (and to make sure it's not calling a tool) we can take a look at the [LangSmith trace](https://smith.langchain.com/public/28311faa-e135-4d6a-ab6b-caecf6482aaa/r)

Let's now try it out on an example where it should be invoking the tool

```
response = agent_executor.invoke(    {"messages": [HumanMessage(content="whats the weather in sf?")]})response["messages"]
```

```
[HumanMessage(content='whats the weather in sf?', id='1d6c96bb-4ddb-415c-a579-a07d5264de0d'), AIMessage(content=[{'id': 'toolu_01Y5EK4bw2LqsQXeaUv8iueF', 'input': {'query': 'weather in san francisco'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}], response_metadata={'id': 'msg_0132wQUcEduJ8UKVVVqwJzM4', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 269, 'output_tokens': 61}}, id='run-26d5e5e8-d4fd-46d2-a197-87b95b10e823-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'weather in san francisco'}, 'id': 'toolu_01Y5EK4bw2LqsQXeaUv8iueF'}], usage_metadata={'input_tokens': 269, 'output_tokens': 61, 'total_tokens': 330}), ToolMessage(content='[{"url": "https://www.weatherapi.com/", "content": "{\'location\': {\'name\': \'San Francisco\', \'region\': \'California\', \'country\': \'United States of America\', \'lat\': 37.78, \'lon\': -122.42, \'tz_id\': \'America/Los_Angeles\', \'localtime_epoch\': 1717238703, \'localtime\': \'2024-06-01 3:45\'}, \'current\': {\'last_updated_epoch\': 1717237800, \'last_updated\': \'2024-06-01 03:30\', \'temp_c\': 12.0, \'temp_f\': 53.6, \'is_day\': 0, \'condition\': {\'text\': \'Mist\', \'icon\': \'//cdn.weatherapi.com/weather/64x64/night/143.png\', \'code\': 1030}, \'wind_mph\': 5.6, \'wind_kph\': 9.0, \'wind_degree\': 310, \'wind_dir\': \'NW\', \'pressure_mb\': 1013.0, \'pressure_in\': 29.92, \'precip_mm\': 0.0, \'precip_in\': 0.0, \'humidity\': 88, \'cloud\': 100, \'feelslike_c\': 10.5, \'feelslike_f\': 50.8, \'windchill_c\': 9.3, \'windchill_f\': 48.7, \'heatindex_c\': 11.1, \'heatindex_f\': 51.9, \'dewpoint_c\': 8.8, \'dewpoint_f\': 47.8, \'vis_km\': 6.4, \'vis_miles\': 3.0, \'uv\': 1.0, \'gust_mph\': 12.5, \'gust_kph\': 20.1}}"}, {"url": "https://www.timeanddate.com/weather/usa/san-francisco/hourly", "content": "Sun & Moon. Weather Today Weather Hourly 14 Day Forecast Yesterday/Past Weather Climate (Averages) Currently: 59 \\u00b0F. Passing clouds. (Weather station: San Francisco International Airport, USA). See more current weather."}]', name='tavily_search_results_json', id='37aa1fd9-b232-4a02-bd22-bc5b9b44a22c', tool_call_id='toolu_01Y5EK4bw2LqsQXeaUv8iueF'), AIMessage(content='Based on the search results, here is a summary of the current weather in San Francisco:\n\nThe weather in San Francisco is currently misty with a temperature of around 53°F (12°C). There is complete cloud cover and moderate winds from the northwest around 5-9 mph (9-14 km/h). Humidity is high at 88%. Visibility is around 3 miles (6.4 km). \n\nThe results provide an hourly forecast as well as current conditions from a couple different weather sources. Let me know if you need any additional details about the San Francisco weather!', response_metadata={'id': 'msg_01BRX9mrT19nBDdHYtR7wJ92', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 920, 'output_tokens': 132}}, id='run-d0325583-3ddc-4432-b2b2-d023eb97660f-0', usage_metadata={'input_tokens': 920, 'output_tokens': 132, 'total_tokens': 1052})]
```

We can check out the [LangSmith trace](https://smith.langchain.com/public/f520839d-cd4d-4495-8764-e32b548e235d/r) to make sure it's calling the search tool effectively.

## Streaming Messages

We've seen how the agent can be called with `.invoke` to get a final response. If the agent executes multiple steps, this may take a while. To show intermediate progress, we can stream back messages as they occur.

```
for step in agent_executor.stream(    {"messages": [HumanMessage(content="whats the weather in sf?")]},    stream_mode="values",):    step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================whats the weather in sf?==================================[1m Ai Message [0m==================================[{'text': 'Okay, let me look up the current weather for San Francisco using a search engine:', 'type': 'text'}, {'id': 'toolu_01H1brh5EZpZqtqHBxkosPtN', 'input': {'query': 'san francisco weather'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]Tool Calls:  tavily_search_results_json (toolu_01H1brh5EZpZqtqHBxkosPtN) Call ID: toolu_01H1brh5EZpZqtqHBxkosPtN  Args:    query: san francisco weather=================================[1m Tool Message [0m=================================Name: tavily_search_results_json[{"url": "https://www.weatherapi.com/", "content": "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.775, 'lon': -122.4183, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1739994486, 'localtime': '2025-02-19 11:48'}, 'current': {'last_updated_epoch': 1739994300, 'last_updated': '2025-02-19 11:45', 'temp_c': 13.3, 'temp_f': 55.9, 'is_day': 1, 'condition': {'text': 'Light rain', 'icon': '//cdn.weatherapi.com/weather/64x64/day/296.png', 'code': 1183}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 195, 'wind_dir': 'SSW', 'pressure_mb': 1023.0, 'pressure_in': 30.2, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 87, 'cloud': 100, 'feelslike_c': 12.7, 'feelslike_f': 54.8, 'windchill_c': 9.1, 'windchill_f': 48.4, 'heatindex_c': 10.2, 'heatindex_f': 50.3, 'dewpoint_c': 9.8, 'dewpoint_f': 49.7, 'vis_km': 4.0, 'vis_miles': 2.0, 'uv': 1.4, 'gust_mph': 8.9, 'gust_kph': 14.4}}"}, {"url": "https://world-weather.info/forecast/usa/san_francisco/february-2025/", "content": "Weather in San Francisco in February 2025 (California) - Detailed Weather Forecast for a Month Weather World Weather in San Francisco Weather in San Francisco in February 2025 San Francisco Weather Forecast for February 2025, is based on previous years' statistical data. +59°+50° +59°+52° +59°+50° +61°+52° +59°+50° +61°+50° +61°+52° +63°+52° +61°+52° +61°+50° +61°+50° +61°+50° +59°+50° +59°+50° +61°+50° +61°+52° +59°+50° +59°+48° +57°+48° +59°+50° +59°+48° +59°+50° +57°+46° +61°+50° +61°+50° +59°+50° +59°+48° +59°+50° Extended weather forecast in San Francisco HourlyWeek10-Day14-Day30-DayYear Weather in large and nearby cities Weather in Washington, D.C.+41° Sacramento+55° Pleasanton+55° Redwood City+55° San Leandro+55° San Mateo+54° San Rafael+52° San Ramon+52° South San Francisco+54° Vallejo+50° Palo Alto+55° Pacifica+55° Berkeley+54° Castro Valley+55° Concord+52° Daly City+54° Noverd+52° Sign Hill+54° world's temperature today day day Temperature units"}]==================================[1m Ai Message [0m==================================The search results provide details on the current weather conditions and forecast for San Francisco. Some key details:- It is lightly raining in San Francisco right now, with a temperature around 55°F/13°C. - The forecast for the rest of February 2025 shows daytime highs mostly in the upper 50s to low 60s F, with night lows in the upper 40s to low 50s F. - Typical weather includes some rain, clouds, cool temperatures and breezy conditions.So in summary, as is common for San Francisco in late winter, it is currently cool with light rain showers, and similar mild, unsettled weather is expected over the next couple weeks. Layers and a light jacket would be advisable for being outdoors. Let me know if you need any other details!
```

## Streaming tokens

In addition to streaming back messages, it is also useful to stream back tokens. We can do this by specifying `stream_mode="messages"`.

::: note

Below we use `message.text()`, which requires `langchain-core>=0.3.37`.

:::

```
for step, metadata in agent_executor.stream(    {"messages": [HumanMessage(content="whats the weather in sf?")]},    stream_mode="messages",):    if metadata["langgraph_node"] == "agent" and (text := step.text()):        print(text, end="|")
```

```
Base|d on the weather| search| results, here| are the key details| about the weather in| San Francisco:|- The current temperature| in| San Francisco is aroun|d 55|-|56|°F (13|°|C).| Light| rain is occurring with| |100|% clou|d cover. |-| Winds| are aroun|d 5-9| mph from| the south|-southwest.|- The| forecast| for| the rest| of February| 2025 |shows da|ytime highs mostly| in the upper| 50s to| low| 60s°|F,| with overnight lows| in| the upper| 40s to| low| 50s°|F.|-| Overall|, typical| cool| an|d show|ery late| winter weather is| expected in San Francisco| for the remainder| of February,| with a| mix| of rain| and dry| periods|.| Temperatures will be| season|able| for| this| time of year.|So| in summary, San| Francisco is| experiencing light| rain an|d cool| temperatures currently, but| the late| winter forecast| shows typical mil|d and show|ery conditions| pers|isting through the en|d of the| month.| Let| me know if you| need any other| details about| the weather in the| city!|
```

## Adding in memory

As mentioned earlier, this agent is stateless. This means it does not remember previous interactions. To give it memory we need to pass in a checkpointer. When passing in a checkpointer, we also have to pass in a `thread_id` when invoking the agent (so it knows which thread/conversation to resume from).

```
from langgraph.checkpoint.memory import MemorySavermemory = MemorySaver()
```

**API Reference:**[MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
agent_executor = create_react_agent(model, tools, checkpointer=memory)config = {"configurable": {"thread_id": "abc123"}}
```

```
for chunk in agent_executor.stream(    {"messages": [HumanMessage(content="hi im bob!")]}, config):    print(chunk)    print("----")
```

```
{'agent': {'messages': [AIMessage(content="Hello Bob! It's nice to meet you again.", response_metadata={'id': 'msg_013C1z2ZySagEFwmU1EsysR2', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 1162, 'output_tokens': 14}}, id='run-f878acfd-d195-44e8-9166-e2796317e3f8-0', usage_metadata={'input_tokens': 1162, 'output_tokens': 14, 'total_tokens': 1176})]}}----
```

```
for chunk in agent_executor.stream(    {"messages": [HumanMessage(content="whats my name?")]}, config):    print(chunk)    print("----")
```

```
{'agent': {'messages': [AIMessage(content='You mentioned your name is Bob when you introduced yourself earlier. So your name is Bob.', response_metadata={'id': 'msg_01WNwnRNGwGDRw6vRdivt6i1', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 1184, 'output_tokens': 21}}, id='run-f5c0b957-8878-405a-9d4b-a7cd38efe81f-0', usage_metadata={'input_tokens': 1184, 'output_tokens': 21, 'total_tokens': 1205})]}}----
```

Example [LangSmith trace](https://smith.langchain.com/public/fa73960b-0f7d-4910-b73d-757a12f33b2b/r)

If you want to start a new conversation, all you have to do is change the `thread_id` used

```
config = {"configurable": {"thread_id": "xyz123"}}for chunk in agent_executor.stream(    {"messages": [HumanMessage(content="whats my name?")]}, config):    print(chunk)    print("----")
```

```
{'agent': {'messages': [AIMessage(content="I'm afraid I don't actually know your name. As an AI assistant without personal information about you, I don't have a specific name associated with our conversation.", response_metadata={'id': 'msg_01NoaXNNYZKSoBncPcLkdcbo', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 267, 'output_tokens': 36}}, id='run-c9f7df3d-525a-4d8f-bbcf-a5b4a5d2e4b0-0', usage_metadata={'input_tokens': 267, 'output_tokens': 36, 'total_tokens': 303})]}}----
```

## Conclusion

That's a wrap! In this quick start we covered how to create a simple agent. We've then shown how to stream back a response - not only with the intermediate steps, but also tokens! We've also added in memory so you can have a conversation with them. Agents are a complex topic with lots to learn!

For more information on Agents, please check out the [LangGraph](https://python.langchain.com/docs/concepts/architecture/#langgraph) documentation. This has it's own set of concepts, tutorials, and how-to guides.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
