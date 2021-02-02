
class User:

    def __init__(self,userId: st,selected_region: str,selected_province: str,send_notification: int):
        self.userId = userId
        if send_notification != 0:
            self.send_notification = True
        else:
            self.send_notification = False
        self.selected_region = selected_region
        self.selected_province = selected_province