from datetime import datetime

class DataHandler:

    def __create_iso_date(self, date):
        date = date.split(".")
        date.reverse()
        return "-".join(date)

    def __dict_creator(self, data_list) -> list:
        for i in data_list:
            name = i.get("first_name")
            last_name = i.get("last_name")
            country = i.get("country").get("title") if i.get("country") else None
            city = i.get("city").get("title") if i.get("city") else None
            bdate = self.__create_iso_date(i.get("bdate")) if i.get("bdate") else None
            sex = "Женский" if i.get("sex") == "1" else "Мужской"
            friend_data_list = [name, last_name, country, city, bdate, sex]
            yield friend_data_list

    def get_prepared_friends_list(self, data_list: dict) -> list[list]:
        preparation_data = data_list.get("response").get('items')
        friends_data_list = []
        for i in self.__dict_creator(preparation_data):
            friends_data_list.append(i)
        return sorted(friends_data_list, key=lambda x: x[0])


