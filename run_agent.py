from agent_core.agent import Agent

def main():
    print("🧠 PROJECTY-7 Activated")
    agent = Agent(name="PROJECTY-7")

    objective = input("Enter your objective: ")
    print("\n🤖 Planning and Executing...\n")
    agent.run(objective)

    # TESTING: Memory recall
    query = input("\nEnter a keyword to recall from memory: ")
    results = agent.recall(query)

    print("\n📚 Memory Results:")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
