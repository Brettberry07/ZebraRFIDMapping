import json

def parse_messages(data):
    parsed = []
    for entry in data:
        try:
            # Parse the inner JSON string
            inner_msg = json.loads(entry["Message"])
            
            parsed.append({
                "id": inner_msg.get("id"),
                "idFormat": inner_msg.get("idFormat"),
                "type": inner_msg.get("type"),
                "site": inner_msg.get("site"),
                "region": inner_msg.get("region"),
                "timestamp": inner_msg.get("timestamp"),
                "events": inner_msg.get("events", []),
                "x": inner_msg.get("x"),
                "y": inner_msg.get("y"),
                "z": inner_msg.get("z"),
                "outerTimestamp": entry.get("Timestamp")
            })
        except Exception as e:
            print(f"Error parsing entry: {e}")
    return parsed


if __name__ == "__main__":
    # Example: load from file
    with open("RFID_Data.json", "r") as f:
        raw_data = json.load(f)

    messages = parse_messages(raw_data)

    # # Print nicely
    # with open("parsed_messages.json", "w") as f:
    #     json.dump(messages, f, indent=2)
    
    # printing only the ids of each message
    for msg in messages:
        print(msg["id"])
