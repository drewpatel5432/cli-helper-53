import json
from typing import Any, Dict, List

class ClickEvent:
    def __init__(self, x: int, y: int, delay: float):
        self.x = x
        self.y = y
        self.delay = delay

    def to_dict(self) -> Dict[str, Any]:
        return {'x': self.x, 'y': self.y, 'delay': self.delay}

def serialize_click_events(events: List[ClickEvent]) -> str:
    events_dict = [event.to_dict() for event in events]
    return json.dumps(events_dict, indent=4)

def deserialize_click_events(data: str) -> List[ClickEvent]:
    try:
        events_dict = json.loads(data)
        return [ClickEvent(**event) for event in events_dict]
    except (json.JSONDecodeError, TypeError) as e:
        raise ValueError(f"Invalid data: {e}") from e