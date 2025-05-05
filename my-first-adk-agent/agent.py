from google.adk.agents import Agent

# 1. Define the model (Gemini 2.0 in this case)
model = "gemini-2.0-flash-001"

# 2. Create the agent
root_agent = Agent(
    name="EchoBot",
    description="Echoes back anything you say.",
    instruction="Repeat the user's message back to them as clearly as possible.",
    model=model,
)
