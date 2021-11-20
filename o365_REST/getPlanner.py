from office365.graph_client import GraphClient
from office365.graph_client import GraphServiceClient

graphClient = GraphServiceClient.builder().authenticationProvider( authProvider ).buildClient();

PlannerPlan plannerPlan = graphClient.planner().plans("{plan-id}")
	.buildRequest()
	.get();