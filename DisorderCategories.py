# TODO :Implement rules and structures based on cases observed and generate an automated User, with predetermined

# TODO :Write the actual classes

# TODO :Write the actual rules

# TODO :Create a context analyzer

# TODO :Make the server check for each rule's question and answer and update the user agent's vals.

"""
BasicStructure :

Global Variables :

List Global_Disorders -> Instantiated list of all disorders
Global_AI_Agent -> Instance of AI agent
Global_Human_Agent -> Instance of Human agent
RuleDict {Tuple(intensity_symptoms, intensity_category), rule} -> Helps choose next rule




class Agent:
    List(categories)
    dict(intensity, category)
    List(causal_agents)
    dict(intensity, Symptoms)
    Functions :

    checkDisorder(self) -> Cycles through all disorders to determine if agent is afflicted with any

________________________________________________________________________________________________________________________

class Disorders:
    List(categories)
    dictThreshold(category, intensity)
    List(resolutionStrats)
    string SimilarScenario
    Functions:

    isDiagnosed(self, agent) -> Checks for intensity of categories in the user agent and returns disorder if > threshold
    returnStory(self) -> Prints a story of a person with the similar disorder to help understand the issue at hand



________________________________________________________________________________________________________________________

class Rule:
    string Query
    Enum expectedAnswerType (Answers should conform to some predetermined type)
    string answer
    addressed_symptoms
    Functions :

    calculateCategoryVal(self) -> Uses it to calculate the intensity for categories from symptoms

________________________________________________________________________________________________________________________

class conflictAnalyzer:

    Analyzes context and then resolves conflict between rules by assigning priority to the rules
"""