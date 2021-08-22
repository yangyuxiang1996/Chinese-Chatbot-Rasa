# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionInternalMedicine(Action):
    def name(self) -> Text:
        return "action_internal_medicine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        """
        1: 连接用户的数据（输入的文本）
        2: 连接es
        3: 分本分词
        4: 处理后的文本放到es进行查询
        5: 通过es进行问题的匹配，进行初步的粗召回
        6: 将粗召回的结果和用户的问题输入到Bert或者其它的相似度匹配算法中，例如TF-IDF
        7: 通过上一步的算法，得到相似度匹配的结果
        8: 将相似度匹配的结果按照相似度进行倒序排序
        9: 将倒序排序的内容进行返回，取TopN返回：
        9.1: 如果大于95%，直接返回最大的结果
        9.2: 如果大于50%，小于95%，返回top10
        9.3: 如果小于50%，提示用户，输入的问题无法找到相应的答案，建议换一种问法。
        """

        return []

class ValidateMedicineForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_medicine_form"

    @staticmethod
    def ask_about_db() -> List[Text]:
        """Database of supported cuisines"""

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
