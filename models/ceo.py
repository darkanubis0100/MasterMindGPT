import tkinter as tk

class CEO:
    def __init__(self, agent_listbox, chat_output):
        self.agents = {}
        self.jobs = []        
        #self.ceo_boss = CEO(self.agent_listbox)
        self.agent_listbox = agent_listbox
        from gui.task_board_gui import Logger
        self.logger = Logger(chat_output) 
                        
    def initiate_workflow(self, message):
        if message == "start the workflow":
            # Filter only those tasks that belong to the '1 Planner' team
            planner_tasks = [job for job in self.jobs if job.team == '1 Planner']
            for job in planner_tasks:
                self.delegate_task(job)

    def add_agent(self, agent):                     
        self.agents[agent.name] = agent
        print(f"Added agent {agent.name} to CEO's list of agents.")
        self.logger.log_to_widget(f"Added agent {agent.name} to CEO's list of agents.")
        self.agent_listbox.insert(tk.END, agent.name)  # Add this line
        
    def delegate_task(self, job):           
        print(f"Delegating task: {job}")  # Print a message
        if not self.agents:
            print("No agents available")
            self.logger.log_to_widget("No agents available")
            return

        # Delegate task to the appropriate agent based on job team
        agent = self.agents.get(job['Team'])
        #agent = self.agents.get(job.team)
        if agent:
            agent.handle_task(job)
            self.report_task_delegation(job)
        else:
            print(f"No matching agent found for team {job['Team']}.")
            self.logger.log_to_widget(f"No matching agent found for team {job['Team']}.")
            print("Available agents:", self.agents.keys())
            self.logger.log_to_widget(f"Available agents: {self.agents.keys()}")

    def report_task_delegation(self, job):       
        print(f"Delegated task '{job.description}' to {job['Team']}.")
        self.logger.log_to_widget(f"Delegated task '{job.description}' to {job['Team']}.")
        
    def report_tasks_status(self):
        status_report = {agent_name: agent.report_status() for agent_name, agent in self.agents.items()}
        return status_report

    def add_job(self, job):       
        self.jobs.append(job)
        print(f"Added job {job.description} to CEO's list of jobs.")
        self.logger.log_to_widget(f"Added job {job.description} to CEO's list of jobs.")