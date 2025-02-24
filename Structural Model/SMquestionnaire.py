import json

keys = ["name",
        "id",
        "connections",
        "webpage"
        ]

def prompt_user(question):
    more_connections = "y"
    element = {}
    split = question.split("_")
    """Function to prompt the user for input."""
    print(split[2])
    response = input()
    element[keys[0]] = response
    element[keys[2]] = []
    while more_connections == "y":
        if split[3] != "None":
            print(split[3])
            element[keys[2]] += [input()]
        else:
            break
        print("Any more connections? (y/n)")
        more_connections = input()
    element[keys[1]] = "gb."+ split[0] + split[1] + response.lower()
    return element

def main():
    main = {"hardware":[{"controllers":[]}, {"sensors":[]}, {"energie":[]}], 
            "software":[{"ide":[]}, {"code":[]}, {"sites":[]}, {"tools":[]}, {"protocols":[]}]}  # Dictionary to store user responses
    print("What is your project called?")
    project_name = input()
    counter = 0
    # List of questions
    questions = [
        "hardware._controllers._Which controller did you use? (ex: RaspberryPi, ArduinoUNO, ArduinoNANO, ...)_To what are they connected? (ex: Other Controller, Sensors, Database, WebPage, ...)",
        "hardware._sensors._Which sensors did you use? (ex: Light, Temperature, Humidity, ...)_To which controller are they connected? (ex: Arduino, RaspberryPi, ...)",
        "hardware._energie._What did you use to power your project? (ex: Battery, PowerBank, Solar Panels, ...)_None",
        "software._ide._Which IDE did you use? (ex: Arduino IDE, OpenMV, ...)_None",
        "software._code._What is the name of the code files you created?_None",
        "software._sites._Which third-party application did you use? (ex: Adafruit, IFTTT, PowerBI, ...)_None",
        "software._tools._What did you use to connect your hardware? (ex: WiFi, Bluetooth, Cables, ...)_None",
        "software._protocols._What application layer protocols did you use? (ex: MQTT, http, ...)_None"
    ]   

    # Prompt user for responses to each question
    for question in questions:
        yes_no = "y"
        split = question.split("._")
        if (split[0] == "software") and (split[1] == "ide"):
            counter = 0
        while yes_no == "y":
            response = prompt_user(question)
            main[split[0]][counter][split[1]] += [response]
            print("Any other", split[1], "? (y/n)")
            yes_no = input()
        counter += 1
        yes_no = "y"

    # Write responses to a JSON file
    with open(project_name + '.json', 'w') as json_file:
        json.dump(main, json_file, indent=4)

    print("Your responses have been saved to " + project_name + "'.json'.")

if __name__ == "__main__":
    main()
