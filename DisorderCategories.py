# TODO :Implement rules and structures based on cases observed and generate an automated User, with predetermined

# TODO :Write the actual classes

# TODO :Write the actual rules

# TODO :Create a context analyzer to analyze rule conflict and take necessary action.

# TODO :Make the server check for each rule's question and answer and update the user agent's vals.

# TODO : Change the type of I/O files to CSV files (from text) for faster read and removal of text splitting.
import textblob
import matplotlib.pyplot as plt
from enum import Enum

RuleDict = {}
BaseRules = []


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
    stress = 8 # relevant for reasons for relapse, escapism


class agent:
    def __init__(self, name, selfesteem, depression, validation, popularity, anxiety, loneliness, satisfaction,
                 stress, disorderDict):
        self.name = name
        self.selfesteem = selfesteem
        self.depression = depression
        self.validation = validation
        self.popularity = popularity
        self.anxiety = anxiety
        self.loneliness = loneliness
        self.satisfaction = satisfaction
        self.disorderDict = disorderDict



# The rule's answer influences these scores in a certain way.
class Rule:
    def __init__(self, query, expectedtype, answer, category, reason, category_score):
        self.query = query
        self.expectedtype = expectedtype
        self.answer = answer
        self.category = category
        self.reason = reason
        self.category_score = category_score


class introspectioncategories:
    def __init__(self, id, value, reasonlist, ):
        self.id = id
        self.value = value
        self.reasonlist = reasonlist


# The method to create new rules
def createRule(query, iotype, answerstr, categoryaffected, reason, score):
    return Rule(query, iotype, answerstr, categoryaffected, reason, score)


def createAgent():
    return agent()


def checkforname(name):
    namelist = []
    nametxt = name+"\n"
    namefile_read = open("names.txt", "r")
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
    name = input("\nEnter your name (in one word)\n")
    checkforname(name)
    print("\n Hello," + name + " this is your friendly neighbourhood AI.\n I hope you are doing fine."
                               "\n I would like to request your help in helping me understand something."
                               "\n I hope you can cooperate with me on this.\n")


# Get initial values from user in order to build a rule tree for this particular user.
def setupbasefeelings(name):
    checkbasefeeling_depression = createRule(
        "\nI haven't been all chipper lately.How are you feeling today ?\n",
        inputType.textblock,
        "",
        categories.depression,
        "",
        .1)
    BaseRules.append(checkbasefeeling_depression)

    print("base condition added")


    checkbasefeeling_loneliness = createRule(
        "\nI have been trying to make friends lately, "
        "I am always looking for information on making friends.\n"
        "Do you have a lot of friends ?",
        inputType.y_n,
        "",
        categories.popularity,
        .1)
    BaseRules.append(checkbasefeeling_loneliness)

    print("base condition added")


    checkbasefeeling_anxiety = createRule(
        "\nAre you feeling worried about the future?\n",
        inputType.textblock,
        "",
        categories.anxiety,
        .1)
    BaseRules.append(checkbasefeeling_anxiety)

    print("base condition added")


    checkbasefeelings_selfesteem = createRule(
        "\nI have been finding it hard to understand my own value lately, do you feel the same ?\n",
        inputType.y_n,
        "",
        categories.selfesteem,
        .2)
    BaseRules.append(checkbasefeelings_selfesteem)

    print("base condition added")


    checkbasefeelings_satisfaction = createRule(
        "\nDo you feel satisfied with how things are currently, if not, what is unsatisfactory ?\n",
        inputType.textblock,
        "",
        categories.satisfaction,
        .1)
    BaseRules.append(checkbasefeelings_satisfaction)

    print("base condition added")


    checkbasefeelings_satisfaction = createRule(
        "\nDo you feel as if you are under a lot of pressure with regards to work, or personal life, why do you feel that way ?\n",
        inputType.textblock,
        "",
        categories.satisfaction,
        .1)
    BaseRules.append(checkbasefeelings_satisfaction)

    print("base condition added")


def main():
    intro()


if __name__ == "__main__":
    main()
# TODO :GetCauses() -> Meant to retrieve causal agent data from user based on past cases

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
