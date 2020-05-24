# TODO :Implement rules and structures based on cases observed and generate an automated User, with predetermined

# TODO :Write the actual classes

# TODO :Write the actual rules

# TODO :Create a context analyzer to analyze rule conflict and take necessary action.

# TODO :Make the server check for each rule's question and answer and update the user agent's vals.

# TODO : Change the type of I/O files to CSV files (from text) for faster read and removal of text splitting.
import textblob
import matplotlib.pyplot as plt
from enum import Enum
import csv

RuleDict = {}
BaseRules = []
reasonlist = []
past_agents = []


# these are the types of inputs in the system
class inputType(Enum):
    y_n = 1
    one_to_5 = 2
    textblock = 3
    one_to_ten = 4
    one_word = 5


class categories(Enum):
    selfesteem = 1  # relevant for gamer motivations
    depression = 2  # relevant for escapism
    validation = 3  # relevant for social media use
    popularity = 4  # relevant for social media use
    anxiety = 5  # relevant for escapism, gamer motivation and social media
    loneliness = 6  # relevant for social media use and gamer motivations
    satisfaction = 7  # relevant for gamer motivations and social media use
    stress = 8  # relevant for reasons for relapse, escapism


class agent:
    def __init__(self, name, selfesteem, depression, need_validation, anxiety, loneliness, satisfaction,
                 stress, reasons, disorderDict):
        self.name = name
        self.selfesteem = selfesteem
        self.depression = depression
        self.need_validation = need_validation
        self.anxiety = anxiety
        self.loneliness = loneliness
        self.satisfaction = satisfaction
        self.stress = stress
        self.reasons = reasons
        self.disorderDict = disorderDict


# The rule's answer influences these scores in a certain way.
class Rule:
    def __init__(self, query, expectedtype, category, category_score, priority):
        self.query = query
        self.expectedtype = expectedtype
        self.category = category
        self.category_score = category_score
        self.priority = priority


# The method to create new rules
def createRule(query, iotype, categoryaffected, score, priority):
    return Rule(query, iotype, categoryaffected, score, priority)

# Get the list of past agents and their values from the datafile
def readagents():
    global past_agents
    with open('datafile.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        print("Reading data from file")
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print({row["name"], "is the name"})
            past_agents.append(
                createAgent({row["name"]}, {row["selfesteem"]}, {row["depression"]}, {row["need_validation"]},
                            {row["anxiety"]}, {row["loneliness"]}, {row["satisfaction"]}, {row["stress"]},
                            {row["reasonlist"]}, {row["disorderlist"]}))
            line_count += 1
        print(f'Processed {line_count - 1} agents.')

# Write the new agent's vals to the datafile
def writeagents(human_agent):
    with open('datafile.csv', mode='a+') as human_agentfile:
        human_agent_writer = csv.writer(human_agentfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        human_agent_writer.writerow([str(human_agent.name), str(human_agent.selfesteem), str(human_agent.depression),
                                     str(human_agent.need_validation), str(human_agent.anxiety),
                                     str(human_agent.loneliness),
                                     str(human_agent.satisfaction), str(human_agent.stress), str(human_agent.reasons),
                                     str(human_agent.disorderDict)])


# Meant to read rules from a csv file
def readRules():
    return True


# Meant to write a new rule to the csv
def writeRules():
    return True


def createAgent(name, esteem_score, depression_score, validation_score, anxiety_score, loneliness_score,
                satisfaction_score, stress_score, reasonsforissue, disordersidentified):
    return agent(name, esteem_score, depression_score, validation_score, anxiety_score, loneliness_score,
                 satisfaction_score, stress_score, reasonsforissue, disordersidentified)


def checkforname(name):
    # TODO : Deprecate the entire function and read from csv for data and compare with input name.
    namelist = []
    nametxt = name + "\n"
    namefile_read = open("datafile.csv", "r")
    if namefile_read.mode == "r":
        content = namefile_read.readlines()
        for nameInstance in content:
            namelist.append(nameInstance)
            print("This is the namelist", namelist)
        print(content)
        namefile_read.close()
    namefile_append = open("names.txt", "a+")
    if nametxt not in namelist:
        return name
    else:
        # TODO : Load data from an already present agent archive. Path should be name.txt
        print("Loading old Data from file")
        namefile_append.close()
        return name


def intro():
    readagents()
    name = input("\nEnter your name (in one word)\n")
    checkforname(name)
    print("\n Hello," + name + " this is your friendly neighbourhood AI.\n I hope you are doing fine."
                               "\n I would like to request your help in helping me understand something."
                               "\n I hope you can cooperate with me on this.\n")


# Get initial values from user in order to get some bae values from the user for building their initial profile
def setupbasefeelings(name):
    checkbasefeeling_depression = createRule(
        "\nI haven't been all chipper lately.How are you feeling today ?\n",
        inputType.textblock,
        categories.depression,
        .1)
    BaseRules.append(checkbasefeeling_depression)

    print("base condition added")

    checkbasefeeling_loneliness = createRule(
        "\nI have been trying to make friends lately, "
        "I am always looking for information on making friends.\n"
        "Do you have a lot of friends ?",
        inputType.y_n,
        categories.popularity,
        .1,
        0)
    BaseRules.append(checkbasefeeling_loneliness)

    print("base condition added")

    checkbasefeeling_anxiety = createRule(
        "\nAre you feeling worried about the future?\n",
        inputType.textblock,
        categories.anxiety,
        .1,
        0)
    BaseRules.append(checkbasefeeling_anxiety)

    print("base condition added")

    checkbasefeelings_selfesteem = createRule(
        "\nI have been finding it hard to understand my own value lately, do you feel the same ?\n",
        inputType.y_n,
        categories.selfesteem,
        .2,
        0)
    BaseRules.append(checkbasefeelings_selfesteem)

    print("base condition added")

    checkbasefeelings_satisfaction = createRule(
        "\nDo you feel satisfied with how things are currently, if not, what is unsatisfactory ?\n",
        inputType.textblock,
        categories.satisfaction,
        .1,
        0)
    BaseRules.append(checkbasefeelings_satisfaction)

    print("base condition added")

    checkbasefeelings_stress = createRule(
        "\nDo you feel as if you are under a lot of pressure with regards to work, or personal life, if so, why? ?\n",
        inputType.textblock,
        categories.stress,
        .1,
        0)
    BaseRules.append(checkbasefeelings_stress)

    print("base condition added")


def main():
    intro()


if __name__ == "__main__":
    main()
# TODO :GetCauses() -> Meant to retrieve causal agent data from user based on past cases (this is the reason)

# TODO :GetQuery() -> Meant to retrieve next query in queue and send it to the user client through the server


"""
BasicStructure :

Global Variables :

List Global_Disorders -> Instantiated list of all disorders
Global_AI_Agent -> Instance of AI agent
Global_Human_Agent -> Instance of Human agent
RuleDict {Tuple(intensity_symptoms, intensity_category), rule} -> Helps choose next rule
List RuleQueue -> List of rules added to the queue of rules to be assessed by the user agent.




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
