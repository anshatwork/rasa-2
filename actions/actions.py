# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker # type: ignore
# from rasa_sdk.executor import CollectingDispatcher # type: ignore

# class ActionExtractEntities(Action):
#     def name(self) -> Text:
#         return "action_extract_entities"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         entities = tracker.latest_message.get("entities", [])
#         entity_texts = [entity["value"] for entity in entities]
#         response = "Identified entities: {}".format(", ".join(entity_texts))
#         dispatcher.utter_message(text=response)
#         return []