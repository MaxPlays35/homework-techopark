# Simpler fetcher
import json
import requests
import random

class Todo:
    @property
    def id(self) -> int:
        return self.__id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def completed(self) -> bool:
        return self.__completed

    def __init__(self, todo: dict) -> None:
        self.__user_id = todo['userId']
        self.__id = todo['id']
        self.__title = todo['title']
        self.__completed = todo['completed']

    
    def __repr__(self) -> str:
        return f'Todo for user with {self.__user_id} id'

data = requests.get("https://jsonplaceholder.typicode.com/todos/")
array = []

data = json.loads(data.content)

for todo in data:
    array.append(Todo(todo))

print(random.choice(array).title)
# print(array)
