import json

def generate_component_id(category, component_type, name):
    return f"gb.{category}.{component_type}.{name.replace(' ', '')}"

def collect_system_info():
    system_info = {}
    
    print("Welcome to the IoT System Prototype Questionnaire!\n")

    # Get project name
    project_name = input("Enter the name of your project: ")
    
    # Data collection
    print("Data Collection:")
    print("---------------")
    print("Data collection involves gathering raw data from various sensors or sources.")
    num_data_collection = int(input("How many data collection components do you want to add? "))
    system_info["data_collection"] = []
    for i in range(1, num_data_collection+1):
        print(f"Describe data collection component {i}:")
        data_collection_component = {}
        data_collection_component["id"] = generate_component_id("data", "collection", input("Name (e.g., Temperature Sensor): "))
        data_collection_component["description"] = input("Description: ")
        data_collection_type = input("Is this component a sensor or a controller? (Enter 'sensor' or 'controller'): ").lower()
        if data_collection_type == "sensor":
            data_collection_component["sensors"] = input("What types of sensors are used for data collection? (e.g., Thermocouple, Humidity Sensor): ")
            data_collection_component["sampling_rate"] = input("What is the sampling rate of sensors? (e.g., 1 sample/second): ")
        elif data_collection_type == "controller":
            data_collection_component["controller_type"] = input("What type of controller is used for data collection? (e.g., Raspberry Pi, Arduino): ")
            data_collection_component["communication_protocol"] = input("What communication protocol does the controller use? (e.g., MQTT, HTTP): ")
        system_info["data_collection"].append(data_collection_component)
    
    # Data transmission
    print("\nData Transmission:")
    print("-----------------")
    print("Data transmission involves sending the collected data to other systems or devices.")
    num_data_transmission = int(input("How many data transmission components do you want to add? "))
    system_info["data_transmission"] = []
    for i in range(1, num_data_transmission+1):
        print(f"Describe data transmission component {i}:")
        data_transmission_component = {}
        data_transmission_component["id"] = generate_component_id("data", "transmission", input("Name (e.g., Wi-Fi Module): "))
        data_transmission_component["description"] = input("Description: ")
        data_transmission_component["protocol"] = input("What communication protocol is used for transmission? (e.g., Wi-Fi, Bluetooth): ")
        system_info["data_transmission"].append(data_transmission_component)
    
    # Data processing
    print("\nData Processing:")
    print("----------------")
    print("Data processing includes manipulating, analyzing, or transforming the collected data.")
    num_data_processing = int(input("How many data processing components do you want to add? "))
    system_info["data_processing"] = []
    for i in range(1, num_data_processing+1):
        print(f"Describe data processing component {i}:")
        data_processing_component = {}
        data_processing_component["id"] = generate_component_id("data", "processing", input("Name (e.g., Data Analyzer): "))
        data_processing_component["description"] = input("Description: ")
        data_processing_component["algorithms"] = input("What algorithms are used for data processing? (e.g., Machine Learning, Statistical Analysis): ")
        system_info["data_processing"].append(data_processing_component)
    
    # Data storage
    print("\nData Storage:")
    print("-------------")
    print("Data storage involves storing the processed data.")
    num_data_storage = int(input("How many data storage components do you want to add? "))
    system_info["data_storage"] = []
    for i in range(1, num_data_storage+1):
        print(f"Describe data storage component {i}:")
        data_storage_component = {}
        data_storage_component["id"] = generate_component_id("data", "storage", input("Name (e.g., Database Server): "))
        data_storage_component["description"] = input("Description: ")
        data_storage_component["type"] = input("What type of database is used for storage? (e.g., SQL, NoSQL): ")
        system_info["data_storage"].append(data_storage_component)
    
    # Data visualization
    print("\nData Visualization:")
    print("-------------------")
    print("Data visualization involves presenting the processed data in a visual format.")
    num_data_visualization = int(input("How many data visualization components do you want to add? "))
    system_info["data_visualization"] = []
    for i in range(1, num_data_visualization+1):
        print(f"Describe data visualization component {i}:")
        data_visualization_component = {}
        data_visualization_component["id"] = generate_component_id("data", "visualization", input("Name (e.g., Dashboard): "))
        data_visualization_component["description"] = input("Description: ")
        data_visualization_component["platform"] = input("What platform is used for data visualization? (e.g., Tableau, Grafana): ")
        system_info["data_visualization"].append(data_visualization_component)
    
    # Automated action
    print("\nAutomated Action:")
    print("-----------------")
    print("Automated action involves taking predefined actions based on certain conditions.")
    num_automated_action = int(input("How many automated action components do you want to add? "))
    system_info["automated_action"] = []
    for i in range(1, num_automated_action+1):
        print(f"Describe automated action component {i}:")
        automated_action_component = {}
        automated_action_component["id"] = generate_component_id("automated", "action", input("Name (e.g., Alarm System): "))
        automated_action_component["description"] = input("Description: ")
        automated_action_component["triggers"] = input("What triggers automated actions? (e.g., Threshold Exceeded, Time Interval): ")
        system_info["automated_action"].append(automated_action_component)
    
    return project_name, system_info

def save_to_json(project_name, system_info):
    filename = f"{project_name}_iot_system_prototype.json"
    with open(filename, 'w') as f:
        json.dump(system_info, f, indent=4)
    print(f"\nYour IoT system prototype information has been saved to '{filename}'.")

if __name__ == "__main__":
    project_name, system_info = collect_system_info()
    save_to_json(project_name, system_info)