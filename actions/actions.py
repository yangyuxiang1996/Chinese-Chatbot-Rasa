# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ValidateMedicinesForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_medicines_form"

    def validate_medicine(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value:
            return {"medicine": slot_value}

    @staticmethod
    def ask_about_db() -> List[Text]:

        return ["efficacy", "origin", "composition"]

    def validate_ask_about(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if slot_value.lower() in self.ask_about_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"ask_about": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"ask_about": None}


class ActionInternalMedicine(Action):

    def name(self) -> Text:
        return "action_internal_medicine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is internalmedicine")

        return []


class ActionObstetricsGynecology(Action):

    def name(self) -> Text:
        return "action_obstetrics_gynecology"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is obstetrics gynecology")

        return []


class ActionPediatric(Action):

    def name(self) -> Text:
        return "action_pediatric"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is pediatric")

        return []


class ActionOncology(Action):

    def name(self) -> Text:
        return "action_oncology"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is oncology")

        return []


class ActionAndriatria(Action):

    def name(self) -> Text:
        return "action_andriatria"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is andriatria")

        return []


class ActionSurgical(Action):

    def name(self) -> Text:
        return "action_surgical"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is surgical")

        return []


class ActionMedicines(Action):

    def name(self) -> Text:
        return "action_medicines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="this is medicines")
        slots = []
        for key in ('medicine', 'ask_about'):
            slots.append(SlotSet(key=key, value=None))
        return slots
